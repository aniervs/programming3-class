import os


def find_files(directory, extension: str = None, size: int = None, name: str = None):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if extension is not None and not file_name.endswith(extension):
            continue
        if size is not None and os.path.getsize(file_path) != size:
            continue
        if name is not None and name not in file_name:
            continue
        print(file_name)


find_files("edu", extension=".py")