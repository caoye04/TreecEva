def analyze_component(metrics, config):
    base = metrics['base_value']
    threshold = config.get('threshold', 100)
    adjustment = 0
    
    # Irrelevant computation (distractor)
    temp_debug = [x ** 0.5 for x in range(1, 6) if x % 2 == 1]
    debug_sum = sum(temp_debug)

    if base > threshold:
        adjustment += 15
    else:
        adjustment -= 5

    # Semi-relevant transformation
    normalized = (base + adjustment) / (len(metrics.get('history', [])) + 1)
    return int(normalized)


def validate_entry(record):
    # Dummy validation logic with side computations
    checksum = 0
    for k, v in record.items():
        checksum += len(k) + hash(str(v)) % 17
    # This function doesn't affect final result but looks important
    return checksum % 3 == 0


def calculate_performance(data):
    total = 0
    penalties = []
    history_tracker = {}
    
    for key, entry in data.items():
        # Extract relevant fields
        component_a = entry['components']['A']
        component_b = entry['components']['B']
        
        # Configuration mock
        cfg = {'threshold': 80}
        
        # Compute intermediate scores
        score_a = analyze_component(component_a, cfg)
        score_b = analyze_component(component_b, cfg)
        
        # Aggregate logic
        combined = score_a * 0.6 + score_b * 0.4
        
        # Tracking for unused analysis (distractor)
        if key not in history_tracker:
            history_tracker[key] = []
        history_tracker[key].append(combined)
        
        # Conditional penalty
        if combined < 50:
            penalties.append(10)
        
        total += combined
    
    # Red herring: complex penalty logic that ends up unused
    adjustment_factor = 1.0
    if len(penalties) > 2:
        adjustment_factor = 0.9
    elif len(penalties) == 1:
        adjustment_factor = 0.95
    
    # Final score computed without using adjustment_factor (misleading path)
    raw_final = total / len(data)
    
    # Additional irrelevant dictionary operation
    metadata_summary = {k: len(v['components']) for k, v in data.items()}
    unused_aggregate = sum(metadata_summary.values())
    
    final_score = int(raw_final)  # Actual answer assignment
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution block
benchmark_data = {
    'module_1': {
        'components': {
            'A': {'base_value': 95, 'history': [70, 75, 80]},
            'B': {'base_value': 110, 'history': [85, 90]}
        },
        'version': '2.1'
    },
    'module_2': {
        'components': {
            'A': {'base_value': 120, 'history': [100, 105]},
            'B': {'base_value': 85, 'history': [70, 75, 80, 82]}
        },
        'version': '2.2'
    },
    'module_3': {
        'components': {
            'A': {'base_value': 70, 'history': [60, 65]},
            'B': {'base_value': 90, 'history': [88]}
        },
        'version': '2.3'
    }
}

# Entry point
final_score = calculate_performance(benchmark_data)