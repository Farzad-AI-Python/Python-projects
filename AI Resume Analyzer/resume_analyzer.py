import re


def read_resume_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("Resume file not found.")
        return None


def analyze_resume(text):
    required_skills = [
        "python", "java", "javascript", "html", "css",
        "sql", "machine learning", "data analysis",
        "communication", "problem solving", "teamwork",
        "git", "github", "excel"
    ]

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    email_found = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    phone_found = re.search(r"\+?\d[\d\s-]{7,}\d", text)

    word_count = len(text.split())

    score = len(found_skills) * 5

    if email_found:
        score += 10
    if phone_found:
        score += 10
    if word_count >= 100:
        score += 10

    if score > 100:
        score = 100

    return found_skills, missing_skills, email_found, phone_found, word_count, score


def display_report(found_skills, missing_skills, email_found, phone_found, word_count, score):
    print("\n==============================")
    print(" AI RESUME ANALYSIS REPORT")
    print("==============================")

    print(f"\nResume Word Count: {word_count}")
    print(f"Resume Score: {score}/100")

    print("\nContact Information:")
    print("Email Found:", "Yes" if email_found else "No")
    print("Phone Found:", "Yes" if phone_found else "No")

    print("\nSkills Found:")
    if found_skills:
        for skill in found_skills:
            print(f"- {skill.title()}")
    else:
        print("No matching skills found.")

    print("\nMissing Recommended Skills:")
    if missing_skills:
        for skill in missing_skills:
            print(f"- {skill.title()}")
    else:
        print("No missing skills. Good match.")

    print("\nSuggestions:")
    if score < 50:
        print("- Add more technical skills and improve resume structure.")
    elif score < 75:
        print("- Resume is decent, but adding more relevant skills can improve it.")
    else:
        print("- Resume looks strong based on the current analysis.")


def main():
    print("==============================")
    print(" AI RESUME ANALYZER")
    print("==============================")

    filename = input("Enter resume text file name: ").strip()

    resume_text = read_resume_file(filename)

    if resume_text:
        result = analyze_resume(resume_text)
        display_report(*result)


main()