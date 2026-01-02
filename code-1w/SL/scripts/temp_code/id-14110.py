import itertools

# System health monitoring simulation with red herrings and complex logic paths

def analyze_component_stability(readings, thresholds):
    stable_count = 0
    transient_anomalies = 0
    for i, (reading, threshold) in enumerate(zip(readings, thresholds)):
        if reading < threshold * 0.9:
            stable_count += 1
        elif reading > threshold * 1.1:
            transient_anomalies += 1
    return stable_count, transient_anomalies


def compute_entropy(data_stream):
    # Irrelevant entropy calculation (distraction)
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)


# Simulated sensor inputs (real data interlaced with noise)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
raw_readings = [87, 94, 85, 96, 88]
nominal_thresholds = [90, 95, 80, 100, 90]

# Phase 1: Stability analysis (partially relevant)
base_stable, anomalies = analyze_component_stability(raw_readings, nominal_thresholds)

# Decoy diagnostic chain
historical_data = [[85, 90, 87], [92, 94, 93], [80, 82, 81], [95, 97, 96], [89, 88, 90]]
consistency_metrics = []
for seq in historical_data:
    avg = sum(seq) / len(seq)
    dev = sum(abs(x - avg) for x in seq)
    consistency_metrics.append(dev < 5)

# Fake anomaly resolution protocol (dead path)
def resolve_anomaly(anomaly_code):
    mapping = {1: 'RETRY', 2: 'RESET', 3: 'ISOLATE'}
    return mapping.get(anomaly_code, 'IGNORE')

# Real signal extraction via bit manipulation (critical path)
status_flags = 0b10110  # Binary: S1=0, S2=1, S3=1, S4=1, S5=0 (LSB first)
active_components = bin(status_flags).count('1')

# Correlation engine (mix of relevant and irrelevant)
correlation_matrix = list(itertools.combinations([0, 1, 2, 3, 4], 2))
high_corr_pairs = 0
for a, b in correlation_matrix:
    if abs(raw_readings[a] - raw_readings[b]) < 5:
        high_corr_pairs += 1

# Secondary validation using enumeration (partially used)
weighted_sum = 0
for idx, reading in enumerate(raw_readings):
    weight = 1 + (idx % 2)  # Alternating weights
    weighted_sum += reading * weight

effective_baseline = weighted_sum // len(raw_readings)

# Distraction: Data stream entropy (unused later)
data_stream = [1, 1, 0, 1, 1, 1, 0, 0, 1]
stream_entropy = compute_entropy(data_stream)

# Conditional override simulation (never triggered - red herring)
if anomalies > 10 or effective_baseline < 50:
    for i in range(len(nominal_thresholds)):
        nominal_thresholds[i] *= 1.2

# Critical computation chain
aggregate_score = base_stable * 100 + active_components * 10 + (high_corr_pairs // 3)

# Hidden calibration factor based on bitwise XOR pattern
diagnostic_key = 0
for i, rid in enumerate(sensor_ids):
    diagnostic_key ^= ord(rid[-1])  # XOR last char of ID

correction_factor = diagnostic_key % 7 - 3  # Range: -3 to 3

adjustment_multiplier = 13  # Magic constant from legacy spec

# Key assignment: This is where the answer is determined
final_diagnostic = aggregate_score + correction_factor * adjustment_multiplier

# Final output
print(f"Result: {final_diagnostic}")