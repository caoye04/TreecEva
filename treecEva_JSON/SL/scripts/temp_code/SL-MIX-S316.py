from functools import reduce

def transform_char_frequency(char, freq):
    return freq * (ord(char) % 10 + 1)

def compute_readability(document):
    char_freq = {}
    for char in document:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Apply transformation and sum using functional programming
    transformed_values = [transform_char_frequency(char, freq) for char, freq in char_freq.items()]
    return reduce(lambda x, y: x + y, transformed_values, 0)

# Process the document
research_paper_abstract = "Dynamic programming solves complex problems by breaking them into simpler subproblems."
readability_score = compute_readability(research_paper_abstract)

print(f"Result: {readability_score}")