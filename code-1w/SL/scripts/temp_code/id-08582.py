from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def analyze_workload(timestamps, thresholds):
    cumulative_load = 0
    peak_moments = []
    temp_buffer = []  # Unused decoy buffer
    mode_counter = defaultdict(int)

    for t in timestamps:
        if t < 0:
            continue  # Invalid timestamp guard
        adjusted = t * 1.05
        if adjusted > thresholds['critical']:
            peak_moments.append(adjusted)
        elif adjusted > thresholds['warning']:
            mode_counter['elevated'] += 1
        else:
            mode_counter['normal'] += 1
        cumulative_load += adjusted ** 0.5

    return cumulative_load, peak_moments, mode_counter

def evaluate_stability(readings):
    # Irrelevant stability metric (dead function)
    total = 0
    for r in readings:
        total += abs(r) ** 0.3
    return total / len(readings) if readings else 0

def parse_events(event_stream):
    # Distractor: parses unrelated event codes
    code_map = {'A': 1, 'B': 2, 'C': 3}
    parsed = []
    for e in event_stream:
        if e in code_map:
            parsed.append(code_map[e])
    return parsed  # Never used

def compute_entropy(data):
    # Misleading complexity: computes Shannon entropy (unused)
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return entropy

def aggregate_metrics(log_entries, flags):
    base_score = 0
    anomaly_count = 0
    flag_weights = {'overclocked': -5, 'debug_mode': 3, 'safe_boot': 2}

    for entry in log_entries:
        cycle_time = entry['duration']
        temp = entry['temp']
        if 'sensor_x9' in entry and entry['sensor_x9'] > 75:
            anomaly_count += 1

        # Core logic embedded in noise
        if cycle_time < 100 and temp > 80:
            base_score += 7
        elif temp > 85:
            base_score += 3
        else:
            base_score += 1

    # Critical weighting from flags
    for f in flags:
        base_score += flag_weights.get(f, 0)

    # Red herring: unused lambda transformation
    transform = lambda x: x * 1.75 if x < 50 else x * 0.85
    transformed_score = transform(base_score)  # Computed but unused

    # Real answer path
    diagnostic_value = base_score * 10 + anomaly_count

    # Decoy counters
    dummy_counter = Counter()
    for _ in range(3):
        dummy_counter['dummy'] += 1

    return diagnostic_value

# Main execution with irrelevant setup
timing_log = [
    {'duration': 95, 'temp': 82, 'sensor_x9': 78},
    {'duration': 105, 'temp': 86, 'sensor_x9': 72},
    {'duration': 88, 'temp': 79, 'sensor_x9': 81},
    {'duration': 92, 'temp': 88, 'sensor_x9': 83}
]

system_flags = ['overclocked', 'debug_mode']

# Dead data structures
aux_data = list(zip([1, 2, 3], ['x', 'y', 'z']))
enum_data = list(enumerate(aux_data))

# Unused analysis calls
cumulative, peaks, modes = analyze_workload([90, 110, 85], {'warning': 95, 'critical': 105})
stability = evaluate_stability([-1.2, 0.5, 2.3])
event_codes = parse_events(['A', 'B', 'X', 'C'])

# Key computation
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output required result
print(f"Target result: {final_diagnostic}")