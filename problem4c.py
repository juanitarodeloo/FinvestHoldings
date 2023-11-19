from problem1c import *
from problem2c import *
import getpass

class Login:
    """Login handles the actions performed when a user tries to login to an already existing account. """
    
    def __init__(self):
        self.AccessControl = AccessControl()
        self.PasswordManagement = PasswordManagement()

    def display_permissions(self, username):
        """Prints permissions for the given username"""
        print("UserID:", username, "has the following permissions: ")
        roleNum = self.PasswordManagement.get_role_num(username)
        role = self.AccessControl.get_role_name(roleNum)
        self.AccessControl.print_role_capabilities(role)
        # role_capabilities = capabilities_list.get(Role.role_name, {})
        # print(role_capabilities)

    def login_user(self):
        """Logs in user"""
        userNameNotExist = True

        #loop until user enters a valid username
        while(userNameNotExist):
            username = input("Enter username: ")
            passwordRecord = self.PasswordManagement.get_password_record(username)
            #print("full hashed record in file: " + passwordRecord)

            if passwordRecord is None:
                print("That username does not exist, try again. ")
            else:
                userNameNotExist = False
                incorrectPassword = True
                saltInFile = self.PasswordManagement.get_salt(username)
                hashedPsswdInFile = self.PasswordManagement.get_hashed_password(username)
                # print("\nsalt in file: " + saltInFile) #just for testing
                # print("hashed password in file: " + str(hashedPsswdInFile))

                numOfAttempts = 0
                MAX_ATTEMPTS = 5

                #loop until user enters correct password or until they reach max attempts
                while incorrectPassword and numOfAttempts < MAX_ATTEMPTS:
                    
                    userPasswd = getpass.getpass("Enter password: ")  
                    print("You entered: ", userPasswd) #TODO: just for testing, take out
                    newHash = self.PasswordManagement.hash_password(userPasswd, saltInFile)
                    
                    #print("\ncalculated hash from user input: " + newHash)
                    if(hashedPsswdInFile == newHash):
                        print("\nACCESS GRANTED\n")
                        self.display_permissions(username)
                        incorrectPassword = False
                    else:
                        numOfAttempts += 1
                        print("Incorrect Password. Try again!\n")
                
                if numOfAttempts == MAX_ATTEMPTS:
                    print("Maximum attempts reached. Ending session.")
                    

                



