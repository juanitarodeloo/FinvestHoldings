import hashlib
import secrets

class PasswordManagement:

    #TODO: have a class variable that is the password file that is passed when creating a new instance of this class 
    def __init__(self, password_file = "passwd.txt"):
        self.password_file = password_file


    def hash_password(self, password, salt):
        """Hashes the given plaintext password and salt using SHA-256 encryption algorithm. Returns the hashed password."""
        sha256 = hashlib.sha256()
        #genSalt = secrets.token_hex()
        sha256.update(password.encode() + salt.encode())
        # hashed_psswd = sha256.digest()
        hashed_psswd = sha256.hexdigest()
        return hashed_psswd

    def generate_salt(self):
        """Generates a random secure salt and returns it in hexadecimal format"""
        return secrets.token_hex()

    def save_password_record(self, username, role, salt, hashed_password):
        """Saves the given password record parameters in password file."""
        try:
            with open(self.password_file, 'a') as file:
                record = f"{username}:{role}:{salt}:{hashed_password}\n"
                print("\nWriting this record in the file: ", record) #just for testing
                file.write(record)
        except FileNotFoundError:
            print("Password file not found. ")
        except IOError as e:
            print(f"Error writing to file {e}")

    def get_password_record(self, username):
        """Returns the full password record for the given usernamevthat is stored in the password file. Returns null if username does not exist in file."""
        try:
            with open(self.password_file, 'r') as file:
                for line in file:
                    usernameInFile = (line.split(":"))[0].strip()
                    if username == usernameInFile:
                        return line
        except FileNotFoundError:
            print("Password file not found. ")
        return None

    def get_role_num(self, username):
        """Returns the role number stored in the password file associated with the given username. If there was a problem extracting the role number, this returns None. """
        full_record = self.get_password_record(username)
        role_num = None
        try:
            role_num = int(full_record.split(":")[1].strip())
        except (IndexError, ValueError):
            print("Error extracting the role number from the password file. ")
        return role_num

    def get_salt(self, username):
        """Returns the salt stored in the password file associated with the given username. If there was an error extracting the salt, this returns None. """
        full_record = self.get_password_record(username)
        salt = None
        try:
            salt = full_record.split(":")[2].strip()
        except (IndexError, ValueError):
            print("Error extracting salt.")
        
        return salt

    def get_hashed_password(self, username):
        """Returns the hashed password stored in the password file associated with the given username. If there was a problem extracting the hashed password, this returns None. """
        full_record = self.get_password_record(username)
        hashed_password = None
        try:
            hashed_password = full_record.split(":")[3].strip()
        except (IndexError, ValueError):
            print("Error extracting hashed password.")

        return hashed_password

    def get_password_file(self):
        return self.password_file
                


#example username and password
# password = "jPassword"
# username = "jrodelo" #TODO: should i have a UID or can I make the username unique?
# genSalt = generate_salt()
#print("\ngenerated salt: " , genSalt)

# h = hash_password(password, genSalt)
# save_password_record(username, genSalt, h)



# retrieved_record = get_password_record(username)
# print("record for username jrodelo: ", retrieved_record)

# print("\nsalt in file: " + str(get_salt(username))) #just for testing
# print("\nhashed password in file: " + str(get_hashed_password(username))) #just for testing




