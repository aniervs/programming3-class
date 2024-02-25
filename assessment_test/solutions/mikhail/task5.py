from pathlib import Path
import os

def find_files(directory, extension=None, min_size=None, max_size=None, name_contains=None):
    
    files_found = []
    for file in Path(directory).rglob('*' + extension if extension else '*'):
        if extension and not file.name.endswith(extension):
            continue
        if min_size and file.stat().st_size < min_size:
            continue
        if max_size and file.stat().st_size > max_size:
            continue
        if name_contains and name_contains not in file.name:
            continue
        files_found.append(file)
    return files_found

directory_to_search = 'aoc/mikhail'  
extension_to_search = '.txt' 
files = find_files(directory_to_search, extension=extension_to_search)
for file in files:
    print(file)
