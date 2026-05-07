def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey"]
    study_words = ["study", "learning", "focus"]
    ai_words = ["ai", "artificial intelligence", "machine learning"]
    python_words = ["python", "coding", "programming"]
    exam_words = ["exam", "test", "quiz"]
    english_words = ["english", "speaking", "grammar"]

    if any(word in user_input for word in greetings):
        return "Hello! I am your AI Study Assistant."

    elif any(word in user_input for word in python_words):
        return "Python is very useful for AI, automation, and software development."

    elif any(word in user_input for word in ai_words):
        return "Artificial Intelligence helps machines learn patterns and make decisions."

    elif any(word in user_input for word in study_words):
        return "Studying consistently every day is more effective than studying once in a while."

    elif any(word in user_input for word in exam_words):
        return "Practice and revision are important for exam success."

    elif any(word in user_input for word in english_words):
        return "Daily speaking and listening practice can improve your English faster."

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}"

    elif "bye" in user_input:
        return "Goodbye! Keep learning and improving."

    else:
        return "I am still learning. Please ask about study, AI, Python, exams, or English."


def main():
    print("=== AI Study Assistant ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()