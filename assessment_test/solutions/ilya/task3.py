def find_duplicates_in_sequence(sequence):
    a = set()
    duplicates = []

    for element in sequence:
        if element in a:
            if element not in duplicates:
                duplicates.append(element)
        else:
            a.add(element)

    return duplicates

user_input = input("Enter a sequence of numbers separated by spaces: ")
input_data = [int(num) for num in user_input.split()]

print(find_duplicates_in_sequence(input_data))