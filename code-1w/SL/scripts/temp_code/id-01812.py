def calculate_final_score(config):
    base = config['input_value']
    temp_result = 0
    adjustments = []

    # Misleading preprocessing block (not directly used)
    for i in range(3):
        noise = (i * 17) % 5
        adjustments.append(noise * 2)

    # Real computation begins
    if base > 100:
        base = base // 2
    elif base < 50:
        base = base * 1.5
    else:
        base = base + 25

    # Dictionary-based weight mapping
    weights = {
        'tier1': 0.8,
        'tier2': 1.1,
        'tier3': 1.4
    }

    category = config.get('category')
    multiplier = weights[category] if category in weights else 1.0

    # Intermediate distraction: string manipulation with no impact
    status_msg = "Processing data..."
    status_msg = status_msg.split(' ')[0].lower()
    status_msg = ''.join([c for c in status_msg if c != 's'])

    # Actual score calculation
    temp_result = base * multiplier

    # Red herring loop with dead logic
    outlier_count = 0
    for val in config['history']:
        if val > 200:
            outlier_count += 1
        if outlier_count > 10:  # Never reached due to data
            temp_result *= 0.9

    # Final adjustment based on threshold
    threshold_bump = 10 if temp_result >= 150 else 0
    final_score = int(temp_result + threshold_bump)

    return final_score

# Input data setup
data_map = {
    'input_value': 88,
    'category': 'tier2',
    'history': [95, 87, 90, 102, 113, 88, 95, 101, 99, 104]
}

# Execute and print result
final_score = calculate_final_score(data_map)
print(f"Result: {final_score}")