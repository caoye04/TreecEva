def analyze_performance(metrics):
    avg_latency = sum(metrics['latency']) / len(metrics['latency'])
    success_rate = metrics['success'] / metrics['attempts']
    weighted_score = avg_latency * 0.3 + success_rate * 0.7
    return weighted_score

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum([x ** 2 for x in data if x > 5])

# Simulated system metrics
temp_readings = [23, 25, 27, 26, 28, 29, 24]
error_buffer = [0, 1, 0, 0, 1]

# Core data dictionary with performance stats
stats_dict = {
    'latency': [120, 150, 130, 110, 140],
    'attempts': 50,
    'success': 42,
    'retries': 8,
    'timeout_count': sum(1 for x in temp_readings if x > 27),  # distractor
    'checksum': len(temp_readings) * 17  # irrelevant metric
}

# Secondary analysis (semi-relevant but not used)
baseline = {'peak': max(stats_dict['latency']), 'floor': min(stats_dict['latency'])}
fluctuation = baseline['peak'] - baseline['floor']

# Conditional adjustment based on success rate (not actually impacting final logic)
adjustment_factor = 1.0
if stats_dict['success'] / stats_dict['attempts'] > 0.8:
    adjustment_factor = 1.1  # never applied, misleading

# Main scoring logic
def calculate_final_score(data):
    raw_score = analyze_performance(data)
    penalty = 0.0
    
    # Nested conditional with distractor variables
    if data['retries'] > 5:
        excess_ratio = (data['retries'] - 5) / data['attempts']
        penalty += excess_ratio * 10
    else:
        surplus = data['success'] - data['retries']  # unused
        bonus_tier = surplus // 10  # dead computation

    # Another distraction: character counting in keys (irrelevant)
    key_length_sum = sum(len(k) for k in data.keys())
    dummy_offset = key_length_sum * 0.01

    # Final calculation using only relevant components
    final_raw = raw_score * 100  # scale up
    final_raw -= penalty
    return int(final_raw)

# Execution point of interest
final_score = calculate_final_score(stats_dict)
print(f"Target result: {final_score}")