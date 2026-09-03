#Python Encryption Program

import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encrypt
print("***********************************")
original = input("Enter a message to Encrypt: ")
print("***********************************")
cipher = ""

for letter in original:
    index = chars.index(letter)
    cipher += key[index]

print(f"Original message: {original}")
print("***********************************")

print(f"Encrypted message: {cipher}")
print("***********************************")

#Decrypt
print("***********************************")
cipher = input("Enter a message to Decrypt: ")
print("***********************************")
decrypted = ""

for letter in cipher:
    index = key.index(letter)
    decrypted += chars[index]

print(f"To Decrypt message: {cipher}")
print("***********************************")

print(f"Decrypted message: {decrypted}")
print("***********************************")

