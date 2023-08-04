def even_filter(data):
    return [num for num in data if num % 2 == 0]

def odd_filter(data):
    return [num for num in data if num % 2 != 0]

if __name__ == "__main__":
    try:
        # Get user input for list of numbers
        numbers_list = list(map(int, input("Enter a list of numbers (separate elements with a space): ").split()))

        # Call the even_filter function and pass the list of numbers as an argument
        even_numbers = even_filter(numbers_list)
        print("Even numbers:", even_numbers)

        # Get user input for dictionary of numbers
        key_value_pairs = input("Enter a dictionary of numbers (key-value pairs separated by a space): ").split()
        numbers_dict = {int(key): int(value) for key, value in zip(key_value_pairs[::2], key_value_pairs[1::2])}

        # Call the odd_filter function and pass the dictionary as an argument
        odd_numbers = odd_filter(list(numbers_dict.values()))
        print("Odd numbers:", odd_numbers)

    except ValueError as e:
        print("Error:", e)
