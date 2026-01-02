from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and redundant readings
timestamped_signals = [
    (1001, [3, 1, 4, 1, 5]), (1002, [2, 7, 1, 8, 2]), (1003, [1, 4, 1, 4, 2]),
    (1004, [1, 8, 2, 8, 1]), (1005, [9, 9, 5, 3, 6]), (1006, [2, 6, 5, 3, 5])
]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSETS = {"alpha": 0.023, "beta": -0.117, "gamma": 0.982}
REFERENCE_PATTERN = [1, 4, 1, 4, 2]

# Misleading preprocessing path (dead code - never called)
def legacy_filter(sequence):
    return [x for x in sequence if x % 2 == 1]

def generate_noise_profile(signal):
    # Unused function: creates red herring
    profile = []
    for i in range(len(signal)):
        profile.append((signal[i] + signal[(i+1)%len(signal)]) % 10)
    return profile

# Core analysis logic
noise_mask = {0: 7, 1: 3, 2: 1, 3: 9, 4: 5}  # Used in transformation

aggregated_data = []
raw_histogram = defaultdict(int)

for ts, readings in timestamped_signals:
    # Apply noise mask transformation (relevant)
    masked = [(readings[i] + noise_mask.get(i, 0)) % 10 for i in range(len(readings))]
    
    # Update frequency map (used later)
    for val in masked:
        raw_histogram[val] += 1
    
    # Add transformed block to aggregated data
    aggregated_data.extend(masked)

# Control sequence derived from statistical properties
mode_value = max(raw_histogram, key=lambda k: raw_histogram[k])
median_approx = sorted(raw_histogram.keys())[len(raw_histogram)//2]
control_seed = (mode_value * 3 + median_approx * 2) % 8

# Build control sequence using modular arithmetic and bit shifts
control_sequence = []
for i in range(8):
    val = (control_seed ^ i) * 3
    val = (val + (val >> 2)) % 10
    control_sequence.append(val)

# Auxiliary function that appears important but is only used once
def compute_entropy(seq):
    total = len(seq)
    freqs = Counter(seq)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Secondary distraction: unused correlation check
def cross_correlate(a, b):
    return sum(x * y for x, y in zip(a, b))

windowed_energy = []
for i in range(0, len(aggregated_data) - 4, 5):
    window = aggregated_data[i:i+5]
    energy = sum(x**2 for x in window) // len(window)
    windowed_energy.append(energy)

# Real-time anomaly flagging (partially irrelevant)
current_alert_level = 0
for energy in windowed_energy:
    if energy > 30:
        current_alert_level += 1

# Critical function: pattern diagnostic engine
def analyze_pattern(data, control):
    # Step 1: Count occurrences of control values in data
    data_set = set(data)
    control_set = set(control)
    overlap = data_set & control_set  # Set intersection
    base_score = sum(overlap)
    
    # Step 2: Frequency-weighted contribution
    freq_counter = Counter(data)
    weighted_addition = 0
    for val in overlap:
        weighted_addition += freq_counter[val] * val
    
    # Step 3: Apply combinatorial adjustment based on control structure
    n_pairs = 0
    for i in range(len(control) - 1):
        if control[i] % 2 == 0 and control[i+1] % 2 == 1:
            n_pairs += 1
    
    # Step 4: Final computation chain
    temp_result = base_score * 100 + weighted_addition
    adjustment = (n_pairs ** 2) * 17
    final_score = temp_result - adjustment
    
    # Decoy conditional (never triggers due to domain constraints)
    if any(x < 0 for x in data):
        final_score += 1000
    
    # Actual result
    return final_score

# Execute critical statement
final_diagnostic = analyze_pattern(aggregated_data, control_sequence)
print(f"Target result: {final_diagnostic}")