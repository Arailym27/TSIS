import os 
path = input("каталог: ")
list = ['Arai', 'Fariza', 'Sultan']

with open('TSIS-6/exaples/demofile.txt' , 'w') as file:
    for i in list:
        file.write(i + '\n')
file.close()