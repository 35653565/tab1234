import datetime

# user class implementation
class User:
    # initialise user
    def __init__(self, name, password, location):
        self.name = name
        self.password = password
        self.location = location
        self.signupdate = datetime.datetime.now().date()

    # the user can change their password and location
    def update(self, password, location):
        self.password = password
        self.location = location

    # login method for user
    def login(self, password):
        # if the password is correct the user gets a welcome message
        if password == self.password:
            print("Welcome, You have logged in successfully!!")
        else:
            print("Incorrect Password!!")

    # User gets a goodbye message
    def logout(self):
        print("Good bye!!")


# main function to test user class
def main():
    # create User
    user = User("Ashton", "35653565", "Miami, Fl")

    # login for the user
    user.login("304079")  # Incorrect Password
    user.login("35653565")  # correct Password

    # change Password and location
    user.update("3132", "Canada")

    # login again
    user.login("3132")

    # logout
    user.logout()




