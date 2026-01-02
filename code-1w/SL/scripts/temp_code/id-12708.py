def analyze_entry(entry, min_len=3, factor=1.5):
    if not entry['active']:
        return 0
    
    name = entry['name'].strip().lower()
    length = len(name)
    
    # Irrelevant transformation (distractor)
    reversed_name = name[::-1]
    capitalized = name.title() if length > 4 else name
    
    if length < min_len:
        return 0

    # Semi-relevant scoring
    base_score = length * factor
    bonus = 10 if 'x' in name or 'z' in name else 0
    
    # Dead code path (distractor)
    temp_value = None
    if False:
        temp_value = [char for char in name if char in 'aeiou']
        temp_value = ''.join(temp_value)

    return int(base_score) + bonus


def calculate_final_score(data, thresholds):
    total = 0
    max_name_length = 0
    count_valid = 0
    
    # Track unused stats (distractors)
    all_lengths = []
    special_entries = 0

    for item in data:
        item_status = item['active']
        item_name = item['name']
        
        # Unused computation (distractor)
        normalized_name = item_name.strip().replace(' ', '_').lower()
        if 'test' in normalized_name:
            special_entries += 1

        current_length = len(item_name.strip())
        all_lengths.append(current_length)
        
        if current_length > max_name_length:
            max_name_length = current_length

        score = analyze_entry(item)
        
        # Conditional expression (required Python feature)
        adjustment = 5 if score > thresholds['high'] else (-3 if score < thresholds['low'] else 0)
        
        total += score + adjustment
        count_valid += 1
        
        # Early exit that may or may not trigger (logic red herring)
        if total > thresholds['ceiling']:
            total -= adjustment  # Compensate to avoid skewing
            break

    # Linear search for threshold category (suggested paradigm)
    category = 'unknown'
    for key, limit in [('low', 10), ('medium', 20), ('high', 30)]:
        if max_name_length <= limit:
            category = key
            break

    # Final aggregation with irrelevant string method use (required feature)
    suffix = f"_{category.upper()}".ljust(5, 'X')
    label = "RESULT" + suffix.rstrip('X')

    # Final score calculation — only this matters
    scaling_factor = 1.2 if count_valid > 3 else 1.0
    final_score = int(total * scaling_factor)

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
entries = [
    {'name': 'Alex', 'active': True},
    {'name': 'Bob', 'active': False},
    {'name': 'Jinx', 'active': True},
    {'name': 'Zoe', 'active': True},
    {'name': 'Maxwell', 'active': True},
    {'name': 'Una', 'active': True}
]

thresholds_config = {
    'low': 8,
    'high': 15,
    'ceiling': 50
}

# Key execution point
final_score = calculate_final_score(entries, thresholds_config)