from collections import defaultdict
import math

# Simulate sensor data processing with performance evaluation
raw_readings = [105, 97, 112, 89, 94, 118, 96]
baseline = 100
tolerance = 5

# Irrelevant temperature simulation
ambient_temps = [22.1, 23.5, 21.8, 24.0, 22.7]
adjusted_temps = [round(t * 1.02, 2) for t in ambient_temps]
deviation_map = defaultdict(float)
for i, t in enumerate(adjusted_temps):
    deviation_map[i] = round(abs(t - 22.5), 2)

# Distractor: unused function
def calculate_entropy(data):
    freqs = defaultdict(int)
    for x in data:
        freqs[x] += 1
    return -sum(f/len(data) * math.log2(f/len(data)) for f in freqs.values())

# Signal quality assessment (partially relevant)
signal_quality = []
for val in raw_readings:
    if val > baseline + tolerance:
        signal_quality.append('HIGH')
    elif val < baseline - tolerance:
        signal_quality.append('LOW')
    else:
        signal_quality.append('NORMAL')

# Distractor: dead code path
if False:
    correction_factor = 0.95
    raw_readings = [x * correction_factor for x in raw_readings]

# Extract statistical features
mean_reading = sum(raw_readings) / len(raw_readings)
variance = sum((x - mean_reading) ** 2 for x in raw_readings) / len(raw_readings)
std_dev = math.sqrt(variance)

# Normalize readings
normalized = [(x - mean_reading) / std_dev for x in raw_readings]

# Another distractor variable
smoothed = [normalized[0]]
for i in range(1, len(normalized)):
    smoothed.append(round(0.7 * normalized[i] + 0.3 * smoothed[-1], 3))

# Key metric computation
out_of_range_count = len([x for x in raw_readings if abs(x - baseline) > tolerance])
consistency_ratio = (len(raw_readings) - out_of_range_count) / len(raw_readings)
fluctuation_index = sum(1 for i in range(1, len(signal_quality)) if signal_quality[i] != signal_quality[i-1])

# Weight assignment (some weights are red herrings)
weights = {
    'stability': 0.4,
    'consistency': 0.3,
    'rarity': 0.2,  # unused weight
    'complexity': 0.1  # unused weight
}

# Metrics that feed into final score
metrics = {
    'stability': round(100 - (fluctuation_index * 2), 2),
    'consistency': round(consistency_ratio * 100, 2),
    'efficiency': 87  # fixed placeholder, minor relevance
}

# Unused diagnostic block
def analyze_trend(seq):
    up = down = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            up += 1
        elif seq[i] < seq[i-1]:
            down += 1
    return {'ups': up, 'downs': down}

trend_analysis = analyze_trend(raw_readings)

# Core evaluation logic
status_flags = []
for mq in signal_quality:
    if mq == 'NORMAL':
        status_flags.append(1)
    else:
        status_flags.append(0)

penalty_rate = 1 - (sum(status_flags) / len(status_flags))
base_performance = (metrics['stability'] + metrics['consistency']) / 2
adjusted_performance = base_performance * (1 - 0.5 * penalty_rate)

# Final integration
final_score = 0
def evaluate_performance(mets, wts):
    score = 0
    for key in ['stability', 'consistency']:
        if key in mets and key in wts:
            score += mets[key] * wts[key]
    # Boost for low fluctuation
    if fluctuation_index <= 3:
        score += 10
    return int(round(score))

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")