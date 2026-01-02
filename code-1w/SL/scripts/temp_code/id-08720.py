def analyze_pattern(data):
    char_freq = {}
    for i, char in enumerate(data):
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    
    # Filter letters appearing more than once
    repeated = {k: v for k, v in char_freq.items() if v > 1}
    
    # Compute weighted score using lambda
    score_fn = lambda freq: sum(f**2 for f in freq.values())
    return score_fn(repeated)

# Irrelevant auxiliary variable (minimal distraction)
placeholder_value = "N/A"

text_data = "Programming in Python enables powerful abstractions."
result = analyze_pattern(text_data)
print(f"Target result: {result}")