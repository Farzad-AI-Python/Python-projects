students = []

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def load_students():
    with open("students.txt", "a") as file:
        pass

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(" - ")

            if len(data) == 3:
                name = data[0]
                mark = float(data[1])
                grade = data[2]
                students.append([name, mark, grade])

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student[0]} - {student[1]} - {student[2]}\n")

def show_results():
    print("\nStudent Results")

    for student in students:
        print(student[0], "-", student[1], "-", student[2])

def show_summary():
    if len(students) == 0:
        print("\nNo student records found")
        return

    total = 0

    for student in students:
        total += student[1]

    average = total / len(students)

    top_student = students[0]
    lowest_student = students[0]

    for student in students:
        if student[1] > top_student[1]:
            top_student = student

        if student[1] < lowest_student[1]:
            lowest_student = student

    passed = 0
    failed = 0

    for student in students:
        if student[1] >= 60:
            passed += 1
        else:
            failed += 1

    print("\nClass Summary")
    print("Total students:", len(students))
    print("Class average:", round(average, 2))
    print("Top student:", top_student[0], "-", top_student[1])
    print("Lowest student:", lowest_student[0], "-", lowest_student[1])
    print("Passed:", passed)
    print("Failed:", failed)

def add_student():
    name = input("Student name: ")
    mark = float(input("Mark: "))
    grade = get_grade(mark)

    students.append([name, mark, grade])
    save_students()

    print("Student added")

def clear_records():
    students.clear()
    save_students()
    print("All records cleared")

load_students()

print("Student Performance Analyzer")

while True:
    print("\n1. Add student")
    print("2. Show results")
    print("3. Show summary")
    print("4. Clear records")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        clear_records()

    elif choice == "5":
        print("Program closed")
        break

    else:
        print("Wrong option")