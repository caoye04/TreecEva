# Analyzing letters in a phrase
phrase = "hello world"
letters_count = {}

# Count occurrences of each character
for char in phrase:
    if char.isalpha():
        letters_count[char] = letters_count.get(char, 0) + 1

# Find the longest word
words = phrase.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Filter out vowels from the longest word
filtered_word = ""
for char in longest_word:
    if char.lower() not in "aeiou":
        filtered_word += char

# Count unique consonants in the filtered word
unique_letters = len(set(filtered_word))

print(f"Result: {unique_letters}")