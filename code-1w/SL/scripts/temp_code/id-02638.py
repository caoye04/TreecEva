def analyze_text_patterns(text_data):
    char_count = len(text_data)
    vowel_count = sum(1 for c in text_data.lower() if c in 'aeiou')
    upper_count = sum(1 for c in text_data if c.isupper())
    word_list = text_data.split()
    avg_word_length = sum(len(word) for word in word_list) / len(word_list) if word_list else 0
    
    # Distractor: irrelevant statistical computation
    entropy_approx = 0
    freq_map = {}
    for c in text_data:
        freq_map[c] = freq_map.get(c, 0) + 1
    for count in freq_map.values():
        if count > 0:
            entropy_approx -= (count / char_count) * (count / char_count)

    # Semi-relevant transformation
    normalized_vowels = vowel_count / char_count if char_count else 0
    complexity_score = (upper_count * 1.5) + (len(word_list) * 0.8)

    return normalized_vowels, complexity_score, avg_word_length


def evaluate_consistency(metrics_log):
    if not metrics_log:
        return 0.0
    total = sum(metrics_log)
    deviation_sum = 0
    mean_val = total / len(metrics_log)
    for val in metrics_log:
        deviation_sum += (val - mean_val) ** 2
    variance = deviation_sum / len(metrics_log) if metrics_log else 0
    consistency_score = 1 / (1 + variance)  # Higher stability gives higher score
    
    # Dead code path - misleading but syntactically present
    if False:
        consistency_score = max(consistency_score, 0.5)
        buffer = [0] * 100
        for i in range(len(buffer)-1):
            buffer[i+1] = buffer[i] + 2
    
    return consistency_score

# Main logic chain
raw_input = "The Quick Brown Fox Jumps Over The Lazy Dog 123!"
processed_input = raw_input.strip().replace('123!', '').upper()  # Preprocessing step

# Extract features
norm_vowels, comp_score, avg_len = analyze_text_patterns(processed_input)

# Tracking intermediate states
metric_history = [comp_score]
for i in range(2):
    updated_comp = comp_score * (0.9 + i * 0.05)
    metric_history.append(updated_comp)

# Conditional adjustment based on length property
if avg_len > 4.0:
    comp_score += 5.0
    temp_adjustment = comp_score * 0.1  # unused distraction

# Simulate multi-step evaluation
stability = evaluate_consistency(metric_history)
base_rating = norm_vowels * 100 + avg_len * 10

# Final performance rating with distractor variables
bonus_factor = len(processed_input.split()) // 4
decay_factor = 0.95 ** len(metric_history)
dummy_tracker = {'stage1': base_rating, 'stage2': comp_score}

final_score = base_rating + comp_score * stability - 20
final_score = int(final_score)  # Discrete output

print(f"Result: {final_score}")