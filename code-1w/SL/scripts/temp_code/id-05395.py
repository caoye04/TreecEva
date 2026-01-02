def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    reversed_seq = sequence[::-1]
    is_palindrome = sequence.lower() == reversed_seq.lower()
    char_set = set(sequence.lower())
    unique_chars = len(char_set)
    
    # Distractor: irrelevant string analysis
    uppercase_ratio = len([c for c in sequence if c.isupper()]) / len(sequence) if sequence else 0
    
    return count_vowels, is_palindrome, unique_chars


def validate_entry(record):
    if not record.get('active'):
        return False
    if 'error' in record.get('flags', []):
        return False
    return True


def calculate_final_score(data, threshold):
    total_weight = 0.0
    bonus_counter = 0
    penalty = 0

    valid_records = [r for r in data if validate_entry(r)]
    
    # Misleading computation: this list isn't used later
    processed_names = [r['name'].strip().upper() for r in valid_records if 'name' in r]
    name_lengths = [len(name) for name in processed_names]
    
    temp_state = []
    for record in valid_records:
        raw_value = record.get('value', 0)
        
        # Real logic begins
        if raw_value > threshold:
            weight = raw_value * 1.2
            if raw_value % 2 == 0:
                bonus_counter += 1
        else:
            weight = raw_value * 0.85
            if raw_value < 0:
                penalty += 5

        # Additional condition with string method
        name = record.get('name', '')
        if name.endswith('son') and len(name) > 5:
            weight *= 1.1
        
        temp_state.append(weight)
    
    # Core calculation
    base_sum = sum(temp_state)
    adjustment = bonus_counter * 3.5 - penalty
    final_score = int(base_sum + adjustment)
    
    # Dead code path (distractor)
    if len(temp_state) > 100:
        fallback = ''.join(set(processed_names))
        final_score -= len(fallback)
    
    return final_score

# Main execution
raw_data = [
    {'name': 'Jackson', 'value': 40, 'active': True, 'flags': []},
    {'name': 'Miller', 'value': 30, 'active': True, 'flags': ['warning']},
    {'name': 'Peterson', 'value': 50, 'active': True, 'flags': []},
    {'name': 'Lee', 'value': -5, 'active': True, 'flags': []},
    {'name': 'Simmons', 'value': 60, 'active': False, 'flags': ['error']},  # invalid
    {'name': 'Watson', 'value': 45, 'active': True, 'flags': []}
]

threshold = 35
final_score = calculate_final_score(raw_data, threshold)
print(f"Result: {final_score}")