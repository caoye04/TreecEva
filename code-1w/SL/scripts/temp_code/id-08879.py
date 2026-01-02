from itertools import compress

def analyze_stability(data, threshold):
    deviations = [abs(x - 50) for x in data]
    stable_flags = [d < threshold for d in deviations]
    return list(compress(data, stable_flags))

def calculate_performance(base, logs):
    adjusted_logs = [x * 1.1 if x < base else x * 0.9 for x in logs]
    
    # Irrelevant transformation (distractor)
    temp_offset = sum([abs(y - base) for y in logs]) / len(logs) if logs else 0
    offset_correction = temp_offset * 0.5  # Not used later

    filtered_data = analyze_stability(adjusted_logs, 45)
    
    # Additional distraction: dead computation on string
    status_msg = "Processing complete"
    padded_msg = status_msg.ljust(20, '.')
    char_count = len(padded_msg.replace('.', ''))  # Unused

    raw_total = sum(filtered_data)
    count = len(filtered_data)
    average = raw_total / count if count > 0 else 0

    # Final logic step: performance score with bonus condition
    bonus = 10 if any(x > 60 for x in filtered_data) else 0
    penalty = 5 if all(x < 40 for x in filtered_data) else 0
    final_score = average + bonus - penalty
    
    return final_score

# Simulated sensor readings
baseline = 55
readings = [48, 52, 58, 45, 63, 39]

# Misleading pre-processing (semi-relevant but not impactful)
distorted_readings = [r ^ 1 for r in readings]  # Bitwise red herring
checksum = sum(r & 1 for r in distorted_readings)  # Unused metric

# Key execution point
temp_result = calculate_performance(baseline, readings)
final_score = temp_result

# Print result as required
print(f"Result: {final_score}")