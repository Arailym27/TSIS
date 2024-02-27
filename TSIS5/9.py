# Write a Python program to insert spaces between words starting with capital letters.
import re
txt = input(str())
x = re.sub(r"([A-Z]+)", r" \1", txt)
# +	One or more occurrences
# r" \1": Это строка для замены
# \1 представляет собой первую группу, найденную в регулярном выражении 
print(x)