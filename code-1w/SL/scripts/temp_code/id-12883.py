def analyze_text_quality(text):
    words = text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Distractor: character frequency analysis (not used later)
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    unique_consonants = set('bcdfghjklmnpqrstvwxyz') & set(text.lower())
    consonant_count = len(unique_consonants)

    # Relevant metric: percentage of long words
    long_word_ratio = sum(1 for wl in word_lengths if wl >= 6) / len(words) if words else 0
    
    return {
        'avg_word_length': avg_length,
        'long_word_ratio': long_word_ratio,
        'word_count': len(words)
    }


def normalize_metrics(metrics):
    # Normalize values to 0-1 scale using arbitrary baselines
    normalized = {}
    
    # Simulated normalization factors (some are red herrings)
    max_possible_avg = 15.0
    max_possible_long_ratio = 1.0
    typical_word_count = 50
    
    normalized['norm_avg'] = min(metrics['avg_word_length'] / max_possible_avg, 1.0)
    normalized['norm_long'] = metrics['long_word_ratio'] / max_possible_long_ratio
    
    # Distractor: irrelevant scaling based on word count deviation
    deviation_factor = abs(metrics['word_count'] - typical_word_count) / typical_word_count
    penalty_score = 0.1 * deviation_factor  # Not actually used
    
    # Only first two matter
    return [normalized['norm_avg'], normalized['norm_long']]


def calculate_final_score(norm_vals):
    # Simple weighted sum; only uses first two normalized metrics
    weight_1, weight_2 = 0.6, 0.4
    score = weight_1 * norm_vals[0] + weight_2 * norm_vals[1]
    
    # Dead code branch — never executed but looks relevant
    if False:
        backup_weights = [0.5, 0.5]
        score = (norm_vals[0] * backup_weights[0]) + (norm_vals[1] * backup_weights[1])
    
    return round(score * 100, 2)  # Scale to percentage-like score


# Main execution
raw_input = "The quick brown fox jumps over the lazy dog near the scenic riverbank under golden sunlight."

# Step 1: Analyze text
analysis_result = analyze_text_quality(raw_input)

# Step 2: Normalize the extracted metrics
processed_data = normalize_metrics(analysis_result)

# Step 3: Calculate final composite score
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")