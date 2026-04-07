class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# create user
user1 = User("John", "Doe")

# increment attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# print attempts
print(f"Login attempts: {user1.login_attempts}")

# reset attempts
user1.reset_login_attempts()

# print again
print(f"Login attempts after reset: {user1.login_attempts}")