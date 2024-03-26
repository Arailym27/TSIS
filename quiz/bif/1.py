# Write a Python program with builtin function to multiply all the numbers in a list
import math 
num = [1 , 2 , 3, 4 , 5]
result = math.prod(num)
# math.prod() для умножения всех чисел в этом списке. 
print(result)


# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
txt = "AraiKabykenovaIS"

def letters(txt):
    num_upper = sum(1 for char in txt if char.isupper())
    num_lower =sum(1 for char in txt if char.islower())
    return num_lower , num_upper
num_lower , num_upper = letters(txt)
print(num_upper)
print(num_lower)



# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
txt = input()
if txt == txt[::-1]:
    # способ получить обратную версию строки txt / с отрицательным шагом
    print("palindrome")
else:
    print("not palindrome")


# Write a Python program that invoke square root function after specific milliseconds.
import time  # time.sleep()чтобы создать паузу в выполнении 
import math  # math.sqrt()

Square_root = 25100
miliseconds = 2123
time.sleep(miliseconds / 1000)
print("Square root of 25100 after 2123 miliseconds is ", math.sqrt(Square_root))



# Write a Python program with builtin function that returns True if all elements of the tuple are true
tuple1 = (True , False , True)
tuple2 = (True , True  , True)
print(all(tuple1))
print(all(tuple2))