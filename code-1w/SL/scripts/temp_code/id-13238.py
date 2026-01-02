def process_results(data, config):
    # Preprocessing: extract and normalize values
    normalized = [x.lower().replace(' ', '_') for x in data.get('attributes', [])]
    
    # Mapping function using lambda for transformation
    transform = lambda val: sum(ord(c) for c in val) % config['mod_base']
    transformed_vals = [transform(val) for val in normalized]

    # Auxiliary calculation with distractor variables
    total_chars = sum(len(val) for val in data.get('attributes', []))
    avg_length = total_chars / len(data.get('attributes', [1])) if data.get('attributes') else 0
    size_factor = len(data.get('attributes', [])) * config['mod_base']

    # Dictionary-based scoring with red herring keys
    score_map = {
        'alpha': sum(transformed_vals),
        'beta': sum(v ** 2 for v in transformed_vals) // config['mod_base'],
        'gamma': len([v for v in transformed_vals if v > 5]),
        'delta': 999  # unused distractor value
    }

    # State tracking with intermediate irrelevant logic
    state_log = []
    temp_state = 0
    for i, v in enumerate(transformed_vals):
        if i % 2 == 0:
            temp_state += v * 2
        else:
            temp_state -= v
        state_log.append(temp_state % 100)

    # Core computation chain
    base_score = score_map['alpha'] + score_map['gamma']
    penalty = (size_factor - total_chars) if size_factor > 10 else 0
    adjustment = config['multiplier'] * (score_map['beta'] // 2)

    # Final derivation
    final_score = base_score - penalty + adjustment

    return final_score

# Input construction
user_data = {
    'attributes': ['ResponseTime', 'MemoryUsage', 'CPU Load', 'Latency'],
    'timestamp': 1712345678,
    'meta': {'version': '2.1', 'region': 'us-west'}
}

test_config = {
    'mod_base': 17,
    'multiplier': 3,
    'timeout': 5000
}

# Execution point
final_score = process_results(user_data, test_config)
print(f"Result: {final_score}")