def calculate(num1, op, num2):

    if op == "+":
        return num1 + num2

    elif op == "-":
        return num1 - num2

    elif op == "*":
        return num1 * num2

    elif op == "/":

        if num2 == 0:
            return "Cannot divide by zero"

        return num1 / num2

    elif op == "**":
        return num1 ** num2

    elif op == "%":
        return num1 % num2

    else:
        return "Wrong operation"


history = []

with open("history.txt", "a") as file:
    pass

with open("history.txt", "r") as file:
    for line in file:
        history.append(line.strip())


print("Advanced Calculator")

while True:

    choice = input("\nType 'clear' to delete history or press Enter to continue: ")

    if choice == "clear":
        open("history.txt", "w").close()
        history.clear()
        print("History cleared")
        continue

    num1 = float(input("First number: "))
    op = input("Operation (+ - * / ** %): ")
    num2 = float(input("Second number: "))

    answer = calculate(num1, op, num2)

    print("Answer:", answer)

    record = f"{num1} {op} {num2} = {answer}"
    history.append(record)

    with open("history.txt", "a") as file:
        file.write(record + "\n")

    print("\nHistory:")

    for item in history:
        print(item)

    again = input("\nDo another calculation? (yes/no): ")

    if again == "no":
        print("Calculator closed")
        break