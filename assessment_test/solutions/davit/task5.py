import os
import datetime

def find_files(directory, extension=None, min_size=None, max_size=None, from_date=None, to_date=None, name_contains=None):
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if extension and not file.endswith(extension):
                    continue

                size = os.path.getsize(file_path)
                if (min_size and size < min_size) or (max_size and size > max_size):
                    continue

                creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path)).date()
                if (from_date and creation_date < from_date) or (to_date and creation_date > to_date):
                    continue

                if name_contains and name_contains not in file:
                    continue

                matched_files.append(file_path)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    return matched_files

print(find_files("/Users/qwerty/Documents/py-3/programming3-class", '.py'))
print(find_files("/Users/qwerty/Documents/py-3/programming3-class", '.py', min_size=202000000))