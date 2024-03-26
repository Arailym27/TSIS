# Write a Python program that invoke square root function after specific milliseconds.
import time  # time.sleep()чтобы создать паузу в выполнении 
import math  # math.sqrt()

Square_root = 25100
miliseconds = 2123
time.sleep(miliseconds / 1000)
print("Square root of 25100 after 2123 miliseconds is ", math.sqrt(Square_root))