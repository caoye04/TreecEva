import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S1', 'S2', 'S3', 'S4']
baseline_readings = [23.5, 24.1, 22.8, 25.0]
calibration_offsets = [0.2, -0.3, 0.1, 0.0]

# Irrelevant maintenance logs (distractor data)
maintenance_log = {
    'last_cleaned': '2023-05-12',
    'firmware': 'v2.1.0',
    'location': 'Chamber A'
}

# Simulate raw signal capture with noise
raw_signals = []
for i in range(len(baseline_readings)):
    noise = 0.5 * math.sin(i + 0.1)
    raw_signals.append(baseline_readings[i] + noise + calibration_offsets[i])

# Signal processing pipeline
filter_threshold = 24.0
effective_signals = []
rejected_count = 0

for val in raw_signals:
    if abs(val - filter_threshold) < 1.5:
        effective_signals.append(round(val, 2))
    else:
        rejected_count += 1

# Dead code path - never executed due to logic (red herring)
temporary_buffer = []
if rejected_count > 10:
    for x in raw_signals:
        temporary_buffer.append(x * 1.1)

# Decoy function that is defined but not used
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 0)

# Actual processing begins here
processed_signals = []
for s in effective_signals:
    processed = s * 1.05
    if processed < 25.0:
        processed += 0.8
    processed_signals.append(round(processed, 2))

# Set operations: identify anomalous vs stable readings
stable_set = set()
anomalous_set = set()
reference_set = {24.5, 24.6, 24.7, 24.8, 24.9}

for p in processed_signals:
    if round(p, 1) in reference_set:
        stable_set.add(round(p, 1))
    else:
        anomalous_set.add(round(p, 1))

# Bit manipulation red herring (irrelevant computation)
bit_flag = 0
for x in stable_set:
    bit_flag ^= int(x) & 7

# Character counting distraction
diag_string = "SensorStabilityCheck"
char_count = len([c for c in diag_string if c.isupper()])  # Always 4

# Case conversion distractor
norm_tag = diag_string.lower().replace("sensor", "node")

# Core diagnostic logic (critical path)
def analyze_readings(readings):
    total = 0.0
    weight_factor = 1.0
    
    # Conditional weighting based on modular pattern
    for i, val in enumerate(readings):
        if i % 2 == 0:
            weight_factor = 1.2
        else:
            weight_factor = 0.95
        
        # Modular arithmetic adjustment
        mod_adjusted = (val * 100) % 47
        total += mod_adjusted * weight_factor
    
    # Final transformation
    final_score = (total * 1.07) - 33.5
    return int(round(final_score))

# Unused recursive decoy
def recursive_diagnostics(n):
    if n <= 1:
        return 1
    return recursive_diagnostics(n-1) + recursive_diagnostics(n-2)

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")