import os
def extensions(pathe, extension):
    dir = os.listdir(pathe)
    for i in range(len(dir)):
        if dir[i].endswith(extension):
            print(dir[i])

def size(pathe, size):
    dir = os.listdir(pathe)
    for i in range(len(dir)):
        if os.stat(dir[i]).st_size//1024 == size:
            print(dir[i])

def name(pathe, name):
    dir = os.listdir(pathe)
    for i in range(len(dir)):
        if dir[i].split('.')[0] == name:
            print(dir[i])
            return

path = input("input path to folder in format C:\dir\dir\..\dir")

sz = int(input("Input size of the file in KB: "))
size('C:\harbour\python3\programming3-class\\nikolai', sz)

ex = input("Input extension: ")
extensions('C:\harbour\python3\programming3-class\\nikolai', ex)

nm = input("Input name of the file: ")
name('C:\harbour\python3\programming3-class\\nikolai', nm)




