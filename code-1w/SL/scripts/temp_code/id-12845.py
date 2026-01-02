import itertools

# Simulated sensor array data from a distributed monitoring system
def acquire_sensor_data():
    base_values = [1.2, 0.8, 3.4, 2.1, 0.9]
    return [v * 1.05 for v in base_values]

# Irrelevant transformation - dead end path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val for x in data]

# Unused but plausible signal smoothing function
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Core processing pipeline
sensor_readings = acquire_sensor_data()

# Apply non-linear gain correction (relevant)
corrected_readings = list(map(lambda x: x ** 1.5 if x > 1.0 else x ** 0.5, sensor_readings))

# Generate synthetic auxiliary channels (distractor)
aux_channels = []
for i in range(3):
    aux_channels.append([abs(c - (i+1)*0.3) for c in corrected_readings])

# Compute power spectrum harmonics (irrelevant computation)
harmonics = []
for reading in corrected_readings:
    harmonic_set = []
    for h in range(1, 4):
        harmonic_set.append(reading * (h ** 0.7) % 1.3)
    harmonics.append(harmonic_set)

# Real-time threshold detection (red herring)
active_thresholds = []
for val in corrected_readings:
    if val > 2.0:
        active_thresholds.append((val, 'HIGH'))
    elif val > 1.0:
        active_thresholds.append((val, 'MEDIUM'))
    else:
        active_thresholds.append((val, 'LOW'))

# Actual signal processing begins here
rolling_window = lambda seq, n: (seq[i:i+n] for i in range(len(seq)-n+1))
windows = list(rolling_window(corrected_readings, 2))

# Extract paired differential features
paired_deltas = [abs(w[1] - w[0]) for w in windows]

# Compute weighted coherence score (misleading intermediate result)
coherence_score = sum(paired_deltas) * 0.77

# Key data transformation chain
filtered_pairs = list(filter(lambda p: p[0] + p[1] > 2.5, windows))
expanded_features = list(itertools.chain.from_iterable(
    [[p[0]*0.9, p[1]*1.1, (p[0]+p[1])/2] for p in filtered_pairs]
))

# Add dummy metadata structure (distractor)
signal_metadata = {
    'source': 'ARRAY_7B',
    'calibration': '2023-Q4',
    'gain_factor': 1.05,
    'units': 'normalized_volts'
}

# Inject artificial noise floor (unused)
noise_floor = tuple(0.01 * (i % 4) for i in range(len(corrected_readings)))

# Processed signals - actual input to final analysis
processed_signals = [
    expanded_features[0] * 2.0,           # First amplified component
    sum(expanded_features[1:4]) / 3.0,    # Average of middle features
    expanded_features[-1] ** 2          # Squared last element
]

# Decoy analysis function that is never called
def legacy_diagnostic(signal):
    accum = 0
    for i, x in enumerate(signal):
        accum += x * (-1)**i
    return accum / len(signal)

# Final diagnostic engine
memory_cache = {}  # unused cache (distraction)

def analyze_readings(readings):
    # Nested conditional logic with red herrings
    if len(readings) < 2:
        return -999  # error code - unreachable due to prior logic
    
    primary = readings[0]
    secondary = readings[1]
    tertiary = readings[2] if len(readings) > 2 else 0
    
    # Complex interdependent calculations
    temp_a = primary * 1.8 + 32  # Fahrenheit conversion (deceptive)
    temp_b = (secondary - 32) * 5/9  # Back to Celsius (misdirection)
    
    # Actual critical computation path
    index = int((primary + secondary) % 3)  # determines routing
    
    results_pool = [
        primary ** secondary,
        secondary ** 0.5,
        (primary + tertiary) * 1.5
    ]
    
    # Conditional selection based on composite metric
    metric = (primary * 0.3) + (secondary * 0.7)
    
    if metric > 4.0:
        selected = results_pool[0]
    elif metric > 2.5:
        selected = results_pool[2]  # Correct branch taken
    else:
        selected = results_pool[1]
    
    # Final adjustment using bitwise manipulation (surprising but correct)
    raw_value = int(selected * 1000)
    masked = raw_value & 0xFFFF  # Apply 16-bit mask
    adjusted = masked ^ 0xAAAA  # XOR obfuscation
    
    # Reverse bit manipulation to recover meaningful result
    recovered = adjusted ^ 0xAAAA
    final_float = recovered / 1000.0
    
    # Inject decoy side effect
    memory_cache['last_result'] = final_float  # never accessed
    
    return final_float

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Target result: {final_diagnostic}")