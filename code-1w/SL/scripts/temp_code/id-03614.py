def analyze_conditions(x, y):
    if x < 0:
        return False
    temp_result = (x ** 2 + y) % 5 == 0
    offset_check = (x + 2) % 3
    return temp_result and offset_check != 1

def build_lookup(keys):
    lookup = {}
    for k in keys:
        lookup[k] = (k * 3) + 1
    # Irrelevant computation (distractor)
    redundant_sum = sum(lookup.values()) * 0.1
    return lookup

def filter_and_transform(values):
    filtered = [v for v in values if v % 2 == 1]
    transformed = [t ** 2 for t in filtered]
    # Dead code path (distractor)
    if len(transformed) > 100:
        transformed = transformed[:50]
    return transformed

def calculate_final_score(raw_data):
    # Step 1: Preprocess data
    processed = [item * 2 - 1 for item in raw_data]
    
    # Step 2: Build dictionary mapping (relevant)
    indices = [i for i in range(len(processed)) if processed[i] > 0]
    map_table = build_lookup(indices)
    
    # Step 3: Apply conditional filtering
    valid_entries = []
    for idx, val in enumerate(processed):
        if analyze_conditions(val, idx):
            valid_entries.append(val)
    
    # Step 4: Transform valid entries
    squared_vals = filter_and_transform(valid_entries)
    
    # Step 5: Compute aggregate metrics
    total = sum(squared_vals)
    count = len(squared_vals)
    average = total / count if count > 0 else 0
    
    # Step 6: Weighted contribution from map_table (only keys < 5 matter)
    bonus = 0
    for k in map_table:
        if k < 5:
            bonus += map_table[k] // 4
    
    # Step 7: Final score calculation
    final_score = int(average + bonus)
    
    # Red herring variables (not used)
    phantom_metric = max(squared_vals) * 0.5 if squared_vals else 0
    shadow_accum = sum([i**3 for i in range(count)]) * 0.01
    
    return final_score

# Main execution
data = [3, -1, 4, 1, 5, 9, 2, 6]
final_score = calculate_final_score(data)
print(f"Target result: {final_score}")