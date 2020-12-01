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

    def email_check(self, email):
         pattern = "^([A-Za-z]{3,}(.?[A_Za-z0-9]+)?[@][A-Za-z0-9]+[.][a-zA-Z]{2,3}([.]?[a-zA-Z]{2,3})?)$"
         if re.match(pattern, email):
            return "VALID EMAIL"
         else:
             return "INVALID MAIL"

    def Phonenumbercheck(self, number):
        pattern = "^[0-9]{2}[ ][6-9]{1}[0-9]{9}$"
        if re.match(pattern, number):
            return "Valid phone number"
        else:
            return "Invalid phone number"

    def Passwordvalidation(self,Password):
        pattern="(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$^&*()_-])([a-zA-Z0-9]|[^a-zA-Z0-9]){8,}";
        if re.match(pattern,Password):
            return "Valid Password"
        else:
            return "Invalid Password"
if __name__ == '__main__':
    Regex=RegularExpression()
    print("Enter Firstname")
    First_name=input()
    print(Regex.Firstnamecheck(First_name))
    print("Enter Last name")
    Last_name = input()
    print(Regex.Lastnamecheck(Last_name))
    print("ENTER EMAIL")
    mail = input()
    print(Regex.email_check(mail))
    print("Enter Phone number")
    phone_number = input()
    print(Regex.Phonenumbercheck(phone_number))
    print("Enter password")
    password=input()
    print(Regex.Passwordvalidation(password))