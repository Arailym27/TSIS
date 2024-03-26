# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
txt = "AraiKabykenovaIS"

def letters(txt):
    num_upper = sum(1 for char in txt if char.isupper())
    num_lower =sum(1 for char in txt if char.islower())
    return num_lower , num_upper
num_lower , num_upper = letters(txt)
print(num_upper)
print(num_lower)