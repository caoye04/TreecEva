from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant channels
data_stream = [
    (1, 105, 'active', 0.8), (2, 110, 'idle', 0.1), (3, 98, 'active', 0.7),
    (4, 115, 'active', 0.9), (5, 93, 'fault', 0.0), (6, 120, 'active', 0.6),
    (7, 88, 'idle', 0.2), (8, 125, 'active', 1.1), (9, 95, 'active', 0.8),
    (10, 130, 'fault', 0.0)
]

# Irrelevant metadata - distractor
device_specs = {
    'model': 'X250',
    'firmware': 'v2.1.9',
    'calibration_offset': 0.03,
    'max_bandwidth': 1200,
    'legacy_mode': True
}

# Decoy processing function - never called
def analyze_pattern(seq):
    total = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            total += i * seq[i]
    return total // 2 if total > 0 else 0

# Unused transformation - dead code path
temp_conversion = lambda x: (x * 9/5) + 32

# Simulated historical logs - misleading context
historical_failures = [101, 102, 107, 108, 112]
failure_counter = Counter(historical_failures)

# Primary data accumulator - looks important but only partially used
event_log = defaultdict(list)
status_weights = {'active': 1.0, 'idle': 0.3, 'standby': 0.1, 'fault': 0.0}

# Initialize working variables
raw_values = []
signal_quality = []
status_flags = []

# First-pass filtering: extract valid entries and populate logs
for entry in data_stream:
    event_id, reading, status, confidence = entry
    
    # Log all events regardless of status - contributes to distraction
    event_log[status].append((event_id, reading))
    
    # Filter logic: only 'active' or 'idle' with reading > 90
    if status in ['active', 'idle'] and reading > 90:
        raw_values.append(reading)
        signal_quality.append(confidence)
        status_flags.append(status_weights[status])

# Secondary filter based on confidence threshold - actual relevant step
filtered_data = []
for i in range(len(raw_values)):
    if signal_quality[i] <= 1.0:  # Always true - red herring condition
        adjusted_value = raw_values[i] * status_flags[i]
        filtered_data.append(adjusted_value)

# Decoy statistical calculation - uses same data but irrelevant
mean_value = sum(raw_values) / len(raw_values) if raw_values else 0
variance_proxy = sum((x - mean_value) ** 2 for x in raw_values) / len(raw_values) if raw_values else 0

# Fake normalization chain - looks critical but unused
normalized = []
base_ref = 100
for val in raw_values:
    norm = (val - base_ref) / base_ref
    if norm < 0: norm = 0
    normalized.append(round(norm, 3))

# Begin actual processing chain that leads to answer
def compute_envelope(signal_list):
    envelope = 0
    for idx, val in enumerate(signal_list):
        if idx % 2 == 0:
            envelope += val * 0.8
        else:
            envelope -= val * 0.2
    return round(envelope, 4)

# Intermediate transformation - part of real logic
def extract_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks if peaks else [sum(data) / len(data)]

# Final processing function - key component
def process_readings(readings):
    # Step 1: Compute temporal envelope
    env = compute_envelope(readings)
    
    # Step 2: Detect local maxima
    peak_values = extract_peaks(readings)
    
    # Step 3: Aggregate diagnostic score
    peak_sum = sum(p for p in peak_values if p > 0)
    
    # Step 4: Apply decay factor based on length
    length_factor = 0.95 ** len(readings)
    
    # Step 5: Combine into final diagnostic index
    diagnostic_index = (env + peak_sum) * length_factor
    
    # Step 6: Clamp to meaningful range (not actually binding here)
    clamped = max(-1000000, min(1000000, diagnostic_index))
    
    # Step 7: Round to nearest integer - actual answer determination
    return int(round(clamped))

# Execute main processing
final_diagnostic = process_readings(filtered_data)

# Print result as required
print(f"Target result: {final_diagnostic}")