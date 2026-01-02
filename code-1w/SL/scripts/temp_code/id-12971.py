from collections import defaultdict, Counter

def analyze_text_patterns(text_blocks):
    char_freq = defaultdict(int)
    word_lengths = []
    total_chars = 0
    temp_sum = 0  # distractor variable

    for block in text_blocks:
        cleaned = block.strip().lower()
        words = cleaned.split()
        
        # Irrelevant computation (distractor)
        for _ in range(2):
            temp_sum += len(cleaned) % 3
        
        for word in words:
            word_lengths.append(len(word))
            for char in word:
                if char.isalpha():
                    char_freq[char] += 1
                    total_chars += 1
    
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    return char_freq, avg_length, total_chars

def transform_keys(data_dict):
    new_dict = {}
    for k, v in data_dict.items():
        new_key = ''.join(sorted(k))
        new_dict[new_key] = v * 2  # transformation
    return new_dict

def calculate_final_score(data):
    score = 0
    length_bonus = 0
    
    # Real logic
    for key, value in data.items():
        if len(key) % 2 == 0:
            score += value
        else:
            score -= value
        
        # Distractor: complex but unused calculation
        subset = [c for c in key if c in 'aeiou']
        vowel_count = len(subset)
        length_bonus += vowel_count ** 2
    
    final_penalty = 0
    for i, c in enumerate(data.keys()):
        final_penalty += (i + 1) * (ord(c[0]) % 5)  # misleading complexity
    
    # Actual answer only depends on score
    return score

# Main execution
raw_texts = [
    "Dynamic Programming Solutions",
    "Graph Traversal Methods",
    "String Manipulation Tools"
]

frequencies, average_len, total = analyze_text_patterns(raw_texts)

# Build frequency signature
signature = ''.join([char for char, _ in Counter(frequencies).most_common(5)])

# Create data profile (this is the actual input to scoring)
data_profile = {
    'ac': 12,
    'eh': 8,
    'il': 15,
    'no': 7
}

# Distractor: unused transformation
transformed = transform_keys(data_profile)

# Key assignment that determines the answer
current_state = {k: v for k, v in data_profile.items() if v > 8}
processed_data = transform_keys(current_state)  # keys sorted, values doubled

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")