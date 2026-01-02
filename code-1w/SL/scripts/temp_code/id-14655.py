from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation over time
raw_readings = [14.2, 18.7, 25.3, 19.1, 22.4, 20.5, 24.8, 26.9, 17.6, 23.2]

def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1.1
        elif data[i] < data[i-1]:
            trend_score -= 0.9
    return round(trend_score, 2)

trend_index = analyze_trend(raw_readings)

# Irrelevant secondary analysis: environmental noise (distractor)
environment_noise = [0.1, 0.3, 0.2, 0.5, 0.7, 0.6, 0.8, 0.4, 0.9, 0.2]
noise_counter = Counter()
for noise in environment_noise:
    bucket = int(noise * 10)
    noise_counter[bucket] += 1

# System state mapping (mixed relevance)
system_state = defaultdict(lambda: 'unknown')
system_state.update({
    0: 'critical',
    1: 'elevated',
    2: 'normal',
    3: 'optimal'
})

# Health thresholds and decay model
base_threshold = 18.5
decay_factor = 0.93
adjusted_limits = []
for i in range(5):
    adjusted_limits.append(round(base_threshold * (decay_factor ** i), 3))

# Falsely relevant signal filter (dead path)
def apply_filter(signal_list, method='moving_avg'):
    if method == 'sma':
        return [sum(signal_list[i:i+3])/3 for i in range(len(signal_list)-2)]
    elif method == 'ema':
        ema = [signal_list[0]]
        for val in signal_list[1:]:
            ema.append(ema[-1] * 0.7 + val * 0.3)
        return ema
    else:
        return []  # unused

filtered_data = apply_filter(raw_readings, 'invalid_method')  # This returns []

# Core diagnostic logic with red herrings
health_trace = []
for reading in raw_readings:
    if reading > adjusted_limits[0]:
        health_trace.append(2)
    elif reading > adjusted_limits[2]:
        health_trace.append(1)
    else:
        health_trace.append(0)

# Misleading complexity: recursive depth counter (partially irrelevant)
def count_transitions(seq, index=0, depth=0):
    if index >= len(seq) - 1 or depth > 10:
        return 0
    current = 1 if seq[index] != seq[index+1] else 0
    return current + count_transitions(seq, index+1, depth+1)

transition_count = count_transitions(health_trace)

# Auxiliary log with decoy metrics
system_log = {
    'timestamp': '2023-10-15T08:45:30Z',
    'mode': 'diagnostic',
    'version': 2.1,
    'readings_processed': len(raw_readings),
    'trend_score': trend_index,
    'transitions': transition_count,
    'checksum': sum([int(x) for x in adjusted_limits])
}

# Decoy function that calculates unrelated statistic
def compute_entropy(values):
    counts = defaultdict(int)
    for v in values:
        counts[v] += 1
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

entropy_metric = compute_entropy(health_trace)  # Computed but not used directly

# Central processing with multiple inputs and subtle logic
healthy_windows = 0
for i in range(len(health_trace) - 2):
    window = health_trace[i:i+3]
    if all(x >= 1 for x in window):
        healthy_windows += 1

# Final weighting using trend and structural analysis
def process_metrics(trace, log):
    base_weight = log['trend_score'] * 10
    adjustment = 0
    if log['transitions'] < 5:
        adjustment += 15
    else:
        adjustment -= 5
    
    # Critical dependency on healthy window count
    window_bonus = healthy_windows * 7
    
    # Noise-influenced term (but noise was never properly integrated - red herring)
    fake_noise_influence = 0
    if 'noise_level' in log:  # Never true
        fake_noise_influence = log['noise_level'] * 10
    
    # Actual calculation ignores entropy and noise
    result = base_weight + adjustment + window_bonus
    return int(round(result))

final_diagnostic = process_metrics(health_trace, system_log)
print(f"Target result: {final_diagnostic}")