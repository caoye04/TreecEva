text = "programming language evaluation benchmark"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
word_length = len(text)
character_types = len(set(text))
target_value = len([char for char in text if char in vowels])
print(f"Result: {target_value}")