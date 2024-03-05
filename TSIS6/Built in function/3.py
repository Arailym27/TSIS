# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
txt = input()
if txt == txt[::-1]:
    # способ получить обратную версию строки txt / с отрицательным шагом
    print("palindrome")
else:
    print("not palindrome")