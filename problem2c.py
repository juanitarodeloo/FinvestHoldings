import hashlib
import secrets

#hash_password hashes the given plaintext password
def hash_password(password):
    salt = secrets.token_bytes()
    sha256 = hashlib.sha256()
    sha256.update(password.encode()+salt) #do we not need to encode the salt? - no because token_bytes returns the salt in bytes
    #hashed_psswd = sha256.hexdigest()
    hashed_psswd = sha256.digest() #should we digest() or hexdigest()?
    return salt, hashed_psswd

#save_password saves users password in a file
def save_password_record(username, salt, hashed_password):
    with open('passwd.txt', 'a') as file:
        #file.write(f"{username}:salt-{salt}:hashedPassword-{hashed_password}\n") #for testing
        file.write(f"{username}:{salt}:{hashed_password}\n")


def get_password_record(username):
    with open('passwd.txt', 'r') as file: #try-catch around
        for line in file:
            usernameInFile = (line.split(':'))[0].strip() #idk if the strip is needed
            if username == usernameInFile:
                return line



#example password record - might need changing
"jrodelo:salt:saltedhash"
#can store a role, or a key of the role


#example username and password
# password = "alPassword"
# username = "arodelo"
# m, s = hash_password(password)
# save_password_record(username, s, m)
# retrieved_record = get_password_record(username)
# print("record for username jrodelo: ", retrieved_record)



