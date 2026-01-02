def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1
    
    # Distractor: Count vowels (not used in final result)
    vowels = 'aeiou'
    vowel_count = sum(char_frequency.get(v, 0) for v in vowels)
    
    # Distractor: Reverse frequency mapping
    freq_to_chars = {}
    for ch, freq in char_frequency.items():
        freq_to_chars[freq] = freq_to_chars.get(freq, []) + [ch]
    
    sorted_letters = sorted(char_frequency.keys())
    entropy = 0.0
    total_chars = sum(char_frequency.values())
    for freq in char_frequency.values():
        prob = freq / total_chars
        entropy -= prob * __import__('math').log2(prob) if prob > 0 else 0
    
    return char_frequency, entropy, total_chars


def filter_relevant_metrics(metrics, min_threshold):
    # Semi-relevant transformation
    filtered = {k: v for k, v in metrics.items() if v >= min_threshold}
    squared_values = [v**2 for v in filtered.values()]  # Not used later
    normalized = {k: v / max(filtered.values()) for k in filtered} if filtered else {}
    return normalized


def compute_weighted_ranks(rank_dict):
    weighted_sum = 0
    for idx, (key, val) in enumerate(sorted(rank_dict.items(), key=lambda x: x[1], reverse=True)):
        weighted_sum += val * (idx + 1.5)  # arbitrary weight
    return weighted_sum


def evaluate_performance(data, limit):
    # Misleading variable names and irrelevant branches
    temp_buffer = []
    for item in data:
        temp_buffer.append(str(item).upper())
    
    # Dead code path (never executed due to constant condition)
    debug_mode = False
    if debug_mode and len(temp_buffer) > 100:
        __import__('time').sleep(0.001)

    processed = [x for x in data if isinstance(x, (int, float)) and x > 0]
    if not processed:
        return 0
    
    avg_val = sum(processed) / len(processed)
    above_avg = [x for x in processed if x > avg_val]
    adjustment_factor = len(above_avg) / len(processed)
    
    # Core logic hidden among distractions
    penalty = 0
    for i in range(len(processed)):
        if i % 3 == 0 and processed[i] < limit:
            penalty += 1
    
    base_score = avg_val * adjustment_factor * 100
    final_score = base_score - (penalty * 5)
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Main execution with realistic context: log analysis scoring
raw_log = "Error occurred at node A; retrying... Success at Node B! Final confirmation from NODE C."

freq_map, info_entropy, total_alpha = analyze_text_patterns(raw_log)

# Simulate metric extraction from text statistics
metric_candidates = {
    'entropy': info_entropy,
    'length_score': len(raw_log) / 10,
    'complexity': info_entropy * 10,
    'letter_diversity': len(freq_map),
    'avg_frequency': total_alpha / len(freq_map) if freq_map else 0
}

refined_metrics = filter_relevant_metrics(metric_candidates, 2.0)
sorted_keys = sorted(refined_metrics.keys(), reverse=True)

# Construct final data using multiple steps
staged_data = []
for key in sorted_keys:
    raw_val = metric_candidates[key]
    staged_data.append(raw_val * 2)  # Amplify signal

# Add synthetic entries based on character patterns
if 'node' in raw_log.lower():
    staged_data.append(len(analyze_text_patterns('node')[0]))  # diversity of 'node'

threshold = 4.5
final_score = evaluate_performance(staged_data, threshold)