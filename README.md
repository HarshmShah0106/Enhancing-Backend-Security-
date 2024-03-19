# Enhancing-Backend-Security-
- **This project focuses on enhancing the security of user authentication by implementing a login page with a robust password storage mechanism.**
- **This is a simple login system that uses SHA-512 hashing and salt to secure user passwords. The system connects to a MySQL database named "your database" and checks if the entered username and password are correct.**
  
# Dependencies
- Python 3.x
- mysql-connector-python
- hashlib (included in Python standard library)

# Code Review
- Define a series of salt strings (salt_ID_1 to salt_ID_20).
- Define a function check_user(result) to check if the user exists in the database.
- Define a function hash_password(password) to hash the password using SHA-512
- Connect to the MySQL database "your database".
- Get the user's entered username add salt value and hash it using hash_password().
- Query the database to find the user with the hashed username.
- If the user exists, retrieve the salt for the user and hash the entered password with the salt.
- Compare the hashed password with the stored password in the database.
- Display the result based on the comparison.

# Usage
- Make sure you have the required dependencies installed.
- Update the MySQL database connection details in the code (host, user, password, and database name).
- Run the code using ```python Password storage.py``` in the terminal **for Registration**.
- Enter the username and password when prompted for registration.
- Run the code using ```python LogIn.py``` in the terminal **for Login and validating User**.
  
  
