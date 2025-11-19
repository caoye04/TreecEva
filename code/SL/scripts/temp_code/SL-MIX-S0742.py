import math

def tokenize(document):
    return [token.strip(',.!?;') for token in document.split()]

def encode_token(token):
    return sum(ord(char) for char in token.lower())

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

technical_document = "The quick brown fox jumps over the lazy dog. Programming languages evolve rapidly. Python excels in readability and versatility."

tokens = tokenize(technical_document)
encoded_values = [encode_token(token) for token in tokens]
unique_encoded_set = frozenset(encoded_values)

# Compute mean of encoded values
mean_encoded = sum(encoded_values) / len(encoded_values)

# Compute variance
variance = sum((x - mean_encoded) ** 2 for x in encoded_values) / len(encoded_values)

# Apply Fibonacci transformation to the count of unique encodings
unique_count_transformed = fibonacci(len(unique_encoded_set))

# Calculate lexical diversity index
lexical_diversity_index = int(math.sqrt(variance) * unique_count_transformed)

print(f"Result: {lexical_diversity_index}")