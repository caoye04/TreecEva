from collections import defaultdict, Counter
import itertools

# Simulated sensor array data with metadata
def fetch_sensor_data():
    raw_streams = [
        [145, 127, 139, 152, 133, 141],
        [98, 110, 105, 112, 99, 103],
        [201, 198, 205, 197, 202, 200],
        [76, 81, 74, 79, 82, 77]
    ]
    labels = ['temp', 'pressure', 'vibration', 'humidity']
    return {labels[i]: raw_streams[i] for i in range(len(labels))}

# Irrelevant utility: computes pairwise deltas (not used in final path)
def compute_deltas(signal):
    return [abs(signal[i+1] - signal[i]) for i in range(len(signal)-1)]

# Misleading preprocessing: appears important but is unused
def normalize_signal(signal, base=100):
    return [round((x - base) / base, 3) for x in signal]

# Decoy function: looks like it's part of analysis but never called
def apply_fourier_transform(signal):
    transformed = []
    for k in range(len(signal)):
        comp = sum(signal[n] * (2.0 * 3.14159 * k * n / len(signal)) for n in range(len(signal)))
        transformed.append(round(comp, 2))
    return transformed

# Core filtering logic based on dynamic thresholds
def filter_outliers(data, factor=1.5):
    filtered = {}
    for key, values in data.items():
        median_val = sorted(values)[len(values)//2]
        mad = sorted([abs(x - median_val) for x in values])[len(values)//2]
        upper = median_val + factor * mad * 2
        lower = median_val - factor * mad * 2
        filtered[key] = [x for x in values if lower <= x <= upper]
    return filtered

# Auxiliary mapping for threshold levels by sensor type
def generate_threshold_map(metrics):
    base_map = defaultdict(lambda: (0, 1000))
    base_map['temp'] = (130, 150)
    base_map['pressure'] = (95, 115)
    base_map['vibration'] = (195, 210)
    base_map['humidity'] = (70, 85)
    # Dead code branch - never accessed due to default dict behavior
    if 'co2' in metrics:
        base_map['co2'] = (400, 450)
    return base_map

# Real-time diagnostic engine with bit-encoded status flags
def analyze_stability(readings):
    status_flags = 0
    for i, val in enumerate(readings):
        if val > 100 and val % 2 == 0:
            status_flags |= (1 << i)  # Set bit if high even value
    return status_flags

# Main processing pipeline with red herring operations
def process_readings(dataset, thresholds):
    # Intermediate variables with plausible but unused transformations
    aggregated = defaultdict(float)
    entropy_tracker = []
    
    for sensor_type, values in dataset.items():
        low, high = thresholds[sensor_type]
        valid_range = [v for v in values if low <= v <= high]
        
        # Actual relevant computation
        if sensor_type == 'vibration':
            aggregated['vib_avg'] = sum(valid_range) / len(valid_range)
        
        # Distractor: complex but unused entropy-like calculation
        freqs = Counter(itertools.chain.from_iterable(
            [[x]*2 for x in values if x % 3 == 0]
        ))
        entropy = sum(f * f for f in freqs.values())
        entropy_tracker.append(entropy + 1e-5)
        
    # Critical diagnostic derived from vibration average
    vib_avg = aggregated['vib_avg']
    calibration_offset = 0.75
    normalized_score = (vib_avg - 190) * 2.3
    
    # Bit manipulation decoy - looks significant but unused
    encoded_diagnostics = int(normalized_score) ^ 0xAA55
    encoded_diagnostics = (encoded_diagnostics << 1) | (encoded_diagnostics >> 15)
    
    # Final result based on processed vibration data
    final_diagnostic = int((normalized_score - calibration_offset) * 10) / 10.0
    
    # Multiple print statements mimicking debugging (only last matters)
    print(f"Raw stability: {analyze_stability(dataset['vibration'])}")
    print(f"Entropy traces: {entropy_tracker}")
    return final_diagnostic

# --- Execution Sequence ---
sensor_data = fetch_sensor_data()

# Irrelevant transformations (distractors)
delta_pressure = compute_deltas(sensor_data['pressure'])
norm_humidity = normalize_signal(sensor_data['humidity'], base=75)

# Real execution path begins here
filtered_data = filter_outliers(sensor_data, factor=1.8)
threshold_map = generate_threshold_map(sensor_data.keys())

# Key statement containing the answer
target_result = process_readings(filtered_data, threshold_map)
print(f"Target result: {target_result}")