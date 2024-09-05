import secrets
import string

def generate_password(length):
    """Generates a cryptographically secure random password of the specified length."""
    # Define the character set: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Secure Password Generator")
    
    # Prompt the user to enter the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Please enter a length of at least 6 characters for better security.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and display the secure password
    password = generate_password(length)
    print(f"Generated Secure Password: {password}")

if __name__ == "__main__":
    main()
