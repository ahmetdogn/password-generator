import secrets
import string


def generate_password(length, upper, lower, numbers, symbols):
    chars = ""
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    if chars == "":
        return None

    password = ""
    for i in range(length):
        password += secrets.choice(chars)
    return password


if __name__ == "__main__":
    print("Welcome to your password-generator!")

    length = input("Password length: ")
    if not length.isdigit() or int(length) < 4:
        print("Invalid length, using 12")
        length = 12
    else:
        length = int(length)

    upper = input("Uppercase? (y/n): ") != "n"
    lower = input("Lowercase? (y/n): ") != "n"
    numbers = input("Numbers? (y/n): ") != "n"
    symbols = input("Symbols? (y/n): ") != "n"

    password = generate_password(length, upper, lower, numbers, symbols)
    if password is None:
        print("You have to choose at least one option!")
    else:
        print("Your password:", password)
