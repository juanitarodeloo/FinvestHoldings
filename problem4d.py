from problem1d import *
from problem2d import *
import getpass

class Login:
    """Login handles the actions performed when a user tries to login to an already existing account. """
    
    def __init__(self, password_file = "passwd.txt"):
        self.AccessControl = AccessControl()
        self.PasswordManagement = PasswordManagement(password_file)

    def display_permissions(self, username):
        """Prints permissions for the given username"""
        roleNum = self.PasswordManagement.get_role_num(username)
        role = self.AccessControl.get_role_name(roleNum)
        print("UserID:", username, "with the role: ", role.name ,"has the following permissions: ")
        self.AccessControl.print_role_capabilities(role)

    def login_user(self):
        """Logs in user"""
        userNameNotExist = True

        #loop until user enters a valid username
        while(userNameNotExist):
            username = input("Enter username: ")
            passwordRecord = self.PasswordManagement.get_password_record(username)

            if passwordRecord is None:
                print("That username does not exist, try again. ")
            else:
                userNameNotExist = False
                incorrectPassword = True
                saltInFile = self.PasswordManagement.get_salt(username)
                hashedPsswdInFile = self.PasswordManagement.get_hashed_password(username)

                numOfAttempts = 0
                MAX_ATTEMPTS = 5

                #loop until user enters correct password or until they reach max attempts
                while incorrectPassword and numOfAttempts < MAX_ATTEMPTS:
                    
                    userPasswd = getpass.getpass("Enter password: ")  
                    newHash = self.PasswordManagement.hash_password(userPasswd, saltInFile)
                    
                    if(hashedPsswdInFile == newHash):
                        print("\nACCESS GRANTED\n")
                        self.display_permissions(username)
                        incorrectPassword = False
                    else:
                        numOfAttempts += 1
                        print("Incorrect Password. Try again!\n")
                
                if numOfAttempts == MAX_ATTEMPTS:
                    print("Maximum attempts reached. Ending session.")
                    

                



