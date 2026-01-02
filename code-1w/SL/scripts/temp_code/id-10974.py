def process_entries(entries):
    # Irrelevant transformation (distractor)
    temp_result = [e.upper() for e in entries if len(e) > 2]
    filtered = [e for e in entries if e.startswith('a')]
    return filtered

# Lambda for case conversion and scoring
score_fn = lambda x: len(x) * (1.5 if x.islower() else 0.5)

# Auxiliary function with misleading intermediate steps
def analyze_patterns(seq):
    pattern_count = 0
    total_length = sum(len(s) for s in seq)
    avg_len = total_length / len(seq) if seq else 0
    
    # Dead computation branch (adds interference)
    if avg_len > 10:
        pattern_count += 5
    else:
        temp_buffer = [s[::-1] for s in seq]  # Unused
        
    # Actual relevant logic
    valid_items = [s for s in seq if s.isalpha() and 'x' not in s]
    return len(valid_items), avg_len

# Main calculation with nested logic
def calculate_final_score(data_map):
    keys = data_map.keys()
    values = data_map.values()
    
    # Distractor: unused aggregation
    total_chars = sum(len(str(v)) for v in values)
    
    # Extract string values for processing
    string_vals = [v for v in values if isinstance(v, str)]
    processed = process_entries(string_vals)
    
    # Intermediate score with semi-relevant transformation
    intermediate_scores = [score_fn(s) for s in processed]
    base_score = sum(intermediate_scores)
    
    # Additional logic path that seems important but only partially used
    count, average = analyze_patterns(string_vals)
    adjustment = count * 2.5
    
    # Key logic step: apply conditional bonus
    bonus = 0
    if base_score > 10 and average > 3.0:
        bonus = 17.5
    
    # Final computation
    final_score = base_score + adjustment + bonus
    
    # Print required result
    print(f"Result: {final_score}")
    return final_score

# Input data with mixed types (realistic)
data_map = {
    'item_a': 'apple',
    'item_b': 'banana',
    'item_c': 'axolotl',
    'item_d': 123,
    'item_e': 'alpine',
    'item_f': 'zebra',
    'item_g': 'amazing'
}

# Execution point of interest
final_score = calculate_final_score(data_map)