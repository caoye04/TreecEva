from itertools import combinations

# Simulate sensor data analysis with noise filtering and threshold logic
def analyze_fluctuations(readings):
    smoothed = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    trend = sum(1 for x in smoothed if x > 5)
    return trend

def generate_pairs(values):
    # Irrelevant helper: generates pairs but not used in final score
    return list(combinations(values, 2))

def validate_integrity(checksum, length):
    # Distractor function: looks important but unused
    return (checksum + length) % 7 == 0

def calculate_final_score(dataset, limits):
    base = 0
    anomalies = 0
    temp_buffer = []

    for entry in dataset:
        # Bitwise flag inspection (relevant)
        flags = entry['status']
        if flags & 8:  # masked interrupt
            base += 3
        if flags & 1 and flags & 4:
            base -= 1

        # Sensor fluctuation analysis (relevant)
        reading_log = entry['readings']
        spike_count = analyze_fluctuations(reading_log)
        if spike_count > limits['spike_threshold']:
            anomalies += 1

        # Dead code path: never executed due to constant condition
        if False:
            temp_buffer.append(spike_count * 2)

        # Conditional logic with distractor variables
        avg_reading = sum(reading_log) / len(reading_log)
        offset_correction = avg_reading * 0.1  # computed but unused

    # Composite scoring logic
    penalty = anomalies * 5
    final = base - penalty

    # Additional irrelevant computation
    dummy_sequence = [i ^ 17 for i in range(len(dataset))]
    dummy_sum = sum(dummy_sequence) // 100  # has no effect

    # Final adjustment using control flow
    adjustment = 10 if final > 0 else -5
    final += adjustment

    # Key assignment
    final_score = final + len(dataset) // 2

    return final_score

# Main execution
sensor_data = [
    {'status': 9, 'readings': [10, 12, 20, 25, 30]},   # status=1001b
    {'status': 5, 'readings': [8, 15, 16, 14, 9]},      # status=0101b
    {'status': 12, 'readings': [5, 6, 12, 20, 21]}     # status=1100b
]

detection_thresholds = {
    'spike_threshold': 1,
    'timeout': 300  # unused parameter
}

# Extra distraction variables
total_packets = len(sensor_data) * 2
drop_rate = total_packets * 0.05

result = calculate_final_score(sensor_data, detection_thresholds)
print(f"Result: {result}")