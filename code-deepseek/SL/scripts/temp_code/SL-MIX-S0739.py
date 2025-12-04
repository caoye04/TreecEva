text = "Programming in Python is fun and educational!"
letters = [char for char in text if char.isalpha()]
uppercase_letters = [char.upper() for char in letters]
unique_count = len(set([char.upper() for char in text if char.isalpha()]))
print(f"Result: {unique_count}")