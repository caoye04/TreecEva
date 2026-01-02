from collections import defaultdict, Counter

# Simulated sensor data from environmental monitoring array
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.9, 23.0, 22.1]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015]

# Irrelevant auxiliary data (distractor)
satellite_ids = ['SAT-ALPHA', 'SAT-BETA', 'SAT-GAMMA']
transmission_log = {sid: [] for sid in satellite_ids}
buffer_cache = [[0]*len(humidity_readings) for _ in range(3)]

# Core processing variables
baseline_offset = 1.25
smoothing_factor = 0.85
adjusted_temps = [t + baseline_offset for t in temperature_readings]

# Apply exponential smoothing (relevant)
smoothed_temps = [adjusted_temps[0]]
for i in range(1, len(adjusted_temps)):
    smoothed_val = smoothing_factor * smoothed_temps[i-1] + (1 - smoothing_factor) * adjusted_temps[i]
    smoothed_temps.append(round(smoothed_val, 3))

# Normalize humidity to match temperature scale (distractor transformation)
normalized_humidity = [(h / 10) + 20 for h in humidity_readings]

# Generate composite index using bitwise manipulation (mixed relevance)
composite_index = []
for i in range(len(smoothed_temps)):
    temp_scaled = int((smoothed_temps[i] - 20) * 10)
    humid_scaled = int(humidity_readings[i] / 5)
    # Bitwise fusion of scaled values
    fused = (temp_scaled << 2) ^ (humid_scaled << 1) ^ (i & 3)
    composite_index.append(fused)

# Build threshold map based on pressure variance (actually relevant)
pressure_avg = sum(pressure_readings) / len(pressure_readings)
threshold_map = defaultdict(float)
for i, p in enumerate(pressure_readings):
    deviation = abs(p - pressure_avg)
    threshold_map[i] = 50 + (deviation * 0.75)

# Spurious mapping (dead path)
legacy_mapping = dict()
for idx in range(100):
    legacy_mapping[f"L{idx:02}"] = (idx * 17) % 97

# Data windowing with slicing (relevant)
window_size = 4
overlapping_windows = [
    composite_index[i:i+window_size] 
    for i in range(len(composite_index) - window_size + 1)
]

# Process windows through conditional logic
processed_data = []
for window in overlapping_windows:
    window_counter = Counter(window)
    dominant_value, freq = window_counter.most_common(1)[0]
    
    # Conditional transformation logic
    if freq >= 2:
        processed_value = dominant_value * 1.5
    elif sum(window) > 300:
        processed_value = sum(window) / 4
    else:
        mid_vals = window[1:3]
        processed_value = (mid_vals[0] + mid_vals[1]) * 0.9
    
    # Filtering based on threshold map (key dependency)
    center_idx = overlapping_windows.index(window) + 2
    if processed_value < threshold_map[center_idx]:
        processed_data.append(int(processed_value))
    else:
        processed_data.append(0)  # suppressed signal

# Dead code path: unused diagnostic chain
aux_diagnostic_chain = []
for x in processed_data:
    if x > 100:
        aux_diagnostic_chain.append(x >> 2)
    elif x > 50:
        aux_diagnostic_chain.append(x << 1)

# Critical analysis function (uses set operations and conditionals)
def analyze_signal(data, thresholds):
    if not data:
        return -1
    
    # Extract unique non-zero signals
    signal_set = set(data)
    signal_set.discard(0)
    
    if len(signal_set) == 0:
        return 0
    
    # Calculate entropy-like metric (irrelevant but plausible)
    total = sum(data)
    if total == 0:
        entropy_metric = 0
    else:
        entropy_metric = sum((x/total)**2 for x in data if x > 0)
    
    # Primary logic: weighted position scoring
    position_score = 0
    for i, val in enumerate(data):
        if val > 0:
            weight = 1 + (0.1 * i)  # increasing importance over time
            position_score += val * weight
    
    # Secondary filter: outlier detection via quartiles (distractor)
    sorted_vals = sorted(v for v in data if v > 0)
    n = len(sorted_vals)
    if n >= 4:
        q1 = sorted_vals[n//4]
        q3 = sorted_vals[3*n//4]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outlier_count = sum(1 for v in data if v > 0 and (v < lower_bound or v > upper_bound))
    else:
        outlier_count = -1
    
    # Final computation: combine position score with signal diversity
    diversity_bonus = len(signal_set) * 2.5
    final_score = position_score + diversity_bonus
    
    # Tertiary adjustment based on threshold coverage
    covered_thresholds = sum(1 for i, t in thresholds.items() if i < len(data) and data[i] > 0)
    if covered_thresholds >= len(thresholds) * 0.6:
        final_score *= 1.1
    
    return round(final_score, 3)

# Execute critical statement
current_buffer_state = buffer_cache[1][:]
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")