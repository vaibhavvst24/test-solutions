def extract_words_with_more_than_four_letters(input_string):
    words_list = input_string.split()
    filtered_list = [word.strip('.,!?()"\'') for word in words_list if len(word.strip('.,!?()"\'')) > 4]
    return filtered_list

if __name__ == "__main__":
    try:
        input_string = input("Enter a paragraph or a sentence: ")

        result_list = extract_words_with_more_than_four_letters(input_string)
        print("Output List:", result_list)

    except Exception as e:
        print("Error:", e)
