import os
import datetime

def find_files(directory, extension: str = None, size: int = None, creation_date: str = None, name: str = None):
    print("Finding in directory", directory)
    print("Current working directory", os.getcwd())
    
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        if extension is not None and not file_name.endswith(extension):
            continue 
        
        if size is not None and os.path.getsize(file_path) != size:
            continue 
        
        if name is not None and name not in file_name:
            continue
        
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if creation_date is not None and file_creation_date.strftime("%Y-%m-%d") != creation_date:
            continue
        
        print(file_name)
        
    
find_files("anier", extension = ".py", creation_date="2024-01-31")