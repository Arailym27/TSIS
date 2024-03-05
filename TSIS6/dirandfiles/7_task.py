with open('TSIS-6/exaples/demofile2.txt', 'r') as file1, open('TSIS-6/exaples/newFile.txt', 'a') as file2:
  for line in file1:
    file2.write(line)
