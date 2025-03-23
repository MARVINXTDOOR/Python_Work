class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name):
        """First and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0  
    def describe_user(self):
        """Prints a summary of name."""
        print(f"User: {self.first_name} {self.last_name}")
    def greet_user(self):
        """Prints hello and first name."""
        print(f"Hello, {self.first_name}!")
    def increment_login_attempts(self):
        """login_attempts by 1."""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Resets login_attempts to 0."""
        self.login_attempts = 0

# Create user
user = User("Marvin", "Pearson")

# Call increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login_attempts to verify
print(f"Login attempts: {user.login_attempts}")

# Reset login_attempts
user.reset_login_attempts()

# Print login_attempts to verify reset
print(f"Login attempts after reset: {user.login_attempts}")