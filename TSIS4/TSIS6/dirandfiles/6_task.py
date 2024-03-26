import string

def gen_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")
gen_files()
