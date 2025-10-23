from functools import reduce

dish_list = ['apple', 'banana', 'cherry']

# Tokenize and convert each character to its numeric value
char_values = [
    [ord(char) - ord('a') + 1 for char in dish]
    for dish in dish_list
]

# Apply divide and conquer strategy using reduce to sum values per dish, then overall
prep_times_per_dish = [
    reduce(lambda x, y: x + y, dish_chars)
    for dish_chars in char_values
]

total_prep_time = reduce(lambda x, y: x + y, prep_times_per_dish)

print(f"Result: {total_prep_time}")