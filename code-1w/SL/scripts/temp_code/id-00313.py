def analyze_pattern(sequence):
    count_vowels = lambda s: sum(1 for c in s if c.lower() in 'aeiou')
    reversed_chunks = [seq[::-1] for seq in sequence]
    lengths = [len(chunk) for chunk in reversed_chunks]
    total_length = sum(lengths)
    avg_length = total_length / len(lengths) if lengths else 0
    
    # Irrelevant distraction: vowel counting in labels
    labels = ['alpha', 'beta', 'gamma', 'delta']
    vowel_count = sum(count_vowels(label) for label in labels)

    # Distractor: unused transformation
    encoded = [chunk.upper() + 'X' for chunk in sequence if len(chunk) > 3]
    
    return avg_length, vowel_count  # vowel_count is irrelevant


def validate_entry(record):
    if not record.get('active'):
        return False
    
    status_code = record.get('status')
    valid_codes = [200, 201, 202]
    
    # Bitwise distraction
    flag_check = (status_code & 1) == 1 and (status_code | 4) > 5
    
    name = record.get('name', '')
    has_upper = any(c.isupper() for c in name)
    
    # Real condition
    is_valid = status_code in valid_codes and has_upper
    
    # Dead code path
    if len(name) > 10:
        temp_flag = name.startswith('A')
        _ = temp_flag  # unused
    
    return is_valid


def compute_hash(key_string):
    # Simple hash for distraction
    h = 0
    for c in key_string:
        h = (h * 31 + ord(c)) % 10007
    return h


def process_metrics(data, config):
    # Main relevant logic starts here
    filtered_data = [x for x in data if x > config['min_val']]
    
    # Conditional expression distraction
    adjustment = 1.5 if len(filtered_data) > 3 else 0.8
    
    # Real computation chain
    squared = [x ** 2 for x in filtered_data]
    shifted = [x >> 1 for x in squared]  # Bitwise shift as red herring
    summed = sum(shifted)
    
    # String distraction
    tag = "metric_summary_" + "_".join([str(len(filtered_data)), str(summed % 10)])
    tag_parts = tag.split('_')
    numeric_tags = [int(p) for p in tag_parts if p.isdigit()]
    
    # Core logic: use only one part
    base_score = summed // 10
    
    # Multiple distractors below
    checksum = compute_hash(tag)
    pattern_info = analyze_pattern([bin(checksum)[2:]])
    
    # More noise
    entries = [
        {'name': 'Alice', 'status': 200, 'active': True},
        {'name': 'bob', 'status': 404, 'active': True},
        {'name': 'Eve', 'status': 201, 'active': False}
    ]
    valid_entries = [e for e in entries if validate_entry(e)]
    entry_names = [e['name'] for e in valid_entries]
    
    # Final score depends only on base_score and adjustment
    final_score = base_score + int(adjustment * 10)  # adjustment used as integer
    
    # Unused but plausible-looking aggregation
    if entry_names:
        first_chars = [name[0] for name in entry_names]
        char_freq = {c: first_chars.count(c) for c in set(first_chars)}
        _ = sum(char_freq.values())  # dead computation

    return final_score

# Setup inputs
raw_data = [2, 5, 3, 7, 1, 9, 4]
thresholds = {'min_val': 2}

# Execution point of interest
data = [x + 1 for x in raw_data]  # transform before processing
final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")