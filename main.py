from problem4c import *
from problem3c import *

class MainApp:
    """MainApp will hold the main application code that dispatches program. """
    def __init__(self):
        self.login = Login()
        self.enrol = Enrol()
    
    def run(self):
        """Starts authentication program. """
        print("\nFinvest Holdings")
        print("Client Holdings and Information Systems")
        print("---------------------------------------------------------")
        #auth a user
        invalidInput = True
        while(invalidInput):
            enrolOrLogin = input("Enter 1 if you want to create a new account. Enter 2 if you want to login: ")
            if(enrolOrLogin == '1'):
                invalidInput = False
                self.enrol.prompt_enrol()
            elif(enrolOrLogin == '2'):
                invalidInput = False
                print("Login:\n")
                self.login.login_user()
            else:
                print("Invalid Input")


if __name__ == "__main__":
    app = MainApp()
    app.run()

    #admin account:
    #username: admin
    #Passwrd: SySc4810!#
    #Technical Support