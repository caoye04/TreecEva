from collections import defaultdict

# Simulate system performance analysis across multiple modules
def analyze_module_performance(log_lines):
    stats = defaultdict(int)
    errors = set()
    temp_buffer = []

    for line in log_lines:
        parts = line.split('|')
        level = parts[1].strip()
        message = parts[2].strip()

        stats['total_entries'] += 1
        if 'ERROR' in level:
            stats['errors'] += 1
            errors.add(message)
        elif 'WARN' in level:
            stats['warnings'] += 1

        # Irrelevant processing: tracking temporary buffer (distractor)
        if len(temp_buffer) > 5:
            temp_buffer.pop(0)
        temp_buffer.append(len(message))

    # Misleading metric that isn't used later
    average_temp_length = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stats['avg_msg_len'] = average_temp_length  # Not used in final logic

    return dict(stats), errors


def calculate_efficiency(raw_data, window_size=3):
    # Process sensor readings with sliding window smoothing
    smoothed = []
    for i in range(len(raw_data)):
        start = max(0, i - window_size + 1)
        window = raw_data[start:i+1]
        avg = sum(window) / len(window)
        smoothed.append(round(avg, 2))

    # Additional irrelevant transformation
    amplified = [x * 1.05 for x in smoothed if x > 0.5]  # Partial use, some distraction

    # Efficiency metric based on variance reduction
    raw_variance = sum((x - sum(raw_data)/len(raw_data))**2 for x in raw_data) / len(raw_data)
    smooth_variance = sum((x - sum(smoothed)/len(smoothed))**2 for x in smoothed) / len(smoothed)
    efficiency = (raw_variance - smooth_variance) / raw_variance if raw_variance > 0 else 0

    return round(efficiency, 4), amplified  # amplified not used later


def evaluate_performance(efficiency, error_count):
    # Core evaluation logic
    base_score = efficiency * 100
    penalty = error_count * 2.5
    final_score = base_score - penalty
    
    # Apply floor but no ceiling
    if final_score < 0:
        final_score = 0
    
    # Dead code branch (distractor)
    if False:
        final_score = max(final_score, 10)  # Never executed
        backup_adjustment = 5  # Unused variable

    return final_score

# Main execution
log_data = [
    "MOD|ERROR|Sensor timeout",
    "NET|INFO|Connection established",
    "MOD|ERROR|Invalid calibration",
    "STG|WARN|Low storage threshold",
    "MOD|INFO|Normal operation resumed",
    "NET|ERROR|Packet loss detected",
    "MOD|ERROR|Sensor timeout"  # Duplicate error
]

sensor_readings = [0.8, 0.75, 0.9, 0.6, 0.65, 0.7, 0.95, 1.0, 0.85]

# Step 1: Analyze logs
log_stats, error_set = analyze_module_performance(log_data)
error_count = log_stats['errors']  # Key input

# Step 2: Calculate efficiency
efficiency_metric, _ = calculate_efficiency(sensor_readings)

# Step 3: Evaluate final performance score
final_score = evaluate_performance(efficiency_metric, error_count)

# Output result
print(f"Result: {final_score}")