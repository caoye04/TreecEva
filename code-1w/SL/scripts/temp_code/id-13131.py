from collections import defaultdict, Counter
def simulate_sensor_drift(raw_values):    
    # Irrelevant simulation of temperature drift (dead path)
    temp_drift = []
    for v in raw_values:
        temp_drift.append(v * 1.02 + 0.5 if v > 75 else v)
    return temp_drift

def generate_synthetic_data(n):
    # Distractor function: generates unused synthetic data
    return [i * 3 + (i % 7) for i in range(n)]

def filter_anomalies(data_stream):
    # Correctly filters values outside valid sensor range (80-110)
    filtered = []
    anomaly_log = defaultdict(int)
    for val in data_stream:
        if val < 80 or val > 110:
            anomaly_log['out_of_bounds'] += 1
        else:
            filtered.append(val)
    # Misleading intermediate: looks important but not used later
    total_anomalies = sum(anomaly_log.values())
    scaled = [x - 80 for x in filtered]  # Normalize base
    return scaled

def evaluate_coherence(sequence):
    # Dead logic path: analyzes sequence coherence but never called
    if len(sequence) < 2:
        return True
    for i in range(1, len(sequence)):
        if abs(sequence[i] - sequence[i-1]) > 15:
            return False
    return True

def process_readings(cleaned):
    # Core accumulation logic
    stats = Counter()
    running_total = 0
    for idx, reading in enumerate(cleaned):
        if idx % 2 == 0:
            running_total += reading * 1.5
        else:
            running_total += reading * 0.8
        # Bit manipulation red herring
        binary_shift = (reading << 1) ^ 3
        stats['processed'] += 1
        stats['sum_check'] += binary_shift % 5
    # Final transformation
    final_score = int(running_total + (stats['sum_check'] * 0.3))
    return final_score

# Main execution flow
base_inputs = [105, 67, 88, 115, 92, 76, 98, 101, 83, 120]

# Unused transformations (distractors)
synthetic_pool = generate_synthetic_data(20)
drifted_values = simulate_sensor_drift(base_inputs)

# Relevant processing chain
stable_readings = [val for val in base_inputs if 80 <= val <= 110]  # Repeats logic but necessary
primary_filtered = filter_anomalies(base_inputs)
final_diagnostic = process_readings(primary_filtered)

# Decoy output
interim_result = sum([x**2 for x in synthetic_pool[:5]]) // 100

print(f"Result: {final_diagnostic}")