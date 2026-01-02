def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    # Distractor: vowel counting (not used later)
    vowels = 'aeiou'
    vowel_count = sum(char_frequency.get(v, 0) for v in vowels)
    
    # Relevant transformation: normalize frequencies
    total_letters = sum(char_frequency.values())
    normalized = {k: v / total_letters for k, v in char_frequency.items()}

    # Distractor: entropy-like computation (not actually used)
    import math
    entropy = -sum(p * math.log2(p) for p in normalized.values() if p > 0)

    return normalized


def filter_and_weight(freq_dict, threshold=0.05):
    # Filter rare characters and apply arbitrary weightings
    weights = {}
    for k, v in freq_dict.items():
        if v >= threshold:
            if k in 'stne':
                weights[k] = v * 1.8
            elif k in 'abc':
                weights[k] = v * 1.2
            else:
                weights[k] = v * 0.9
    return weights


def calculate_complexity_score(weights_dict):
    base = sum(weights_dict.values())
    penalty = 0
    for char, weight in weights_dict.items():
        if weight < 0.1:
            penalty += 0.05
    return base - penalty


def calculate_final_score(data):
    score = 0
    for key in data:
        if key in 'rstl':
            score += data[key] * 2.1
        elif key in 'eino':
            score += data[key] * 1.7
        else:
            score += data[key] * 0.8
    return int(score * 100)  # Discretize final score

# Main execution
raw_input = "The quick brown fox jumps over the lazy dog repeatedly every morning!"

# Step 1: Clean and extract relevant content
cleaned = ''.join([c for c in raw_input if c.isalnum() or c.isspace()])
words = cleaned.split()
long_words = [w for w in words if len(w) > 4]

# Distractor: word length stats (not directly used)
avg_word_length = sum(len(w) for w in words) / len(words)
word_length_variance = sum((len(w) - avg_word_length)**2 for w in words) / len(words)

# Step 2: Process character patterns
freq_map = analyze_text_patterns(raw_input)

# Step 3: Filter and weight important characters
filtered_weights = filter_and_weight(freq_map, threshold=0.045)

# Step 4: Calculate intermediate complexity metric (semi-relevant)
complexity_metric = calculate_complexity_score(filtered_weights)

# Step 5: Final scoring based on refined weights
final_score = calculate_final_score(filtered_weights)

print(f"Result: {final_score}")