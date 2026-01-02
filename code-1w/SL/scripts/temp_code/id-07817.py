from collections import Counter

# Simulate log analysis for system performance evaluation
def analyze_logs(log_entries):
    severity_counter = Counter()
    total_entries = len(log_entries)
    warning_count = 0
    error_count = 0
    efficiency = 0.0

    temp_buffer = []
    for entry in log_entries:
        parts = entry.split(' ')
        level = parts[1]
        severity_counter[level] += 1

        if level == 'WARNING':
            warning_count += 1
            temp_buffer.append(entry)
        elif level == 'ERROR':
            error_count += 1

    # Irrelevant sorting of a temporary buffer (distractor)
    temp_buffer.sort()

    # Simulate processing delay simulation (misleading computation)
    delay_accumulator = 0
    for i in range(min(warning_count, 10)):
        delay_accumulator += (i * 0.1) ** 1.5

    # Core logic: compute efficiency based on ratio
    if total_entries > 0:
        success_rate = (total_entries - error_count) / total_entries
        efficiency = success_rate * 100

    return efficiency, error_count

# Evaluate performance with additional heuristics
def evaluate_performance(efficiency, error_count):
    base_score = efficiency * 1.5
    penalty = 0

    # Apply penalty tiers (nested conditions)
    if error_count > 5:
        penalty += 10
    elif error_count > 2:
        penalty += 5
    else:
        penalty += 1

    # Additional adjustment based on efficiency range
    if efficiency >= 90:
        bonus = 20
    elif efficiency >= 75:
        bonus = 10
    else:
        bonus = 0

    # Dead code path - never executed, but looks relevant (distractor)
    if False:
        bonus += get_hidden_bonus(efficiency)

    final_score = base_score - penalty + bonus
    return final_score

# Dummy function to simulate unused helper (dead code inclusion)
def get_hidden_bonus(value):
    return int(value % 7)

# Main execution
log_data = [
    "2024-01-01 INFO Startup",
    "2024-01-01 WARNING Disk usage high",
    "2024-01-01 ERROR DB connection failed",
    "2024-01-01 INFO Retry attempt 1",
    "2024-01-01 WARNING Memory pressure",
    "2024-01-01 ERROR DB timeout",
    "2024-01-01 INFO Fallback mode activated"
]

# Analyze logs and extract key metrics
efficiency, error_count = analyze_logs(log_data)

# Evaluate final performance score
final_score = evaluate_performance(efficiency, error_count)

print(f"Result: {final_score}")