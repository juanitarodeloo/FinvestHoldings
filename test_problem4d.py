
import unittest
import sys
from io import StringIO
from problem4d import *

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = Login("test_passwd.txt")
        username = "test_client_username"
        role = 1
        salt = 112233
        hashed_password = "Hel12!0#"
        try:
            with open("test_passwd.txt", 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                file.write(record)
        except FileNotFoundError:
            print("Password file not found. ")
        except IOError as e:
            print(f"Error writing to file {e}")

    def tearDown(self):
        #delete contents of test_passwd.txt file after running tests
        try:
            with open("test_passwd.txt", 'w'):  # 'w' mode truncates the file or creates a new empty file
                pass  # Nothing needs to be written; the file is effectively emptied
        except FileNotFoundError:
            print(f"File 'test_passwd.txt' not found.")


    def test_display_permissions(self):
        #redirect stdout to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.login.display_permissions("test_client_username")

        #reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = "UserID: test_client_username with the role:  CLIENT has the following permissions: \n" \
                          "Resource: ACCOUNT_BALANCE, Permissions: READ\n" \
                          "Resource: INVESTMENT_PORTFOLIO, Permissions: READ\n" \
                          "Resource: FA_CONTACT_DETAILS, Permissions: READ\n" \
                          "Resource: SYSTEM_OFF_HOURS, Permissions: ACCESS\n" \
                          "Resource: SYSTEM_ON_HOURS, Permissions: ACCESS\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()