import unittest
from problem2d import *

class TestPasswordManagement(unittest.TestCase):

    def setUp(self):
        self.password_manager = PasswordManagement("test_passwd.txt")

    def tearDown(self):
        #delete contents of test_passwd.txt file after running tests
        try:
            with open("test_passwd.txt", 'w'):  # 'w' mode truncates the file or creates a new empty file
                pass  # Nothing needs to be written; the file is effectively emptied
        except FileNotFoundError:
            print(f"File 'test_passwd.txt' not found.")
        

    def test_hash_password(self):
        """Tests hash_password()"""

        #Test that the hash is not just a concatenation of the password and the salt
        hashed_password1 = self.password_manager.hash_password("password123", "salt123")
        self.assertNotEqual("password123" + "salt123", hashed_password1)

        #Test that the same password and hash will produce the same hashed password
        hashed_password2 = self.password_manager.hash_password("password123", "salt123")
        self.assertEqual(hashed_password1, hashed_password2)

    def test_generate_salt(self):
        """Tests generate_salt() by generating different salts and checking that none of them are equal. """

        salt1 = self.password_manager.generate_salt()
        salt2 = self.password_manager.generate_salt()
        self.assertNotEqual(salt1, salt2)

        salt3 = self.password_manager.generate_salt()
        salt4 = self.password_manager.generate_salt()
        self.assertNotEqual(salt3, salt4)
    
    def test_save_password_record(self):
        """Tests save_password_record() by saving a tst user name, role, salt and hashed password in a test password file
        then check the file to see if it is there. """
        username = "test_username"
        role = 1
        salt = "test_salt"
        hashed_password = "test_hashed_password"
        self.password_manager.save_password_record(username, role, salt, hashed_password)
        expected_record = f"{username}:{role}:{salt}:{hashed_password}\n"
        try:
            with open('test_passwd.txt', 'r') as file:
                for line in file:
                    usernameInFile = (line.split(":"))[0].strip()
                    if username == usernameInFile:
                        self.assertEqual(line, expected_record)
                        break
        except FileNotFoundError:
            print("In test_save_password_record: Password file not found. ")
        

    def test_get_password_record(self):
        """Tests get_password_record() by saving a test user name, role, salt and hashed password in a test password file 
        then check the file to see if it is there."""
        username = "test_username2"
        role = 2
        salt = "test_salt2"
        hashed_password = "test_hashed_password2"
        
        try:
            with open('test_passwd.txt', 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                file.write(record)
        except FileNotFoundError:
            print("In test_get_password_record: Password file not found. ")
        except IOError as e:
            print(f"In test_get_password_record: Error writing to file {e}")

        expected_record2 = f"{username}:{role}:{salt}:{hashed_password}\n"
        self.assertEqual(self.password_manager.get_password_record(username), expected_record2)
        

    def test_get_role_num(self):
        """Tests get_role_num() by creating a record in the test password file and comparing the role number from that record 
        with what is expected"""
        #Test getting a role that exists in the password file:
        username = "test_username3"
        role = 3
        salt = "test_salt3"
        hashed_password = "test_hashed_password3"
        
        try:
            with open('test_passwd.txt', 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                file.write(record)
        except FileNotFoundError:
            print("In test_get_role_num: Password file not found. ")
        except IOError as e:
            print(f"In test_get_role_num: Error writing to file {e}")
        
        self.assertEqual(self.password_manager.get_role_num(username), 3)
        #Test getting a role that does not exists in the password file:
        self.assertNotEqual(self.password_manager.get_role_num(username), 10)

    def test_get_salt(self):
        """Tests get_salt() by creating a record in the test password file and comparing the salt from that record 
        with what is expected"""
        #Test getting a salt that exists in the password file:
        username = "test_username4"
        role = 4
        salt = "test_salt4"
        hashed_password = "test_hashed_password4"
        
        try:
            with open('test_passwd.txt', 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                file.write(record)
        except FileNotFoundError:
            print("In test_get_salt: Password file not found. ")
        except IOError as e:
            print(f"In test_get_salt: Error writing to file {e}")

        self.assertEqual(self.password_manager.get_salt(username), "test_salt4")
        #Test getting a salt that does not exists in the password file:
        self.assertNotEqual(self.password_manager.get_salt(username), "invalid_salt")


    def test_get_hashed_password(self):
        """Tests get_hashed_password() by creating a record in the test password file and comparing the hashed password from that record 
        with what is expected"""
        #Test getting a hashed password that exists in the password file:
        username = "test_username5"
        role = 5
        salt = "test_salt5"
        hashed_password = "test_hashed_password5"
        
        try:
            with open('test_passwd.txt', 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                file.write(record)
        except FileNotFoundError:
            print("In test_get_hashed_password: Password file not found. ")
        except IOError as e:
            print(f"In test_get_hashed_password: Error writing to file {e}")
        
        self.assertEqual(self.password_manager.get_hashed_password(username), "test_hashed_password5")

        #Test getting a hashed password that does not exists in the password file:
        self.assertNotEqual(self.password_manager.get_salt(username), "invalid_hashed_password")

if __name__ == '__main__':
    unittest.main()