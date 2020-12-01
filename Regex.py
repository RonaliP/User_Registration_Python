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
if __name__ == '__main__':
    Regex=RegularExpression()
    print("Enter Firstname")
    First_name=input()
    print(Regex.Firstnamecheck(First_name))