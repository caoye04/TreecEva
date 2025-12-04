def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Text processing for a linguistic analysis project
text = "The quick brown fox jumps over the lazy dog while the nimble cat sleeps"

# Process the text
words = text.lower().split()

# Calculate some metrics about the text
char_count = sum(len(word) for word in words)
avg_word_length = char_count / len(words)

# Generate prime factors count for numbers 1 through 10
prime_factors = {}
for i in range(1, 11):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0 and is_prime(j):
            count += 1
    prime_factors[i] = count

# Process words based on various criteria
processed_words = []
for word in words:
    if len(word) <= 10:  # Only include words with 10 or fewer characters
        processed_words.append(word)
    else:
        # This branch is never taken in our example
        truncated = word[:10]
        processed_words.append(truncated)

# Calculate vowel frequencies - not used for final result
vowel_count = {}
for word in processed_words:
    for char in word:
        if char in 'aeiou':
            vowel_count[char] = vowel_count.get(char, 0) + 1

# Filter words by criteria related to prime factors
filtered_count = len([word for word in processed_words if prime_factors[len(word)] == 2])

# Some additional calculations not affecting the result
total_consonants = sum(len([c for c in word if c not in 'aeiou']) for word in processed_words)
distinct_word_count = len(set(processed_words))

print(f"Result: {filtered_count}")