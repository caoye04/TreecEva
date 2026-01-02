def process_metrics(entries, importance):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant string transformation (distractor)
    labels = [e['name'].upper() for e in entries]
    normalized_labels = [label.replace(' ', '_') for label in labels if len(label) > 3]
    
    # Real computation begins
    for i, entry in enumerate(entries):
        value = entry['value']
        quality = entry['quality_flag']
        weight = importance[i]
        
        # Slice to extract mid-digits (actual use of slicing)
        str_val = str(abs(value))
        mid_part = int(str_val[1:-1]) if len(str_val) > 2 else str_val
        
        # Lambda for dynamic adjustment (lambda function)
        adjust = lambda x, w: x * w + (1 if x % 2 == 0 else -1)
        adjusted = adjust(int(mid_part), weight)
        
        base += adjusted
        
        # Bonus logic with early break (semi-relevant)
        if quality and adjusted > 50:
            bonus += 10
            if bonus > 30:
                break

        # Dead code path (irrelevant)
        if value < 0:
            shadow_factor = abs(value) ** 0.5
            penalty += 0  # No real effect

    # Destructuring assignment (tuple unpacking)
    multiplier, offset = (1.5, -20)
    
    # String-based condition (string method used)
    mode = "aggressive" if 'high' in importance.__str__().lower() else "conservative"
    
    # Final score calculation
    final_score = base * multiplier + offset
    
    # Unused dictionary aggregation (distractor)
    stats = {
        'max_base': max([int(str(abs(e['value']))[1:-1]) if len(str(abs(e['value']))) > 2 else 0 for e in entries]),
        'total_entries': len(entries),
        'bonus_applied': bonus
    }
    
    return final_score

# Input data
data = [
    {'name': 'throughput', 'value': 1428, 'quality_flag': True},
    {'name': 'latency', 'value': 2563, 'quality_flag': True},
    {'name': 'jitter', 'value': 314, 'quality_flag': False},
    {'name': 'bandwidth', 'value': 4829, 'quality_flag': True}
]

weights = [0.8, 1.2, 0.9, 1.5]

# Execution point
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")