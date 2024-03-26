# Write a Python program to convert a given camel case string to snake case.
import re 
txt = input(str())
x = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()
# \1_\2    \1 [a-z] and \2[A-Z] заменена на себя же  and _ 
print(x)