def analyze_metrics(data):
    # Irrelevant transformation (dead path)
    temp_adjustment = sum(x ** 0.5 for x in data if x > 10)
    
    # Distractor: complex but unused calculation
    outlier_filter = list(filter(lambda x: x < (sum(data) / len(data)), data))
    normalized = [x / max(data) * 100 for x in data]

    # Real computation path begins
    valid_entries = [x for x in data if 5 <= x <= 50]
    base_score = sum(valid_entries)

    # Bit manipulation red herring
    encoded = 0
    for val in data[:3]:
        encoded ^= (val << 2) | (val >> 1)
    
    # Unused recursive distraction
    def recursive_weight(n):
        if n <= 1:
            return 1
        return recursive_weight(n-1) + recursive_weight(n-2)
    
    # Actual logic hidden among noise
    adjustment_factor = len(normalized) if len(normalized) % 2 else len(normalized) + 2
    raw_result = base_score * adjustment_factor

    # Conditional logic with misleading branches
    if base_score > 100:
        raw_result -= 15
    elif base_score < 50:
        raw_result += 25
    else:
        raw_result += 10  # This will be the case

    # Case conversion distractor (irrelevant string processing)
    status_flags = ['ERROR', 'OK', 'WARNING']
    lower_flags = [flag.lower() for flag in status_flags]
    flag_sum = sum(len(f) for f in lower_flags)

    # Key slicing operation (required python feature)
    segment = valid_entries[1:-1]  # Middle elements only
    segment_bonus = sum(segment) // len(segment) if segment else 0

    # Final aggregation with lambda (required python feature)
    modifier = lambda x: x * 1.1 if x > 20 else x * 0.9
    final_adjusted = modifier(raw_result + segment_bonus)

    return int(final_adjusted)


def evaluate_performance(diagnostic_logs):
    # Extract numeric sequence from logs (simulated parsing)
    readings = []
    for log in diagnostic_logs:
        parts = log.split(':')
        try:
            val = int(parts[-1])
            readings.append(val)
        except ValueError:
            continue  # Skip malformed entries

    # Call analysis function
    result = analyze_metrics(readings)

    # Decoy assignment
    result *= 1.05  # Looks important, but not used

    # Correct path
    return result

# Simulated input data with mixed content
logs = [
    "sensor_A:12",
    "sensor_B:7",
    "status:OK",
    "sensor_C:45",
    "error:NaN",
    "sensor_D:3",
    "sensor_E:28",
    "sensor_F:52",  # Excluded by filter
    "meta:checksum_9a1"
]

# Dead code path - never called
def auxiliary_debug(arr):
    return [x for x in arr if x & 1]

# Trigger execution
initial_estimate = sum(len(log) for log in logs)  # Red herring computation
interim_value = initial_estimate * 2 - 7  # Misleading intermediate

# Critical execution point
final_score = evaluate_performance(logs)

# Print result as required
print(f"Result: {final_score}")