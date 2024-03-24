class User:

    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = birthYear

    def get_name(self):
        return str(self.name).upper()

    def age(self, current_year):
        return current_year - self.birthYear


if __name__ == "__main__":
    user = User("John", 1999)
    age = user.age(2023)
    print(age)
    print(user.get_name())
