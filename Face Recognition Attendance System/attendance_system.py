import cv2
import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"


def create_attendance_file():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Time"])


def mark_attendance(name):
    create_attendance_file()

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time])

    print(f"Attendance marked for {name} at {time} on {date}")


def start_face_detection():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Camera not found or cannot be opened.")
        return

    attendance_marked = False

    print("Camera started. Press 'q' to quit.")

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Failed to read from camera.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            if not attendance_marked:
                mark_attendance(name)
                attendance_marked = True

        cv2.imshow("Face Recognition Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


def view_attendance():
    create_attendance_file()

    print("\n--- Attendance Records ---")

    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))


def main():
    while True:
        print("\n===================================")
        print(" FACE RECOGNITION ATTENDANCE SYSTEM")
        print("===================================")
        print("1. Start Face Detection")
        print("2. View Attendance Records")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_face_detection()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Invalid option. Please try again.")


main()