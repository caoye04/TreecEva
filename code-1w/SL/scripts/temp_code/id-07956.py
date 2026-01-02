def analyze_text_properties(text_list):
    char_count_map = {}
    total_chars = 0
    unique_char_sets = []

    for text in text_list:
        char_set = set(text.lower())
        char_count_map[text] = len(text)
        total_chars += len(text)
        unique_char_sets.append(char_set)

    intersection_of_all = set.intersection(*unique_char_sets) if unique_char_sets else set()
    
    # Irrelevant statistical distraction
    avg_length = total_chars / len(text_list) if text_list else 0
    variance_tracker = 0
    for text in text_list:
        deviation = len(text) - avg_length
        variance_tracker += deviation * deviation  # Not used later

    return char_count_map, intersection_of_all, avg_length


def transform_counts(raw_counts, modifier):
    adjusted = {}
    temp_buffer = []
    for k, v in raw_counts.items():
        new_val = v * modifier + 2
        adjusted[k] = new_val if new_val % 2 == 0 else new_val + 1
        temp_buffer.append(new_val)  # Dead storage
    
    # Extra loop with no impact
    cumulative = 0
    for val in temp_buffer:
        cumulative += val  # Unused
        if cumulative > 1000:  # Unreachable due to input size
            break
            
    return adjusted


def calculate_final_score(counts):
    score = 0
    bonus_factor = 3
    
    # Key logic: sum even values, apply bonus for long keys
    for text, val in counts.items():
        if val % 2 == 0:
            score += val
            if len(text) > 10:
                score += bonus_factor
    
    # Distractor computation
    squared_sum = sum(v**2 for v in counts.values())
    normalized = squared_sum / (score + 1) if score != -1 else 0  # Not returned
    
    return score

# Main execution
input_texts = ['algorithm', 'function', 'computation', 'logic']

char_counts, common_chars, mean_len = analyze_text_properties(input_texts)

# Intermediate transformation with side noise
adjusted_counts = transform_counts(char_counts, modifier=4)

# Introduce irrelevant zip usage
index_names = list(enumerate([t[:5] for t in input_texts]))
paired_data = list(zip(index_names, adjusted_counts.keys()))

# Add unused set operation
all_keys_set = set(adjusted_counts.keys())
disjoint_check = all_keys_set.isdisjoint(set(['dummy', 'entry']))  # Always True, not used

# Critical statement
final_score = calculate_final_score(adjusted_counts)

print(f"Result: {final_score}")