import re

def check_password_strength(password):
    """
    Checks the strength of a password against specific criteria.

    Args:
        password (str): The password string to be checked.

    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    # Initialize criteria flags
    has_min_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    feedback_messages = []

    # 1. Minimum length: at least 8 characters long
    if len(password) >= 8:
        has_min_length = True
    else:
        feedback_messages.append("Password must be at least 8 characters long.")

    # 2. Contains both uppercase and lowercase letters
    if any(char.isupper() for char in password):
        has_uppercase = True
    else:
        feedback_messages.append("Password must contain at least one uppercase letter.")

    if any(char.islower() for char in password):
        has_lowercase = True
    else:
        feedback_messages.append("Password must contain at least one lowercase letter.")

    # 3. Contains at least one digit (0-9)
    if any(char.isdigit() for char in password):
        has_digit = True
    else:
        feedback_messages.append("Password must contain at least one digit.")

    # 4. Contains at least one special character (e.g., !, @, #, $, %)
    # Using regex to check for special characters
    special_characters = r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`\-=\\|]'
    if re.search(special_characters, password):
        has_special_char = True
    else:
        feedback_messages.append("Password must contain at least one special character (!@#$%^&* etc.).")

    # Determine overall strength and provide feedback
    is_strong = (has_min_length and has_uppercase and has_lowercase and has_digit and has_special_char)

    if is_strong:
        print("\nPassword Strength: STRONG")
        print("Your password meets all the required criteria.")
    else:
        print("\nPassword Strength: WEAK")
        print("Your password does NOT meet the required criteria. Please address the following:")
        for msg in feedback_messages:
            print(f"- {msg}")

    return is_strong

# Main script to take user input
if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    while True:
        user_password = input("Enter a password to check (or 'quit' to exit): ")
        if user_password.lower() == 'quit':
            print("Exiting password checker. Goodbye!")
            break
        
        # Call the function to check strength and print feedback
        check_password_strength(user_password)
        print("-" * 30) # Separator for next input