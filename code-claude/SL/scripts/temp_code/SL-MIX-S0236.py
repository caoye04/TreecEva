# Analyzing text data for common character patterns

text1 = "programming challenges require logical thinking"
text2 = "debugging requires analytical reasoning"
text3 = "algorithms showcase elegant solutions"

# Extract character sets from each text
chars1 = set(text1.replace(" ", ""))
chars2 = set(text2.replace(" ", ""))
chars3 = set(text3.replace(" ", ""))

# Calculate some statistics for analysis
avg_length = (len(text1) + len(text2) + len(text3)) / 3
total_unique = len(chars1.union(chars2).union(chars3))

# Find characters that appear in at least two texts
appears_in_two = (chars1 & chars2) | (chars2 & chars3) | (chars1 & chars3)

# Find characters that appear in all texts
common_elements = chars1.intersection(chars2).intersection(chars3)

# Count vowels in common elements
vowels = {'a', 'e', 'i', 'o', 'u'}
common_vowels = common_elements & vowels

# Calculate frequency of common characters in text1
frequency = {}
for char in common_elements:
    count = text1.count(char)
    frequency[char] = count

# Analyze character positions
position_sums = {}
for char in common_elements:
    positions = [pos for pos, c in enumerate(text1) if c == char]
    position_sums[char] = sum(positions) if positions else 0

# Find the most frequent common character
max_freq = 0
max_char = ''
for char, freq in frequency.items():
    if freq > max_freq:
        max_freq = freq
        max_char = char

# Calculate weighted score based on frequency and position
weighted_score = sum(frequency.values()) - len(common_vowels)

# Count unique common elements
unique_count = len(common_elements)

print(f"Result: {unique_count}")
