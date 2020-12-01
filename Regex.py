import re
"""
Below is the code to validate first name entered by user
First use case
"""
class RegularExpression():
    print("Welcome to User registration program")
    def Firstnamecheck(self,first_name):
        pattern="^[A-Z]{1}[a-z]{2,}$"
        if re.match(pattern,first_name):
            return "Valid Firstname"
        else:
            return "Invalid Firstname,Try again"

    def Lastnamecheck(self, last_name):
        pattern = "^[A-Z]{1}[a-z]{2,}$"
        if re.match(pattern, last_name):
            return "Valid Last name"
        else:
            return "Invalid Last name"

"""
Above function will validate last name
2nd use case
"""
if __name__ == '__main__':
    Regex=RegularExpression()
    print("Enter Firstname")
    First_name=input()
    print(Regex.Firstnamecheck(First_name))
    print("Enter Last name")
    Last_name = input()
    print(Regex.Lastnamecheck(Last_name))