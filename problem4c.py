from problem1c import *
from problem2c import *
import getpass



def displayPermissions(username):
    print("UserID: ", username, " has the following permissions: ")
    roleNum = get_role_num(username)
    role = get_role_name(roleNum)
    print_role_capabilities(role)
    
    # role_capabilities = capabilities_list.get(Role.role_name, {})
    # print(role_capabilities)

#login Users
def loginUser(): #TODO: implement a max number of attempts
    userNameNotExist = True

    #loop until user enters a valid username
    while(userNameNotExist):
        username = input("Enter username: ")
        passwordRecord = get_password_record(username)
        #print("full hashed record in file: " + passwordRecord)

        if passwordRecord is None:
            print("Record with that username does not exist, try again. ")
        else:
            userNameNotExist = False
            incorrectPassword = True
            saltInFile = get_salt(username)
            hashedPsswdInFile = get_hashed_password(username)
            # print("\nsalt in file: " + saltInFile) #just for testing
            # print("hashed password in file: " + str(hashedPsswdInFile))

            numOfAttempts = 0
            MAX_ATTEMPTS = 5

            #loop until user enters correct password
            while incorrectPassword and numOfAttempts < MAX_ATTEMPTS:
                
                userPasswd = getpass.getpass("Enter password: ")  
                print("You entered: ", userPasswd)
                newHash = hash_password(userPasswd, saltInFile)
                
                #print("\ncalculated hash from user input: " + newHash)
                if(hashedPsswdInFile == newHash):
                    print("ACCESS GRANTED")
                    displayPermissions(username)
                    incorrectPassword = False
                else:
                    numOfAttempts += 1
                    print("Incorrect Password. Try again! ")
            
            if numOfAttempts == MAX_ATTEMPTS:
                print("Maximum attempts reached. Ending session.")
                #TODO: call init

            



