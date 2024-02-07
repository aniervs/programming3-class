import os


def find_files(directory, extension=None, min_size=None, max_size=None, contains=None):
    matching_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check file extension (if specified)
            if extension and not filename.endswith(extension):
                continue

            # Check file size (if specified)
            if min_size is not None or max_size is not None:
                file_size = os.path.getsize(file_path)
                if (min_size is not None and file_size < min_size) or \
                        (max_size is not None and file_size > max_size):
                    continue

            # Check if the file name contains a specific string (if specified)
            if contains and contains not in filename:
                continue

            matching_files.append(file_path)

    return matching_files


if __name__ == "__main__":
    directory_to_search = "Directory"
    extension_criteria = ".html"
    min_size_criteria = None
    max_size_criteria = None
    contains_criteria = None  

    found_files = find_files(directory_to_search, extension_criteria, min_size_criteria, max_size_criteria,
                             contains_criteria)

    if found_files:
        print("Matching files:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No matching files found.")
