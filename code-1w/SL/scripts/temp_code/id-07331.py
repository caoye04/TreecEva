def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

# Irrelevant helper function (distractor)
def reverse_string(s):
    return s[::-1]

# Another distractor: unused statistical computation
def entropy(values):
    from math import log
    total = sum(values)
    return -sum((v / total) * log(v / total) for v in values if v > 0)

# Main processing pipeline
def preprocess_entries(raw_entries):
    cleaned = []
    for entry in raw_entries:
        stripped = entry.strip().lower()
        if len(stripped) > 3:
            cleaned.append(stripped)
    return cleaned

# Core logic function
def calculate_final_score(log_data, adj):
    base_points = 0
    vowel_count = 0
    vowels = 'aeiou'
    
    # Character analysis with dictionary tracking
    char_stats = analyze_frequency(''.join(log_data))
    
    # Relevant accumulation
    for word in log_data:
        for ch in word:
            if ch in vowels:
                vowel_count += 1
    
    # Distractor variables (not used in final result)
    max_freq = max(char_stats.values()) if char_stats else 0
    rare_chars = [ch for ch, cnt in char_stats.items() if cnt == 1]
    entropy_estimate = 0.0
    if char_stats:
        counts = list(char_stats.values())
        total_counts = sum(counts)
        entropy_estimate = -sum((c / total_counts) * (c / total_counts).__log__ for c in counts if c > 0)
    
    # Actual score calculation
    word_length_bonus = sum(len(w) for w in log_data)
    base_points += word_length_bonus * 2
    base_points += vowel_count * 5
    
    # Adjustment using parameter
    adjusted = base_points * adj
    
    # Final nonlinear transformation
    final_score = int((adjusted + 10) ** 1.5) % 98765
    
    # Dead code path (never executed due to condition)
    if False and len(rare_chars) > 10:
        extra_penalty = len(rare_chars) * 3
        final_score -= extra_penalty
    
    return final_score

# Setup data
raw_input = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
data_log = preprocess_entries(raw_input)
adjustment_factor = 1.2

# Execute key statement
temp_result = sum(len(entry) for entry in data_log)  # red herring computation
final_score = calculate_final_score(data_log, adjustment_factor)
print(f"Target result: {final_score}")