word = input("Enter any word: ")
if len(word) > 1:
    swapped_word = word[-1] + word[1:-1] + word[0]
    print(f"Swapped word: {swapped_word}")
else:
    print("Word must have at least two characters.")