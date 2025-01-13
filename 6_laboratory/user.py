class UserAccount:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.__password = password

    def set_password(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password
    

user = UserAccount("Ilya", "ilya@gmail.com", 123)
user.set_password(456)
print(user.check_password(456))  # True
print(user.check_password(123))  # False