import random
import string

# Define the length of the password
password_length = 10

# Define the character set for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for i in range(password_length))

# Display the password to the user
print(f"Your new password is: {password}")
