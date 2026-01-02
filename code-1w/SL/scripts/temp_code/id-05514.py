def analyze_text_patterns(text_block, pattern):
    count = 0
    positions = []
    for i in range(len(text_block) - len(pattern) + 1):
        if text_block[i:i+len(pattern)] == pattern:
            count += 1
            positions.append(i)
    return count, positions


def normalize_values(raw_list):
    if not raw_list:
        return []
    max_val = max(raw_list)
    return [x / max_val for x in raw_list] if max_val != 0 else [0] * len(raw_list)


def evaluate_performance(metrics, threshold):
    adjusted = 0
    penalty = 0
    
    # Irrelevant preprocessing (distractor)
    temp_metrics = [x for x in metrics if x >= 0]
    normalized = normalize_values(temp_metrics)
    
    # Key logic begins
    high_count = 0
    for val in metrics:
        if val > threshold * 1.5:
            adjusted += val * 0.8
            high_count += 1
        elif val > threshold:
            adjusted += val * 0.5
        else:
            penalty += 10
    
    # Distractor: unused complex calculation
    combinatorial_weight = 1
    for i in range(1, min(high_count + 1, 4)):
        combinatorial_weight *= i  # 3! max
    
    # Another red herring: string analysis with no impact
    status_msg = "ANALYSIS_COMPLETE"
    flag_chars = [c for c in status_msg if c in 'AEIOU']
    vowel_count = len(flag_chars)
    
    # Final score depends only on adjusted and penalty
    final_score = int(adjusted - penalty)
    
    # Early return not taken (dead path)
    if vowel_count > 10:
        return -1
        
    return final_score

# Main execution
raw_data = [20, -5, 30, 15, 25, 40, 10]
base_threshold = 20

# Distractor: text analysis unrelated to final result
text_block = "AAABBBCCCDDDEEEFFFGGGHHHIII"
pattern = "III"
match_count, indices = analyze_text_patterns(text_block, pattern)

# Additional irrelevant state tracking
state_log = []
for idx, val in enumerate(raw_data):
    if val % 5 == 0 and val > 0:
        state_log.append(f"Valid entry at {idx}")

metric_data = [x for x in raw_data if x >= 10]  # Filtered data

final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")