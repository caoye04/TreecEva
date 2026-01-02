from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_samples):
    filtered = []
    noise_floor = 0.05
    for sample in raw_samples:
        if abs(sample) > noise_floor:
            filtered.append(round(sample * 100) / 100)
    return filtered

# Irrelevant transformation: spectral decomposition (not used in final result)
def spectral_decompose(signal):
    magnitude = 0
    for i in range(len(signal)):
        magnitude += signal[i] * math.sin(i * math.pi / 4)
    return magnitude * 0.1  # red herring

# Core pattern detection logic
def detect_anomalies(sequence):
    anomalies = []
    for i in range(1, len(sequence) - 1):
        prev, curr, next_val = sequence[i-1], sequence[i], sequence[i+1]
        if curr > prev and curr > next_val and curr > 0.75:
            anomalies.append(i)
        elif curr < prev and curr < next_val and curr < -0.75:
            anomalies.append(-i)
    return anomalies

# Data enrichment with decoy features
def enrich_dataset(data_points):
    enriched = defaultdict(list)
    stats_summary = {'peaks': 0, 'valleys': 0, 'trend': None}
    cumulative = 0
    
    for idx, val in enumerate(data_points):
        binary_tag = bin(int(abs(val * 10)) % 8)
        enriched['tags'].append(binary_tag)
        enriched['indices'].append(idx)
        
        # Distractor computation: running XOR of fractional parts
        frac_part = int((val - int(val)) * 100) if val >= 0 else int((abs(val) - int(abs(val))) * 100)
        cumulative ^= frac_part
        
        # Unused statistical tracking
        if val > 0.5:
            stats_summary['peaks'] += 1
        elif val < -0.5:
            stats_summary['valleys'] += 1
            
    stats_summary['trend'] = sum(data_points) / len(data_points)
    return enriched  # not used in main flow

# Primary transformation pipeline
def transform_signal(input_stream, phase_offset=1.2):
    shifted = []
    for x in input_stream:
        shifted_x = x + phase_offset
        transformed = math.cos(shifted_x) * math.sin(shifted_x * 0.5) + math.log(abs(shifted_x) + 1)
        shifted.append(round(transformed, 3))
    return shifted

# Misleading auxiliary function (dead code path)
def legacy_calibrate(buf):
    if not buf:
        return 0
    acc = 0
    for v in buf:
        acc += v ** 2
    return math.sqrt(acc) // 1

# Main analysis engine
def analyze_pattern(dataset, offset):
    temp_state = []
    base_reference = [math.tan(offset * i) for i in range(1, 6)]
    
    for i, val in enumerate(dataset):
        # Complex conditional with bit manipulation distraction
        if i % 2 == 0:
            adjusted = val * base_reference[i % 5]
            # Bitwise red herring
            magic_factor = (int(abs(adjusted) * 100) & 0xF) ^ 5
            adjusted = adjusted + (magic_factor * 0.01)
        else:
            adjusted = val + base_reference[i % 5] - 0.1
        
        temp_state.append(round(adjusted, 4))
    
    # Secondary processing with counting distraction
    count_tracker = Counter()
    for v in temp_state:
        bucket = int(abs(v) * 10)
        count_tracker[bucket] += 1
        # Useless accumulation
        count_tracker[bucket] += (bucket % 3) - 1
    
    # Final reduction to scalar diagnostic
    diagnostic_score = 0
    for i, v in enumerate(temp_state):
        diagnostic_score += v * (i + 1) * 0.1
    
    return round(diagnostic_score, 6)

# === Execution Flow with High Interference ===
raw_sensor_data = [0.12, -0.34, 0.56, 0.78, -0.91, 0.23, -0.45, 0.67]

# Step 1: Preprocess signal
cleaned = preprocess_readings(raw_sensor_data)

# Step 2: Irrelevant spectral analysis (distractor call)
spectral_signature = spectral_decompose(cleaned)  # unused later

# Step 3: Detect anomaly positions (partially relevant)
anomaly_positions = detect_anomalies(cleaned)

# Step 4: Enrich with metadata (returns but not used)
metadata_pool = enrich_dataset(cleaned)

# Step 5: Transform signal using nonlinear functions
transformed_data = transform_signal(cleaned, phase_offset=1.5)

# Step 6: Introduce baseline shift from anomaly pattern
baseline_shift = len(anomaly_positions) * 0.3 + 0.1

# Step 7: Critical statement — compute final diagnostic
final_diagnostic = analyze_pattern(transformed_data, baseline_shift)

# Print result for evaluation
print(f"Result: {final_diagnostic}")