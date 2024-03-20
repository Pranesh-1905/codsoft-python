import random
import string

def passgen(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return
        password = passgen(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter integer for the length.")

if __name__ == "__main__":
    main()
