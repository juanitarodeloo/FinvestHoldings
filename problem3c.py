#Enrol Users
import getpass
import re
from problem2c import *
from problem4c import *
from problem1c import *

def checkPassword(username, passwordToCheck):
    m = ""
    returnVal = True
    # password must not match the username
    if passwordToCheck.lower() == username.lower(): #tested
        returnVal = False
        m += "Password should not match the username. "
    
    # # password must not have a colon in it - for internal reasons
    # if ":" in passwordToCheck: #tested
    #     returnVal = False
    #     m += "Password cannot have a colon. "

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
    
    #TODO: test the following:
    # # must not have common numbers:
    # commonNumsRegex = re.compile(r'\b\D*\d{1,8}\D*\b') #TODO: ask TA about this
    # #fails: Passw0r!123 or sP@sswd123, passes = sP@sswd9j3
    # #fails: sP@sswd123, passes = Hi!7g56sf
    # if commonNumsRegex.match(passwordToCheck): 
    #     returnVal = False
    #     m += "Password has format of common numbers. "
    
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
            m += "Password is too common, choose a new one."
    
    if(returnVal):
        m = 'Password Created!'

    return returnVal, m
        
def userNameExists(username):
    with open('passwd.txt', 'r') as file: #try-catch around
        for line in file:
            usernameInFile = (line.split(":"))[0].strip()
            if username == usernameInFile:
                return True
            
    return False

def getUserRole():
    invalidRole = True
    while(invalidRole):
        userRole = input("What is your role?\nEnter 1 if you are a Client. Enter 2 if you are a Premium Client. Enter 3 if you are" +
            "a Financial Planner. Enter 4 if you are a Financial Advisor. Enter 5 if you are an Investment Analyst. " +
            "Enter 6 if you are a Technical Supprt. Enter 7 if you are a Teller. Enter 8 if you are a Compliance Officer.\n")
        try:
            intUserRoleVal = int(userRole)
            if intUserRoleVal in get_role_values():
                print("\nValid role number. ")
                invalidRole = False
            else:
                print("\nInvalid role number. Try again. ")
        except ValueError:
            print("Please enter a number. Try again.\n")

    return intUserRoleVal



def enrolUser():
    #ask user for username and check that it doesn't already exist
    userNameTaken = True
    while(userNameTaken):
        newUserName = input("Enter new username:\n")
        userNameTaken = userNameExists(newUserName)
        if userNameTaken:
            print("Username already exists. Use a different one. ")

    #ask user for password and check that it is valid
    passwordWorks = False
    while(not passwordWorks):
        userPsswd = getpass.getpass("Enter new password then press Enter:\n")
        passwordWorks, m = checkPassword(newUserName, userPsswd)
  
    #ask user what role they want to have
    userRole = getUserRole()

    #hash password and store record in file
    gen_salt = generate_salt()
    newHashedPsswd = hash_password(userPsswd, gen_salt)
    save_password_record(newUserName, userRole, gen_salt, newHashedPsswd)
    #print(get_password_record(newUserName)) #test to make sure password was saved in files

   


#main
print("\nFinvest Holdings")
print("Client Holdings and Information Systems")
print("---------------------------------------------------------")
#auth a user
invalidInput = True
while(invalidInput):
    enrolOrLogin = input("Enter 1 if you want to create a new account. Enter 2 if you want to login: ")
    if(enrolOrLogin == '1'):
        invalidInput = False
        enrolUser()
    elif(enrolOrLogin == '2'):
        invalidInput = False
        loginUser()
    else:
        print("Invalid Input")



#tests
#TODO: implement a test for each incorrect password condition
#good password: sP@sswd11!

#test enrolling:
#username: sPedari
#password: Hel!12hj






    
    

    


