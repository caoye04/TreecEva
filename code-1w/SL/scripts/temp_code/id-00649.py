def preprocess_entry(entry):
    # Irrelevant transformation
    normalized = entry['value'].strip().lower()
    code_sum = sum(ord(c) for c in normalized)
    return code_sum % 17


def validate_format(text):
    # Distractor: checks format but not used in final logic
    if len(text) < 3:
        return False
    return text.isalpha() and text[0].isupper()


def analyze_trend(values):
    # Semi-relevant: computes trend but only sign matters
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    positive_changes = sum(1 for d in diffs if d > 0)
    negative_changes = sum(1 for d in diffs if d < 0)
    return positive_changes >= negative_changes


def calculate_final_score(data):
    base_accumulator = 0
    adjustment_factor = 0
    temp_flags = []
    
    for item in data:
        # Extract meaningful numeric contribution
        raw_value = item['score']
        tag_length = len(item['tag'])
        
        # Real logic starts here
        processed_key = preprocess_entry(item)
        base_accumulator += raw_value * (tag_length % 4)
        
        # Dead code path — never triggered in this input
        if item['tag'].startswith('X'):
            adjustment_factor += 100
        elif item['tag'].startswith('Z'):
            adjustment_factor -= 50
        
        # Tracking state that isn't fully used
        validation_status = validate_format(item['tag'])
        temp_flags.append(validation_status)
        
    # Actual key computation
    trend_data = [d['score'] for d in data]
    increasing_trend = analyze_trend(trend_data)
    
    # Final score depends on base_accumulator and trend only
    if increasing_trend:
        final_modifier = 3
    else:
        final_modifier = -2
    
    # Key assignment point
    final_score = (base_accumulator // len(data)) * final_modifier
    
    # Unused cleanup
    cleanup_ref = None
    del cleanup_ref
    
    return final_score

# Input data
entries = [
    {'score': 12, 'value': ' Alpha ', 'tag': 'High'},
    {'score': 15, 'value': ' Beta  ', 'tag': 'Medium'},
    {'score': 18, 'value': ' Gamma ', 'tag': 'Low'},
    {'score': 21, 'value': ' Delta ', 'tag': 'Urgent'}
]

result = calculate_final_score(entries)
print(f"Result: {result}")