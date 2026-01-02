def preprocess_entries(entry_list):
    processed = []
    temp_sum = 0
    for entry in entry_list:
        if len(entry) < 3:
            continue
        cleaned = entry.strip().lower()
        if 'error' in cleaned:
            break
        capitalized = cleaned.capitalize()  # Distractor: unused
        temp_sum += len(cleaned)
        processed.append(cleaned)
    average_length = temp_sum / len(processed) if processed else 0
    return processed, average_length


def validate_sequence(seq):
    valid_count = 0
    for item in seq:
        if item.isalpha() and len(item) == 1:
            valid_count += 1
    return valid_count == len(seq)  # Distractor: only partially relevant


def transform_key(k):
    return k[::-1].upper()


def calculate_final_score(data_map):
    score = 0
    bonus = 10
    penalty = 5
    intermediate_results = {}
    
    keys = list(data_map.keys())
    sorted_keys = sorted(keys, key=lambda x: len(transform_key(x)))
    
    for key in sorted_keys:
        value = data_map[key]
        
        # String manipulation and case conversion
        transformed = transform_key(key)
        if transformed.startswith('A'):
            score += value * 2
        elif len(transformed) % 2 == 0:
            score += value + 3
        else:
            score -= penalty  # Red herring: rarely triggered
        
        # Dictionary-based frequency tracking (semi-relevant)
        first_char = transformed[0]
        if first_char not in intermediate_results:
            intermediate_results[first_char] = 0
        intermediate_results[first_char] += 1
    
    # Additional logic that influences final score
    char_count = sum(intermediate_results.values())
    if char_count > 5:
        score += bonus
    
    # Dead computation: does not affect result
    max_key_length = max((len(k) for k in data_map.keys()), default=0)
    padding = max_key_length * 0.5  # Unused float
    
    return int(score)

# Main execution
raw_entries = ["Test1", "DataPoint", "Invalid", "Entry"]
processed_data, avg_len = preprocess_entries(raw_entries)

sequence_check = ["a", "b", "c"]
valid_seq = validate_sequence(sequence_check)

# Build input map with meaningful names
config_params = {
    "xero": 7,
    "beta": 12,
    "gamma": 5,
    "delta": 8,
    "omega": 4
}

final_score = calculate_final_score(config_params)
print(f"Target result: {final_score}")