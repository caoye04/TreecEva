def process_entries(entries):
    processed = []
    temp_sum = 0
    
    for entry in entries:
        name = entry['name'].strip().lower()
        raw_value = entry['value']
        adjusted = raw_value * 0.9 if raw_value > 50 else raw_value * 1.1
        
        # Distractor: tracking sum that isn't used later
        temp_sum += adjusted
        
        if 'type' in entry:
            category = entry['type'].upper()
        else:
            category = 'UNKNOWN'
            
        processed.append({
            'id': len(processed) + 1,
            'score': adjusted,
            'group': category
        })
    
    return processed


def filter_and_rank(items):
    # Irrelevant filtering logic (never called)
    valid_items = [i for i in items if i['score'] > 10]
    sorted_items = sorted(valid_items, key=lambda x: x['score'], reverse=True)
    return sorted_items


def calculate_final_score(dataset):
    results = []
    total_weight = 0.0
    cumulative = 0.0
    
    # Misleading normalization factor
    max_possible = max(d['value'] for d in dataset) * 0.9
    
    for record in dataset:
        value = record['value']
        multiplier = 1
        
        # Conditional adjustments based on name length (actual logic path)
        name_len = len(record['name'])
        if name_len % 2 == 0:
            multiplier += 0.1
        else:
            multiplier -= 0.05
        
        # Secondary adjustment based on dictionary presence
        extra_factor = 1.05 if 'type' in record else 0.95
        
        # Dead computation: this list isn't used
        _ = [x * 2 for x in range(name_len) if x % 3 == 0]
        
        weighted_val = value * multiplier * extra_factor
        cumulative += weighted_val
        total_weight += 1
    
    average_weighted = cumulative / total_weight if total_weight else 0
    
    # Final transformation using case conversion as side operation
    tag = ''.join([record['name'][0] for record in dataset]).upper()
    bonus = len(tag) * 0.5
    
    final_score = int(average_weighted + bonus)
    return final_score

# Main execution
raw_data = [
    {'name': 'Alice', 'value': 80, 'type': 'A'},
    {'name': 'Bob', 'value': 45},
    {'name': 'Charlie', 'value': 60, 'type': 'B'},
    {'name': 'Dana', 'value': 70}
]

interim = process_entries(raw_data)
# Unused variable simulating state tracking
status_log = [{'step': 'processed', 'count': len(interim)}]

final_score = calculate_final_score(raw_data)
print(f"Result: {final_score}")