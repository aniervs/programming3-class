#criteria - filename contains capital letters

import os

def find_files(directory):
    ans = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for char in file:
                if char.isupper():
                    filename = os.path.join(root, file)
                    ans.append(filename)
                break
    return ans

for filename in find_files('/'):
    print('Found file with capital letters:', filename)
