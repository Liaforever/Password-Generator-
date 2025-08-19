import random

letters = "abcdefgilmnoprstuwy"
chars = letters + letters.upper() + "013579" + "-_~"

length = int(input("Enter password length: "))

print("\nCUTE PASSWORDS")
print("*" * (length + 10))

for i in range(3):
    password = "".join(random.choices(chars, k=length))
    print("Password", i+1, ":", password)

print("*" * (length + 10))

messages = [
    "Stay safe online!",
    "Keep your passwords secret!",
    "Secure is cute!",
    "Your data deserves love!"
]
print(random.choice(messages))
