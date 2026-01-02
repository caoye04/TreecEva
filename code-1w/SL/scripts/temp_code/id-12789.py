def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    for entry in raw_entries:
        if not entry.get('active', True):
            continue
        name = entry['name'].strip().lower()
        if 'test' in name or 'demo' in name:
            validation_flag = False
            temp_sum += len(name)  # irrelevant accumulation
        else:
            validation_flag = True
        
        score = entry.get('score', 0)
        if score < 0:
            score = abs(score) % 100
        category = entry.get('category', 'unknown')
        
        # Misleading normalization step
        normalized_score = (score * 1.1) if category == 'premium' else (score * 0.9)
        capped_score = min(normalized_score, 95)
        
        cleaned.append({
            'id': entry['id'],
            'adjusted_score': round(capped_score),
            'valid': validation_flag
        })
    return cleaned, temp_sum  # temp_sum is unused later


def filter_and_rank(data_list):
    valid_items = [item for item in data_list if item['valid']]
    sorted_items = sorted(valid_items, key=lambda x: x['adjusted_score'], reverse=True)
    top_five = sorted_items[:5]
    
    # Dead computation: transforming into dict format that's not used
    id_mapping = {item['id']: idx for idx, item in enumerate(top_five)}
    total_indices = sum(id_mapping.values())  # unused
    
    return top_five

def calculate_final_score(rank_slice):
    base = sum(item['adjusted_score'] for item in rank_slice)
    multiplier = len(rank_slice) if base > 300 else 1.5
    penalty = 0
    
    # Simulate conditional adjustment (not triggered in this data)
    for item in rank_slice:
        if item['id'] < 10:
            penalty += 5
    
    result = (base * multiplier) - penalty
    return int(result)

# Main execution
raw_data = [
    {'id': 12, 'name': ' Alice ', 'score': 88, 'category': 'premium', 'active': True},
    {'id': 15, 'name': 'Bob', 'score': 92, 'category': 'standard', 'active': True},
    {'id': 8, 'name': 'test_user', 'score': 75, 'category': 'standard', 'active': True},
    {'id': 21, 'name': 'Charlie', 'score': 85, 'category': 'premium', 'active': True},
    {'id': 22, 'name': 'Diana', 'score': 90, 'category': 'standard', 'active': True},
    {'id': 14, 'name': 'Eve', 'score': 87, 'category': 'premium', 'active': True},
    {'id': 9, 'name': 'demo_temp', 'score': 95, 'category': 'standard', 'active': True},
    {'id': 18, 'name': 'Frank', 'score': 83, 'category': 'standard', 'active': False}  # inactive
]

processed_data, _ = preprocess_records(raw_data)
filtered_top = filter_and_rank(processed_data)
final_score = calculate_final_score(filtered_top)
print(f"Target result: {final_score}")