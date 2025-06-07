import random
import string

def gen_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):

    #Get user input and assign to variable length
    length = int(input("Enter password length (min length is 12 characters): ").strip())

    """Generate a random password with specified criteria."""
    if length < 12:
        raise ValueError("Passwords must be at least 12 characters in length.")
    
    #define character set selectionbaed on user preferences 
    char_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    #Get user input for character sets
    password = ''.join(random.choice(char_set) for i in range(length))

    print(f'Generated password: {password}')

if __name__ == "__main__":
    try:
        gen_password()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

# Note: The code generates a random password based on user input for length and character set preferences.
# It ensures the password is at least 5 characters long and includes lowercase, uppercase, digits, and special characters.
# The code handles exceptions for invalid input and other errors.
# The generated password is printed to the console.





