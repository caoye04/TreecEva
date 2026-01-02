from collections import defaultdict, Counter

# Simulate sensor data stream with some noise
def generate_sensor_data():
    raw_data = [15, 22, 15, 30, 22, 18, 25, 30, 15, 22, 28, 25]
    noise_filter = lambda x: x if x < 30 else x - 5
    return [noise_filter(x) for x in raw_data]

# Process data through multiple stages
def process_sensor_data(raw):
    temp_stats = defaultdict(int)
    for val in raw:
        temp_stats['sum'] += val
        temp_stats['count'] += 1
        if val > 20:
            temp_stats['high_count'] += 1

    avg_temp = temp_stats['sum'] / temp_stats['count']
    fluctuation = max(raw) - min(raw)

    # Unrelated diagnostic metrics (distractors)
    diagnostics = {}
    diagnostics['stdev_guess'] = (fluctuation / 2.5)
    diagnostics['mode_hint'] = Counter(raw).most_common(1)[0][1]
    diagnostics['trend'] = 'stable' if abs(raw[-1] - raw[0]) < 5 else 'shifting'

    # Real processing path
    normalized = [x - avg_temp for x in raw]
    variance_estimate = sum([x**2 for x in normalized]) / len(normalized)
    return {
        'baseline': avg_temp,
        'variance': variance_estimate,
        'high_freq_ratio': temp_stats['high_count'] / temp_stats['count'],
        'adjusted_values': normalized
    }

# Calculate system efficiency based on processed data
def calculate_efficiency(data):
    base = data['baseline']
    var = data['variance']
    ratio = data['high_freq_ratio']

    # Secondary adjustments using semi-relevant heuristics
    stability_factor = 1.0 if var < 30 else 0.85
    load_factor = 0.9 + (ratio * 0.1)  # scales 0.9 to 1.0

    # Efficiency formula
    efficiency = (base * load_factor) * stability_factor

    # Irrelevant intermediate calculations (distraction)
    peak_adjustment = max(data['adjusted_values']) * 0.05
    decay_rate = 0.0
    for i in range(3):
        decay_rate += 0.01 * (i + 1)  # accumulates to 0.06, unused

    # Final adjustment - only one term matters
    final_efficiency = efficiency + peak_adjustment  # peak_adjustment very small
    rounded_efficiency = round(final_efficiency, 2)

    return rounded_efficiency

# Execution flow
sensor_input = generate_sensor_data()
processed_data = process_sensor_data(sensor_input)
efficiency_score = calculate_efficiency(processed_data)

# Additional irrelevant tracking variables
monitoring_log = []
for idx, val in enumerate(processed_data['adjusted_values']):
    if val > 2.0:
        monitoring_log.append(f"Event at {idx}")

system_diagnostics = {"version": "2.1", "status": "nominal"}
system_diagnostics['last_update'] = "pending"

Result: efficiency_score