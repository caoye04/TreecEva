def calculate_performance(base, data):
    adjustments = set()
    for key in data:
        if key.startswith('delta_'):
            adjustments.add(key)

    net_change = 0
    for adj in adjustments:
        net_change += data[adj]

    threshold = base * 0.1
    if abs(net_change) > threshold:
        multiplier = 1.2
    else:
        multiplier = 1.0

    temp_result = base + net_change
    final_rating = temp_result * multiplier

    # Irrelevant auxiliary variable (minimal distraction)
    debug_mode = False

    return int(final_rating)

# Main execution
baseline = 85
metrics = {
    'delta_temp': 5,
    'delta_pressure': -3,
    'delta_flow': 2,
    'status': 'active',
    'version': 2
}

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")