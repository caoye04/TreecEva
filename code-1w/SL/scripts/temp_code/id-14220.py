def analyze_performance(metrics):
    base = sum([v['score'] for v in metrics if v['active']])
    penalty = 0
    temp_adjustment = 0
    
    for entry in metrics:
        if entry['type'] == 'latency' and entry['value'] > 50:
            penalty += entry['value'] // 10
        elif entry['type'] == 'memory' and entry['critical']:
            temp_adjustment += entry['value'] * 0.1
    
    # Distractor: irrelevant computation on debug flags
    debug_flags = [m.get('debug', False) for m in metrics]
    flag_count = len([f for f in debug_flags if f])
    dummy_result = flag_count * 100

    return base - penalty


def validate_inputs(data):
    if not data or len(data) == 0:
        return False
    for d in data:
        if 'threshold' in d and d['threshold'] < 0:
            return False
    return True


def process_results(raw_data, limits):
    filtered = [r for r in raw_data if r['category'] in ['A', 'B']]
    assessment_data = []
    
    for item in filtered:
        score = item['base'] * 1.1
        
        # Simulate some state tracking
        status_log = []
        if score > limits['high']:
            category_type = 'excellent'
            status_log.append('high_perf')
        elif score > limits['medium']:
            category_type = 'good'
            status_log.append('moderate')
        else:
            category_type = 'basic'
            
        # Irrelevant list comprehension with no effect
        _ = [x * 2 for x in range(len(status_log)) if x % 2 == 0]

        assessment_data.append({
            'score': int(score),
            'active': item.get('enabled', True),
            'type': item['mode'],
            'category': category_type
        })
    
    # Introduce distractor variables
    snapshot = assessment_data[:2]  # slice but not used later
    total_entries = len(assessment_data)
    scaling_factor = total_entries if total_entries > 0 else 1
    
    # Unused nested structure
    summary = {
        'count': total_entries,
        'factors': {
            'scale': scaling_factor,
            'offset': 5
        }
    }
    
    # Core logic hidden among distractions
    processed = analyze_performance(assessment_data)
    adjustment = 10 if len(limits) > 2 else 5
    final_score = processed + adjustment
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input setup
raw_input = [
    {'base': 45, 'category': 'A', 'mode': 'latency', 'enabled': True},
    {'base': 30, 'category': 'B', 'mode': 'memory', 'enabled': True, 'critical': True},
    {'base': 20, 'category': 'C', 'mode': 'cpu', 'enabled': False},
    {'base': 40, 'category': 'B', 'mode': 'latency', 'enabled': True, 'debug': True}
]

config = {
    'high': 45,
    'medium': 35,
    'buffer': 10
}

# Execution point
final_score = process_results(raw_input, config)