from cryptography.fernet import Fernet
pw = input("Masukkan Pasword Anda = ")
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(pw.encode())
print("original string: ", pw)
print("encrypted string: ", encMessage)
