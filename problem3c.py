#Enrol Users
import getpass
import re
from problem2c import *

def checkPassword(username, passwordToCheck):
    m = ""
    returnVal = True
    # password must not match the username
    if passwordToCheck.lower() == username.lower():
        returnVal = False
        m += "Password should not match the user ID. "
    
    # must be 8-12 chars
    if not 8 <= len(passwordToCheck)<= 12:
        returnVal = False
        m += "Password must be between 8 to 12 characters long. "
    
    # must have at least one uppercase letter:
    if not any(char.isupper() for char in passwordToCheck):
        returnVal = False
        m += "Password must include at least one upper-case letter. "

    # must have at least one lowercase letter
    if not any(char.islower() for char in passwordToCheck):
        returnVal = False
        m += "Password must include at least one lower-case letter. "

    # must have at least one numerical digit
    if not any(char.isdigit() for char in passwordToCheck):
        returnVal = False
        m += "Password must include at least one numerical digit. " 

    # must have at least one special character
    specialChars = {'!', '@', '#', '$', '%', '?', '*'}
    if not any(char in specialChars for char in passwordToCheck):
        returnVal = False
        m += "Password must include at least one special character: {!@#$%?*}. "
    
    # must not have common numbers:
    commonNumsRegex = re.compile(r'\b\d{1,8}\b')
    if commonNumsRegex.search(passwordToCheck):
        returnVal = False
        m += "Password has format of common numbers. "
    
    # must not have a calendar date format ((MM/DD/YYYY or YYYY-MM-DD)) - is this fine?
    dateFormatsRegex = re.compile(r'\b(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2})\b')
    if dateFormatsRegex.search(passwordToCheck):
        returnVal = False
        m += "Password should not match the format of common dates. "
    
    # must not have a license plate format
    licensePlateRegex = re.compile(r'\b[A-Z0-9]{2,8}\b') #Ontarion license plates are between 2 - 8 characters
    if licensePlateRegex.search(passwordToCheck):
        returnVal = False
        m += "Password should not match the format of license plate numbers. "

    # must not have a telephone number format
    phoneNumberRegex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
    if phoneNumberRegex.search(passwordToCheck):
        returnVal = False
        m += "Password should not match the format of common phone numbers. "

    # must not be listed in weak passwords list
    with open('weakPasswords.txt', 'r') as file:
        weakPasswordList = [line.strip() for line in file]
        if passwordToCheck in weakPasswordList:
            returnVal = False
            m += "Password is too common, choose a new one."
    
    if(returnVal):
        m = 'Password Created'

    return returnVal, m
        

def enrolUser():
    newUserName = input("Enter new username:\n")
    #print(newUserName)
    userPsswd = getpass.getpass("Enter new pasword then press Enter:\n")
    #print(userPsswd)
    passwordWorks, m = checkPassword(newUserName, userPsswd)
    print(m)
    if(passwordWorks):   
        newSalt, newHashesPsswd = hash_password(userPsswd)
        save_password_record(newUserName, newSalt, newHashesPsswd)
        print(get_password_record(newUserName)) #test to make sure password was saved in file

    #TODO: ask user what role they want to have

print("Finvest Holdings")
print("Client Holdings and Information Systems")
print("---------------------------------------------------------")
enrolOrLogin = input("Enter 1 if you want to create a new account. Enter 2 if you want to login: ")
#enroling a user
if(enrolOrLogin == '1'):
    enrolUser()


#tests
#good password: SecureP@ssw0rd11!
#




    
    

    


