def calculator():
    print("=" * 30)
    print("      Basic Calculator")
    print("=" * 30)
    print("Operations: +  -  *  /  %  **")
    print("Type 'quit' to exit\n")

    while True:
        try:
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':
                print("Goodbye!")
                break

            operator = input("Enter operator (+, -, *, /, %, **): ")
            if operator.lower() == 'quit':
                print("Goodbye!")
                break

            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                print("Goodbye!")
                break

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!\n")
                    continue
                result = num1 / num2
            elif operator == '%':
                if num2 == 0:
                    print("Error: Cannot modulo by zero!\n")
                    continue
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("Error: Invalid operator! Use +, -, *, /, %, **\n")
                continue

            # Display result cleanly (remove .0 for whole numbers)
            result_display = int(result) if result == int(result) else result
            num1_display = int(num1) if num1 == int(num1) else num1
            num2_display = int(num2) if num2 == int(num2) else num2

            print(f"\nResult: {num1_display} {operator} {num2_display} = {result_display}\n")
            print("-" * 30)

        except ValueError:
            print("Error: Please enter valid numbers!\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    calculator()