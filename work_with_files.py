file = open('file1.txt', 'a')
i = input('insert your name')
file.write(i)
file.write('\n')
file.close()

file = open('file1.txt', 'r')
print(file.readline())   # on single line
print(file.readlines())  # list of all the lines
print(file.read())
print(file.read(2))
print(file.tell())  # index of the curser
print(file.seek(0)) # change the position of the curser
file.close()

