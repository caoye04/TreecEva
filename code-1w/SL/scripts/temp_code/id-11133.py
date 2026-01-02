def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    # Distractor: counting vowels (not used later)
    vowel_count = sum(1 for c in input_str if c.lower() in 'aeiou')
    
    # Distractor: reverse frequency map (irrelevant)
    reversed_chars = {v: k for k, v in char_frequency.items()}

    # Relevant: get max frequency
    max_freq = max(char_frequency.values()) if char_frequency else 0
    
    # Semi-relevant: normalize frequencies
    total_chars = len(input_str)
    normalized = {k: v / total_chars for k, v in char_frequency.items()} if total_chars else {}
    
    # Distractor: unused transformation
    shifted_values = [round(v * 100 + 5) for v in normalized.values()]
    
    return max_freq, normalized


def compute_baseline_adjustment(n):
    adjustment = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            adjustment += i ** 0.5
        else:
            adjustment -= i // 3
    # This function is partially relevant but only adjustment[-1] type logic is indirectly used
    return abs(int(adjustment))

# Main execution
text_sample = "abracadabra-magic-sequence"

# Step 1: Extract character analysis
max_occurrence, freq_map = analyze_text_patterns(text_sample)

# Step 2: Compute baseline shift (distractor with partial relevance)
shift_factor = compute_baseline_adjustment(len(text_sample))

# Step 3: Generate auxiliary metrics using list comprehension (semi-relevant)
auxiliary_scores = [int(f * 100) for f in freq_map.values() if f > 0.05]

# Step 4: Create composite metric data (key step)
metric_data = {
    'peak': max_occurrence,
    'length': len(text_sample),
    'score_list': auxiliary_scores,
    'offset': shift_factor
}

# Step 5: Define threshold based on conditional logic (with red herring)
base_threshold = len(text_sample) // 2
if 'z' in text_sample:
    base_threshold += 10
elif 'a' in text_sample and max_occurrence > 3:
    base_threshold += 3  # This branch triggers
else:
    base_threshold -= 1

# Step 6: Evaluate performance - key statement
final_score = 0
def evaluate_performance(data, threshold):
    global final_score
    raw_total = sum(data['score_list'])
    
    # Logical operation chain
    is_significant = data['peak'] >= threshold or raw_total > 150
    has_complexity = len(data['score_list']) > 4 and data['offset'] % 2 == 1
    
    # Short-circuit evaluation pattern
    bonus = 10 if is_significant and (has_complexity or data['length'] < 30) else 0
    
    # Composite calculation
    temp_result = (raw_total + data['peak'] * 2 + bonus)
    
    # Final computation
    final_score = temp_result - data['offset']
    
    return final_score

# Execute key statement
evaluate_performance(metric_data, base_threshold)

print(f"Target result: {final_score}")