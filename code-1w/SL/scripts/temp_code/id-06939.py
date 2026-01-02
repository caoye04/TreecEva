from collections import defaultdict, Counter
from itertools import cycle
import math

# Simulated sensor array data with noise and redundant channels
def generate_raw_samples():
    samples = []
    for i in range(200):
        sample = {
            'timestamp': i,
            'sensor_A': 3.1 * i % 7,
            'sensor_B': (i ** 2) % 11,
            'sensor_C': abs((i * 0.5) - 50),
            'redundant_1': i * 0.01,  # Distractor sensor
            'redundant_2': (i + 5) // 3,  # Another irrelevant metric
            'checksum': i ^ (i >> 1),     # Bitwise red herring
            'flagged': False if i % 17 else True  # Misleading boolean trap
        }
        samples.append(sample)
    return samples

# Irrelevant transformation: simulates calibration but unused
def calibrate_sensor(x, factor=1.05):
    return x * factor if x < 100 else x

# Decoy function that looks important but is never called
def analyze_anomalies(data):
    anomaly_count = 0
    for entry in data:
        if entry['sensor_B'] > 8 and entry['sensor_C'] < 40:
            anomaly_count += 1
    return anomaly_count  # Dead end

# Actual filtering: remove noisy low-value readings
def filter_data(data):
    filtered = []
    threshold = 2.5
    for entry in data:
        # Only keep entries where primary sensors show meaningful activity
        if entry['sensor_A'] > threshold or entry['sensor_C'] > threshold * 4:
            # Extract only relevant fields
            cleaned = {
                't': entry['timestamp'],
                'a': entry['sensor_A'],
                'b': entry['sensor_B'],
                'c': entry['sensor_C']
            }
            filtered.append(cleaned)
    return filtered

# Core processing pipeline

# Weighting strategy using lambda abstraction
weight_fn = lambda x, y: math.log(1 + x) * (y ** 0.3)

# Aggregation via defaultdict to simulate multi-pass analysis
def process_readings(filtered_data):
    aggregator = defaultdict(float)
    stats = defaultdict(int)
    
    # Simulate cyclic correction pattern (itertools usage)
    phase_cycle = cycle([1, -1, 0])
    
    for idx, reading in enumerate(filtered_data):
        phase = next(phase_cycle)
        
        # Real computation path
        score_a = weight_fn(reading['a'], reading['t'])
        score_b = reading['b'] * 0.7 + phase  # Minor phase modulation
        score_c = reading['c'] / (idx + 1) if idx > 0 else reading['c']
        
        # Accumulate weighted contributions
        aggregator['diagnostic_sum'] += (score_a + score_b) * score_c
        
        # Irrelevant counters (distractors)
        stats['processed'] += 1
        if reading['b'] % 3 == 0:
            stats['divisible_by_three'] += 1
        
        # Dummy bit manipulation to mislead
        temp_key = reading['t'] & 0xFF
        aggregator[temp_key] += 0.1  # Scatter attention
    
    # Secondary transformation on results
    raw_total = aggregator['diagnostic_sum']
    
    # Apply nonlinear compression
    compressed = math.tanh(raw_total / 1000)
    
    # Final adjustment based on distribution of values
    counter = Counter([r['b'] % 5 for r in filtered_data])
    mode_adjustment = counter.most_common(1)[0][1]
    
    # TRUE ANSWER COMPUTATION
    final_diagnostic = int(compressed * 1000) + mode_adjustment * 2
    
    # Red herring: use of XOR on timestamps for fake checksum
    fake_checksum = 0
    for r in filtered_data:
        fake_checksum ^= r['t']
    
    # Output true result despite distractions
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
raw_samples = generate_raw_samples()

# Unused diagnostic (distractor call)
dummy_analysis = 0
for s in raw_samples[:10]:
    dummy_analysis += int(s['redundant_1'] + s['redundant_2'])

dummy_analysis = dummy_analysis << 2  # Bit shift decoy

# Key execution point
final_diagnostic = process_readings(filter_data(raw_samples))