myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')

myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())