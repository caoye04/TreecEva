import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [45, 52, 58, 43, 60, 67, 39, 71]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1010, 1014, 1009]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 41, 38, 55, 62, 29, 47, 51]  # dB levels - unused
turbidity_index = {i: val * 0.7 for i, val in enumerate([1.2, 0.9, 1.5, 2.1, 1.8])}  # Water clarity - unrelated

# Preprocessing: Normalize readings to baseline range [0, 100]
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) * 100 for x in data]

# Distractor function - never called
def compute_fourier_components(signal):
    """Irrelevant frequency analysis"""
    result = []
    for k in range(len(signal)//2):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        result.append(math.sqrt(real**2 + imag**2))
    return result

# Transform raw sensor inputs into composite health index
def transform_sensors(temp, humid, press):
    norm_temp = normalize(temp)
    norm_humid = normalize(humid)
    norm_press = normalize(press)
    
    # Apply non-linear weighting (real computation path)
    combined_index = []
    for i in range(len(norm_temp)):
        score = (norm_temp[i] * 0.4 + 
                norm_humid[i] * 0.3 + 
                (100 - abs(norm_press[i] - 50)) * 0.3)  # pressure deviation penalty
        combined_index.append(round(score, 2))
    return combined_index

# Mapping of thresholds by zone (key structure used later)
threshold_map = {
    'critical': 85,
    'elevated': 70,
    'normal': 50,
    'optimal': 90
}

# Secondary transformation: apply hysteresis and lag smoothing (red herring with partial use)
def smooth_sequence(seq, factor=0.3):
    if not seq:
        return []
    smoothed = [seq[0]]
    for i in range(1, len(seq)):
        smoothed.append(factor * seq[i] + (1 - factor) * smoothed[-1])
    return [round(x, 2) for x in smoothed]

# Unused recursive reducer (dead code path)
def recursive_reduce(data, depth=0):
    if depth >= 3 or len(data) == 1:
        return data[0] if data else 0
    mid = len(data) // 2
    left = recursive_reduce(data[:mid], depth + 1)
    right = recursive_reduce(data[mid:], depth + 1)
    return round((left + right) / 2, 2)

# Real transformation step - slicing and string-based tagging
transformed_data = transform_sensors(temperature_readings, humidity_readings, pressure_readings)

# Add metadata tags based on phase (uses string methods and slicing)
phases = ['startup', 'stabilization', 'operation', 'monitoring', 'recovery', 'diagnostic', 'calibration', 'idle']
phase_tags = [phases[i % len(phases)][::-1].upper() for i in range(len(transformed_data))]  # reverse and uppercase

# Attach tags but only use numeric values in final computation
annotated_readings = list(zip(transformed_data, phase_tags))
numeric_values = [x[0] for x in annotated_readings]  # strip off tags for processing

# Misleading accumulation (looks important but unused)
cumulative_drift = 0
historical_bias = []
for val in numeric_values:
    cumulative_drift += abs(val - 50) * 0.05
    historical_bias.append(round(cumulative_drift, 3))

# Set operation to identify anomaly clusters (actually used)
anomaly_set_a = {i for i, v in enumerate(numeric_values) if v > 75}
anomaly_set_b = {i for i, v in enumerate(norm_humidity) if v > 70}  # uses closure from earlier function scope
overlap_count = len(anomaly_set_a & anomaly_set_b)

# Primary analysis function with conditional logic and bit manipulation distraction
def analyze_readings(readings, thresholds):
    # Bitwise decoy
    magic_seed = 0b101010
    mask = (magic_seed << 2) ^ 0b1111
    masked_sum = sum(r * (i & mask) for i, r in enumerate(readings)) % 1000
    
    # Real logic begins here
    optimal_count = 0
    total_score = 0
    
    for idx, reading in enumerate(readings):
        total_score += reading
        # Determine status using threshold map
        if reading >= thresholds['optimal']:
            status_flag = 0b1000
        elif reading >= thresholds['critical']:
            status_flag = 0b0100
        elif reading >= thresholds['elevated']:
            status_flag = 0b0010
        else:
            status_flag = 0b0001
        
        # Only count fully optimal states
        if status_flag == 0b1000:
            optimal_count += 1
    
    # Incorporate overlap from set analysis (critical dependency)
    adjustment_factor = 1 + (overlap_count * 0.1)
    
    # Final diagnostic calculation
    base_diagnostic = (total_score / len(readings))
    adjusted_diagnostic = base_diagnostic * adjustment_factor + (optimal_count * 2.5)
    
    # String-based validation switch (uses slicing)
    verification_key = "DIAGNOSTICv2"[:10].lower()
    if verification_key.startswith("diag"):
        final_scale = 1.05
    else:
        final_scale = 1.0
    
    return round(base_diagnostic * final_scale + adjusted_diagnostic, 2)

# Execute key statement
final_diagnostic = analyze_readings(transformed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")