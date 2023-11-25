#Enrol Users
import getpass
import re
from problem2c import *
from problem4c import *
from problem1c import *

class Enrol:

    def __init__(self, password_file = "passwd.txt"):
        self.password_file = password_file
        self.AccessControl = AccessControl()
        self.PasswordManagement = PasswordManagement(password_file)

    def validate_password(self, username, passwordToCheck):
        """Returns True and an empty message if the given password meets the password policy requirements.
        Returns False along with a message that says which requirement(s) the password does not meet. """
        m = ""
        returnVal = True

        # password must not match the username
        if passwordToCheck.lower() == username.lower(): #tested
            returnVal = False
            m += "Password should not match the username. "

        # must be 8-12 chars
        if not 8 <= len(passwordToCheck)<= 12: #tested
            returnVal = False
            m += "Password must be between 8 to 12 characters long. "
        
        # must have at least one uppercase letter:
        if not any(char.isupper() for char in passwordToCheck): #tested
            returnVal = False
            m += "Password must include at least one upper-case letter. "

        # must have at least one lowercase letter
        if not any(char.islower() for char in passwordToCheck): #tested
            returnVal = False
            m += "Password must include at least one lower-case letter. "

        # must have at least one numerical digit
        if not any(char.isdigit() for char in passwordToCheck): #tested
            returnVal = False
            m += "Password must include at least one numerical digit. " 

        # must have at least one special character
        specialChars = {'!', '@', '#', '$', '%', '?', '*'}
        if not any(char in specialChars for char in passwordToCheck): #tested
            returnVal = False
            m += "Password must include at least one special character: {!@#$%?*}. "
        
        # must not have a calendar date format ((MM/DD/YYYY or YYYY-MM-DD)) - is this fine?
        dateFormatsRegex = re.compile(r'\b(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2})\b')
        if dateFormatsRegex.search(passwordToCheck): 
            returnVal = False
            m += "Password should not match the format of common dates. "
        
        # must not have a license plate format
        #the following regex looks for a sequence of characters that have either letters or digits
        licensePlateRegex = re.compile(r'\b[A-Z0-9]{2,8}\b') #Ontarion license plates are between 2 - 8 characters
        if licensePlateRegex.match(passwordToCheck):
            returnVal = False
            m += "Password should not match the format of license plate numbers. "

        # must not have a telephone number format
        phoneNumberRegex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
        if phoneNumberRegex.search(passwordToCheck):
            returnVal = False
            m += "Password should not match the format of common phone numbers. "

        # must not be listed in weak passwords list
        with open('weakPasswords.txt', 'r') as file: #tested
            weakPasswordList = [line.strip() for line in file]
            if passwordToCheck in weakPasswordList:
                returnVal = False
                m += "Password is too common, choose a new one. "
        
        if(returnVal):
            m = 'Password Created!'

        return returnVal, m
            
    def username_exists(self, username):
        """Returns True if the given username exists in the password file. Returns False otherwise. """
        with open(self.password_file, 'r') as file: #try-catch around
            for line in file:
                usernameInFile = (line.split(":"))[0].strip()
                if username == usernameInFile:
                    return True
                
        return False

    def prompt_user_role(self):
        """Prompts user for their role in the company. Returns the number associated with the role they select. """
        invalidRole = True
        while(invalidRole):
            userRole = input("What is your role?\nEnter 1 if you are a Client.\nEnter 2 if you are a Premium Client.\nEnter 3 if you are" +
                "a Financial Planner.\nEnter 4 if you are a Financial Advisor.\nEnter 5 if you are an Investment Analyst.\n" +
                "Enter 6 if you are a Technical Supprt.\nEnter 7 if you are a Teller.\nEnter 8 if you are a Compliance Officer.\n")
            try:
                intUserRoleVal = int(userRole)
                if intUserRoleVal in self.AccessControl.get_role_values():
                    #print("\nValid role number. ")
                    invalidRole = False
                else:
                    print("\nInvalid role number. Try again. ")
            except ValueError:
                print("Please enter a number. Try again.\n")

        return intUserRoleVal



    def prompt_enrol(self):
        """Prompts user for a username and checks that it doesn't already exist in the password file. """
        userNameTaken = True
        while(userNameTaken):
            newUserName = input("Enter new username:\n")
            userNameTaken = self.username_exists(newUserName)
            if userNameTaken:
                print("Username already exists. Use a different one. ")

        #ask user for password and check that it is valid
        passwordWorks = False
        while(not passwordWorks):
            userPsswd = getpass.getpass("Enter new password then press Enter:\n")
            passwordWorks, m = self.validate_password(newUserName, userPsswd)
            if(not passwordWorks):
                print("Invalid password.", m, "\nTry again")
    
        #ask user what role they want to have
        userRole = self.prompt_user_role()

        #hash password and store record in file
        gen_salt = self.PasswordManagement.generate_salt()
        newHashedPsswd = self.PasswordManagement.hash_password(userPsswd, gen_salt)
        self.PasswordManagement.save_password_record(newUserName, userRole, gen_salt, newHashedPsswd)




#tests
#TODO: implement a test for each incorrect password condition
#good password: sP@sswd11!

#test login:
#username: sPedari
#password: Hel!12hj






    
    

    


