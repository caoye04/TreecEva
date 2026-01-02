import math

# Simulated sensor array data (real values)
sensor_readings = [145.7, 160.3, 138.9, 172.1, 150.5, 158.2, 147.8, 163.4]

def apply_calibration(data, factor=1.05):
    # Applies physical calibration factor (benign transformation)
    return [x * factor for x in data]

def compute_entropy(values):
    # Calculates Shannon entropy of distribution (distractor)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def detect_spikes(signal, window=3):
    # Identifies transient spikes using moving max (irrelevant to final result)
    spikes = []
    for i in range(len(signal)):
        left = max(0, i - window//2)
        right = min(len(signal), i + window//2 + 1)
        window_max = max(signal[left:right])
        if signal[i] == window_max and signal[i] > 155:
            spikes.append(i)
    return spikes

def generate_baseline(count, base=140, variation=5):
    # Generates synthetic baseline (dead code path)
    import random
    random.seed(42)
    return [base + random.uniform(-variation, variation) for _ in range(count)]

def normalize_range(data, new_min=0, new_max=1):
    old_min, old_max = min(data), max(data)
    if old_min == old_max:
        return [0 for _ in data]
    return [(x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for x in data]

def evaluate_stability(indices, metric='index'):
    # Analyzes index patterns (misleading intermediate)
    if len(indices) < 2:
        return 0.0
    diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    return sum(diffs) / len(diffs)

def extract_features(series, mode='magnitude'):
    # Extracts various statistical features (red herring)
    features = {
        'mean': sum(series) / len(series),
        'variance': sum((x - sum(series)/len(series))**2 for x in series) / len(series),
        'skew': 0,  # Simplified
        'peaks': len([x for x in series if x > 155])
    }
    return features

def calculate_risk_score(value, exposure=1.0):
    # Business logic unrelated to core computation (distractor)
    tiers = [(100, 0.1), (130, 0.25), (150, 0.6), (160, 0.85), (float('inf'), 1.0)]
    for limit, score in tiers:
        if value <= limit:
            return score * exposure
    return 1.0

def filter_outliers(data, k=1.5):
    # IQR-based filtering (not actually used in main pipeline)
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def aggregate_by_quartile(data):
    # Divides data into quartiles and aggregates (unused structure)
    sorted_vals = sorted(data)
    n = len(sorted_vals)
    q1 = sorted_vals[n//4]
    q2 = sorted_vals[n//2]
    q3 = sorted_vals[3*n//4]
    groups = {
        'Q1': [x for x in data if x <= q1],
        'Q2': [x for x in data if q1 < x <= q2],
        'Q3': [x for x in data if q2 < x <= q3],
        'Q4': [x for x in data if x > q3]
    }
    return {k: sum(v)/len(v) if v else 0 for k, v in groups.items()}

def derive_adjustment_factor(timestamp_sequence):
    # Temporal adjustment based on fake timestamps (decoy)
    if not timestamp_sequence:
        return 1.0
    avg_ts = sum(timestamp_sequence) / len(timestamp_sequence)
    return math.sin(avg_ts * 0.01) + 1.0

def validate_consistency(pattern):
    # Checks monotonicity (false trail)
    return all(pattern[i] <= pattern[i+1] for i in range(len(pattern)-1))

def slice_and_shift(data, start=1, end=-1, shift=2):
    # Performs slicing and circular shift (partially relevant)
    segment = data[start:end]
    if not segment:
        return data
    shifted = segment[-shift:] + segment[:-shift]
    return shifted

def compute_weighted_sum(components, weights=None):
    # Final aggregation method (critical)
    if weights is None:
        weights = [0.3, 0.2, 0.2, 0.1, 0.1, 0.05, 0.05]
        weights = weights[:len(components)]
    return sum(comp * wgt for comp, wgt in zip(components, weights))

def build_threshold_map(config_level=3):
    # Creates mapping of thresholds (used in final step)
    templates = {
        1: {'low': 0.2, 'medium': 0.5, 'high': 0.7},
        2: {'low': 0.18, 'medium': 0.45, 'high': 0.68},
        3: {'low': 0.15, 'medium': 0.4, 'high': 0.65},
        4: {'low': 0.12, 'medium': 0.35, 'high': 0.6}
    }
    return templates.get(config_level, templates[3])

def process_metrics(data_vector, thresholds):
    # Core diagnostic processor (target function)
    magnitude = sum(abs(x) for x in data_vector)
    normalized_mags = [abs(x) / magnitude for x in data_vector]
    
    # Apply non-linear transformation
    transformed = [math.tanh(x * 5) for x in normalized_mags]
    
    # Slice operation used meaningfully
    mid_section = transformed[1:-1]  # Exclude first and last
    
    # Compute multiple candidate scores (only one matters)
    score_a = sum(transformed) * 100
    score_b = sum(mid_section) * 120
    score_c = compute_weighted_sum(mid_section) * 150  # This one is selected below
    
    # Conditional selection based on threshold (key logic)
    if transformed[0] > thresholds['medium']:
        selected_score = score_a
    elif len(mid_section) > 5:
        selected_score = score_b
    else:
        selected_score = score_c
    
    # Final adjustment using bit manipulation (unexpected but deterministic)
    raw_value = int(selected_score)
    adjusted = (raw_value ^ 0xAA) & 0xFFFF  # Bitwise XOR and mask
    if adjusted > 32767:
        adjusted -= 65536
    
    return adjusted

# --- MAIN EXECUTION FLOW ---

# Step 1: Raw sensor input
raw_data = sensor_readings

# Step 2: Apply calibration (relevant)
calibrated_data = apply_calibration(raw_data)

# Step 3: Normalize to [0,1] range (relevant)
normalized_data = normalize_range(calibrated_data)

# Step 4: Detect anomalies (distractor call)
anomaly_indices = detect_spikes(calibrated_data)

# Step 5: Evaluate stability of anomalies (irrelevant chain)
stability_metric = evaluate_stability(anomaly_indices)

# Step 6: Extract statistical features (red herring)
feature_set = extract_features(calibrated_data)

# Step 7: Generate unused baseline for comparison
dummy_baseline = generate_baseline(len(raw_data))

# Step 8: Compute entropy (distractor only)
data_entropy = compute_entropy(calibrated_data)

# Step 9: Build actual threshold configuration (used later)
threshold_map = build_threshold_map(config_level=3)

# Step 10: Filter outliers (result ignored)
filtered_data = filter_outliers(calibrated_data)

# Step 11: Aggregate by quartile (unused analysis)
quartile_averages = aggregate_by_quartile(calibrated_data)

# Step 12: Derive temporal factor (fake dependency)
timestamps = [1623456000 + i*3600 for i in range(len(raw_data))]
temporal_factor = derive_adjustment_factor(timestamps)

# Step 13: Validate consistency on normalized slice (false path)
consistency_check = validate_consistency(normalized_data[::2])

# Step 14: Perform slicing and shifting (partial relevance)
shifted_slice = slice_and_shift(normalized_data, start=1, end=-1, shift=2)

# Step 15: Recompute normalization on shifted data (misleading)
re_normalized = normalize_range(shifted_slice + [0.1])

# Step 16: Calculate risk scores for each reading (irrelevant)
risk_profile = [calculate_risk_score(x) for x in calibrated_data]

# Step 17: Final diagnostic processing (KEY STEP)
final_diagnostic = process_metrics(normalized_data, threshold_map)

# Output target variable
print(f"Result: {final_diagnostic}")