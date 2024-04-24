from cryptography.fernet import Fernet
from pathlib import Path
import random

dict_ = ["abcdefghijklmnopqrstuvwxyz","0123456789","!@#$%^&*-+"]

def generate_password(length):
    password = ""
    for _ in range(length):
        temp = random.choice(dict_)
        char = random.choice(temp)
        if char.isalpha():
            char = random.choice([char.upper(), char.lower()])
        password += char
    return password

def encrypt(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    password_string = encrypted_password.decode('utf-8')
    return encrypted_password

def decrypt(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode('utf-8')

def create_file(password,key):
    path = Path.cwd()
    try:
        with open(path.joinpath('password.txt'), 'a') as file:
            file.write(f"Password:{password.decode('utf-8')[2:-2]}\nKey:{key.decode('utf-8')[2:-2]}\n\n")
            print("Encrypted Password appended to password.txt")
    except FileNotFoundError:
        path.touch(path.joinpath('password.txt'))
        create_file(password,key)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_ = input("1. Generate and Encrypt Password\n2. Encrypt Password\n3. Decrypt\n")
    match input_:
        case "1":
            length = int(input("How long do you want your password: "))
            password = generate_password(length)
            key = Fernet.generate_key() 
            encrypted_password = encrypt(password, key)
            create_file(encrypted_password,key)
        case "2":
            pw = input("Enter the password: ")
            key = Fernet.generate_key() 
            print(encrypt(pw, key))
        case "3":
            pw = input("Enter the encrypted password: ")
            key = input("Enter the encryption key: ")
            print(decrypt(pw, key))
        case _:
            print("Invalid input. Please select a valid option.")
            
    
    
