import random, string
letters = "abcdefgilmnoprstuwy"
numbers = "013579"
symbols = "-_~"
chars = letters + letters.upper() + numbers + symbols
password = "".join(random.choices(chars, k=10))
print("Here’s your cute password: ", password)
