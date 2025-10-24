class InputVerifier:
    def __init__(self):
        self.letter = input("Enter a letter: ")
        self.number = input("Enter a number: ")

    def verify(self):
        if self.letter == "P" and self.number == "7":
            print("Hello World")
        else:
            print("Invalid input. Please enter 'P' and '7'.")

user = InputVerifier()
user.verify()
