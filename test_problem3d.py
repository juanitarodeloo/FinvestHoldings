import unittest
from unittest.mock import patch
from problem3d import *

class TestEnrol(unittest.TestCase):

    def setUp(self):
        self.enrol = Enrol("test_passwd.txt")
        username = "admin"
        role = 6
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

    def test_validate_password(self):
        """Tests validate_password() by passing the actual method example passwords that should violate 
        each condition and test passwords that should pass all conditions"""

        #Checks that the password isn't equal to username
        result, message = self.enrol.validate_password("john_doe", "john_doe")
        self.assertFalse(result)
        self.assertTrue("Password should not match the username. " in message)

        #Checks that the password is too short
        result, message = self.enrol.validate_password("john_doe", "short")
        self.assertFalse(result)
        self.assertTrue("Password must be between 8 to 12 characters long. " in message)

        #Checks that the password is too long
        result, message = self.enrol.validate_password("john_doe", "PasswordThatIsWayTooLongToPassThisCheck")
        self.assertFalse(result)
        self.assertTrue("Password must be between 8 to 12 characters long. " in message)

        #Checks that the password must have at least one upper case letter
        result, message = self.enrol.validate_password("john_doe", "nouppercases")
        self.assertFalse(result)
        self.assertTrue("Password must include at least one upper-case letter. " in message)

        #Checks that the password must have at least one lower case letter
        result, message = self.enrol.validate_password("john_doe", "NOLOWERCASES")
        self.assertFalse(result)
        self.assertTrue("Password must include at least one lower-case letter. " in message)

        #Checks that the password must have at least one digit
        result, message = self.enrol.validate_password("john_doe", "PsswdNoDigit")
        self.assertFalse(result)
        self.assertTrue("Password must include at least one numerical digit. " in message)

        #Checks that the password must have at least one special character
        result, message = self.enrol.validate_password("john_doe", "N0Chars083")
        self.assertFalse(result)
        self.assertTrue("Password must include at least one special character: {!@#$%?*}. " in message)

        #Checks that the password is not in a date format
        result, message = self.enrol.validate_password("john_doe", "12/04/2023")
        self.assertFalse(result)
        self.assertTrue("Password should not match the format of common dates. " in message)

        #Checks that the password is not in a license plate format
        result, message = self.enrol.validate_password("john_doe", "AB123CD")
        self.assertFalse(result)
        self.assertTrue("Password should not match the format of license plate numbers. " in message)

        #Checks that the password is not in a telephone number format
        result, message = self.enrol.validate_password("john_doe", "123-456-7890")
        self.assertFalse(result)
        self.assertTrue("Password should not match the format of common phone numbers. " in message)

        #Checks that the password is not listed in the weak passwords list
        result, message = self.enrol.validate_password("john_doe", "passw0rd")
        self.assertFalse(result)
        self.assertTrue("Password is too common, choose a new one. " in message)

        #Checks that a valid example password passes all the above checks
        result, message = self.enrol.validate_password("john_doe", "Hel12!0#")
        self.assertTrue(result)
        self.assertTrue("Password Created!" in message)


    def test_username_exists(self):
        """Tests username_exists() returns the correct boolean when checking is a username exists. """
        #Checks that an existing username exists
        self.assertTrue(self.enrol.username_exists("admin"))
        #Checks that a non existing username exists
        self.assertFalse(self.enrol.username_exists("Admin"))
        #Checks that a non existing username exists
        self.assertFalse(self.enrol.username_exists("DoesntExist"))

    @patch("builtins.input", test_inputs=["1", "13", "invalid"])
    def test_prompt_user_role(self, mock_input):
        # Test valid role input
        with patch("builtins.input", return_value="1"):
            result = self.enrol.prompt_user_role()
            self.assertEqual(result, 1)

        # Test invalid role input, still a number
        with patch("builtins.input", return_value="13"):
            self.assertRaises(ValueError)

        # Test invalid role input, not a number
        with patch("builtins.input", return_value="invalid"):
            self.assertRaises(ValueError)
                

if __name__ == '__main__':
    unittest.main()