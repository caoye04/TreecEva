from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant channels
data_stream = [
    {'sensor_id': 'A7', 'type': 'temp', 'value': 32.1, 'seq': 1},
    {'sensor_id': 'B4', 'type': 'pressure', 'value': 101.3, 'seq': 2},
    {'sensor_id': 'A7', 'type': 'temp', 'value': 33.5, 'seq': 3},
    {'sensor_id': 'C9', 'type': 'humidity', 'value': 45.0, 'seq': 4},
    {'sensor_id': 'B4', 'type': 'pressure', 'value': 102.1, 'seq': 5},
    {'sensor_id': 'A7', 'type': 'temp', 'value': 31.8, 'seq': 6},
]

# Irrelevant helper that looks important but isn't used in critical path
def analyze_pattern(seq):
    if len(seq) < 3:
        return False
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return all(d == diffs[0] for d in diffs)

# Decoy accumulator for distraction
decoy_accumulator = 0
for item in data_stream:
    if item['type'] == 'temp':
        decoy_accumulator += item['value'] * 0.1

# Real processing starts here
sensor_cache = defaultdict(list)
for entry in data_stream:
    sensor_cache[entry['sensor_id']].append(entry['value'])

# Extract only temperature readings from sensor A7
a7_temps = sensor_cache['A7']

# Misleading transformation chain
transformed = [t ** 0.5 for t in a7_temps if t > 0]
shifted = [t + 1 for t in transformed]
filtered = [s for s in shifted if s > 5.5]  # Only one value passes

# Secondary red herring: pressure correlation (unused)
pressure_vals = [d['value'] for d in data_stream if d['type'] == 'pressure']
correlation_score = sum(p * 0.01 for p in pressure_vals)

# Core logic disguised among distractions
baseline = 32.0
adjustment_factor = 0.85
weighted_deviation = 0
for temp in a7_temps:
    weighted_deviation += (temp - baseline) * adjustment_factor

# Fake aggregation that seems relevant
fake_aggregate = Counter()
for d in data_stream:
    fake_aggregate[d['type']] += 1

# Critical intermediate: count of valid temperature fluctuations
fluctuations = 0
for i in range(1, len(a7_temps)):
    if abs(a7_temps[i] - a7_temps[i-1]) > 1.0:
        fluctuations += 1

# Distractor: nested loop with dead condition
redundant_sum = 0
for i in range(2):
    for j in range(3):
        if i > j:  # Never true
            redundant_sum += i * j

# Real signal extraction
signal_strength = len(filtered) * 1000  # filtered has 1 element
noise_floor = math.log(len(pressure_vals) + 1)
clean_signal = signal_strength - noise_floor

# Final computation buried in abstraction
def process_pipeline(stream):
    cache = defaultdict(list)
    for e in stream:
        cache[e['sensor_id']].append(e['value'])
    temps = cache['A7']
    base = 32.0
    dev = 0
    for t in temps:
        dev += (t - base) * 0.85
    sig = len([t**0.5 + 1 for t in temps if t > 0 and (t**0.5 + 1) > 5.5]) * 1000
    floor = math.log(len([d['value'] for d in stream if d['type'] == 'pressure']) + 1)
    return int(sig - floor + dev - 24.5)  # Final adjustment to land on clean integer

final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")