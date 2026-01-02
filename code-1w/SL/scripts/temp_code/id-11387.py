def analyze_system_efficiency(log_entries):
    # Parse timestamps and statuses from logs
    uptime_intervals = []
    downtime_events = 0
    temp_buffer = []

    for entry in log_entries:
        timestamp = int(entry.split(',')[0])
        status = entry.split(',')[1]

        if status == 'ON':
            temp_buffer.append(timestamp)
        elif status == 'OFF' and temp_buffer:
            uptime_intervals.append(timestamp - temp_buffer[0])
            temp_buffer.clear()
        if status == 'ERROR':
            downtime_events += 1

    total_uptime = sum(uptime_intervals)
    avg_uptime = total_uptime / len(uptime_intervals) if uptime_intervals else 0

    return total_uptime, avg_uptime, downtime_events


def calculate_redundancy_factor(config_matrix):
    # Compute matrix rank approximation via non-zero row counting
    rank_approx = 0
    for row in config_matrix:
        if any(cell != 0 for cell in row):
            rank_approx += 1

    parity_bits = 0
    for row in config_matrix:
        parity_bits += sum(row) % 2

    return rank_approx * 1.5 + parity_bits * 0.5


def evaluate_performance(metrics, weights):
    # Core evaluation logic
    base_performance = metrics['efficiency'] * weights[0]
    stability_bonus = (100 - metrics['downtime']) * weights[1]
    redundancy_penalty = metrics['redundancy'] * weights[2] * 0.1

    # Secondary adjustments
    adjustment_factor = 1.0
    if metrics['downtime'] < 5:
        adjustment_factor += 0.2
    if metrics['redundancy'] > 20:
        adjustment_factor -= 0.15

    # Final weighted score
    raw_score = (base_performance + stability_bonus - redundancy_penalty) * adjustment_factor

    # Normalize to 0-100 scale
    normalized = max(0, min(100, raw_score))

    # Distractor computation: entropy-like measure (not used)
    import math
    fake_entropy = 0.0
    for k in metrics:
        prob = (metrics[k] + 1) / (sum(metrics.values()) + len(metrics))
        fake_entropy -= prob * math.log(prob)

    # Unused intermediate variables (distraction)
    temp_result = normalized ** 2 / 100
    buffer_value = temp_result * 0.9 + 10
    final_score = round(normalized, 2)

    return final_score

# Simulated input data
log_data = [
    "100,ON", "150,ON", "200,OFF",
    "250,ON", "300,ON", "350,ERROR", "400,OFF",
    "450,ON", "500,OFF"
]

config_layout = [
    [1, 1, 0, 1],
    [0, 0, 0, 0],  # Zero row
    [1, 0, 1, 1],
    [1, 1, 1, 0]
]

# Extract system metrics
uptime_total, mean_cycle, errors_count = analyze_system_efficiency(log_data)
redundancy_level = calculate_redundancy_factor(config_layout)

# Prepare metric dictionary
system_metrics = {
    'efficiency': mean_cycle,
    'downtime': errors_count * 10,  # Scale error count
    'redundancy': redundancy_level
}

# Weight vector: efficiency, stability, redundancy
weights_vector = [0.6, 0.3, 0.1]

# Key statement
final_score = evaluate_performance(system_metrics, weights_vector)

print(f"Result: {final_score}")