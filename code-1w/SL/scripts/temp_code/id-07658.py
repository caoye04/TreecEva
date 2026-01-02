import math

# Simulated sensor network data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 80, 96, 112, 240]
    scaling_factor = 0.75
    adjusted = [r * scaling_factor for r in raw_readings]
    return adjusted

def filter_outliers(data, limit=200):
    # Irrelevant filtering (never triggered due to scaling)
    return [x for x in data if x < limit]

def generate_lookup():
    # Distractor: generates unused mapping
    return {i: math.sin(i) for i in range(10)}

def compute_checksum(sequence):
    # Unused cryptographic-style checksum (red herring)
    chk = 0
    for val in sequence:
        chk ^= int(val) & 0xFF
    return chk + 1000  # Decoy value

def temperature_compensation(value, temp=25):
    # Irrelevant compensation function (not used in critical path)
    factor = 1 + (temp - 20) * 0.01
    return value * factor

def extract_critical_band(data):
    # Extracts middle quartile values (relevant only for misdirection)
    sorted_vals = sorted(data)
    n = len(sorted_vals)
    return sorted_vals[n//4 : 3*n//4]

def rolling_average(series, window=3):
    # Dead code path — not used in final calculation
    averages = []
    for i in range(len(series) - window + 1):
        avg = sum(series[i:i+window]) / window
        averages.append(avg)
    return averages

def map_severity_level(value):
    if value < 70:
        return 'LOW'
    elif value < 120:
        return 'MEDIUM'
    else:
        return 'HIGH'

def build_diagnostic_profile(readings):
    # Complex but partially irrelevant profile builder
    profile = {}
    for i, val in enumerate(readings):
        key = f"sensor_{i}"
        profile[key] = {
            'raw_value': val,
            'severity': map_severity_level(val),
            'flagged': val > 100,
            'aux': (val * 1.5) % 42  # Red herring field
        }
    return profile

def calculate_entropy(data):
    # Distractor metric: information entropy (not used)
    total = sum(data)
    probabilities = [v / total for v in data]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

def normalize_dataset(data):
    # Used in processing chain
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def aggregate_metrics(norm_data, labels):
    # Combines normalized data with index weights
    weighted_sum = 0.0
    for idx, (val, lbl) in enumerate(zip(norm_data, labels)):
        weight = idx * 0.1
        contribution = val * weight * (1 + (lbl.count('HIGH') - 0.5))
        weighted_sum += contribution
    return weighted_sum * 100

def derive_threshold_map(norm_values):
    # Creates threshold map using slicing and indexing
    thresholds = {}
    segments = [norm_values[:4], norm_values[4:]]
    for i, seg in enumerate(segments):
        seg_key = f"band_{i}"
        thresholds[seg_key] = {
            'mean': sum(seg) / len(seg),
            'active_count': len([x for x in seg if x > 0.5]),
            'index_offset': i * 4
        }
    return thresholds

def analyze_readings(processed, threshold_map):
    # Final analysis using dictionary lookup and enumeration
    score = 0
    base_ref = threshold_map['band_0']['mean']
    
    for i, val in enumerate(processed):
        band_key = 'band_0' if i < 4 else 'band_1'
        band_info = threshold_map[band_key]
        offset = band_info['index_offset']
        
        # Key logic step: conditional accumulation
        if val > band_info['mean']:
            adjustment = abs(i - offset) * 0.1
            score += math.cos(val) ** 2 + adjustment
    
    # Final transformation
    final_score = int((score * 1000) + 0.5)
    
    # Introduce decoy intermediate
    decoy_result = sum(int(x * 10) for x in processed[:3]) * 7
    
    return final_score

# --- Main Execution ---
if __name__ == "__main__":
    readings = collect_sensor_readings()          # Step 1: Initial collection
    filtered = filter_outliers(readings)           # Step 2: Irrelevant filter (no effect)
    compensated = [temperature_compensation(r) for r in readings]  # Step 3: Dead path
    processed_data = normalize_dataset(readings)    # Step 4: Relevant normalization
    
    # Unused operations (distractors)
    rolled = rolling_average(readings, 2)                         # Dead code
    entropy = calculate_entropy(processed_data)                   # Red herring
    checksum = compute_checksum([int(r) for r in readings])       # Misleading numeric
    
    # Critical path continues...
    severity_labels = [map_severity_level(r * 1.2) for r in readings]  # Step 5
    diagnostic_profile = build_diagnostic_profile(readings)             # Step 6
    threshold_map = derive_threshold_map(processed_data)                # Step 7
    final_diagnostic = analyze_readings(processed_data, threshold_map)  # Step 8
    
    # Print required result
    print(f"Target result: {final_diagnostic}")