def merge_lists_into_dictionary(keys_list, values_list):
    if len(keys_list) != len(values_list):
        raise ValueError("Both lists should be of the same size.")
    
    if len(keys_list) != len(set(keys_list)):
        raise ValueError("The first list must contain unique elements.")

    merged_dict = dict(zip(keys_list, values_list))
    return merged_dict

if __name__ == "__main__":
    try:
        keys_list = input("Enter the list of keys (separate elements with a space): ").split()
        values_list = input("Enter the list of values (separate elements with a space): ").split()

        merged_dict = merge_lists_into_dictionary(keys_list, values_list)
        print("Merged Dictionary:", merged_dict)

    except ValueError as e:
        print("Error:", e)
