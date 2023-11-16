import hashlib
import secrets


def hash_password(password, salt):
    """ Hashes the given plaintext password and salt using SHA-256 encryption algorithm. Returns the hashed password."""
    sha256 = hashlib.sha256()
    #genSalt = secrets.token_hex()
    sha256.update(password.encode() + salt.encode())
    # hashed_psswd = sha256.digest()
    hashed_psswd = sha256.hexdigest()
    return hashed_psswd

def generate_salt():
    return secrets.token_hex()

def save_password_record(username, role, salt, hashed_password):
    """Saves the given password record parameters in password file."""
    
    with open('passwd.txt', 'a') as file:
        #file.write(f"{username}:salt-{salt}:hashedPassword-{hashed_password}\n") #for testing
        record = f"{username}:{role}:{salt}:{hashed_password}\n"
        print("\nWriting this record in the file: ", record) #just for testing
        file.write(record) #TODO: put the f statement directly in here


def get_password_record(username): #this works
    """Returns the full password record for the given usernamevthat is stored in the password file. Returns null if username does not exist in file."""
    
    with open('passwd.txt', 'r') as file: #try-catch around
        for line in file:
            usernameInFile = (line.split(":"))[0].strip()
            if username == usernameInFile:
                return line

def get_role_num(username):
    full_record = get_password_record(username)
    return int(full_record.split(":")[1].strip())

def get_salt(username):
    full_record = get_password_record(username)
    return full_record.split(":")[2].strip()

def get_hashed_password(username):
    full_record = get_password_record(username)
    return full_record.split(":")[3].strip()


                


#example username and password
password = "jPassword"
username = "jrodelo" #TODO: should i have a UID or can I make the username unique?
genSalt = generate_salt()
#print("\ngenerated salt: " , genSalt)

# h = hash_password(password, genSalt)
# save_password_record(username, genSalt, h)



# retrieved_record = get_password_record(username)
# print("record for username jrodelo: ", retrieved_record)

# print("\nsalt in file: " + str(get_salt(username))) #just for testing
# print("\nhashed password in file: " + str(get_hashed_password(username))) #just for testing




