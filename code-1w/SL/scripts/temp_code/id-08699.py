from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing pipeline
raw_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
noise_floor = 2
calibration_offset = 0.7

# Irrelevant calibration constants (distractors)
ref_level_abc = 1.03
scale_factor_x9 = 0.987
temp_comp_coef = 0.0021
baseline_drift = 0.05

# Preprocessing step: remove noise and apply offset
cleaned_data = [x - noise_floor + calibration_offset for x in raw_readings if x > noise_floor]

# Misleading transformation path (dead code - never used)
decay_weights = []
for i in range(len(cleaned_data)):
    weight = math.exp(-0.1 * i) * scale_factor_x9
    decay_weights.append(weight)

# Another red herring: frequency analysis on irrelevant metric
frequencies = {}
for val in raw_readings:
    frequencies[val] = frequencies.get(val, 0) + 1

# Distractor: complex but unused statistical calculation
mean_raw = sum(raw_readings) / len(raw_readings)
variance_raw = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
std_dev_raw = math.sqrt(variance_raw)
skewness = sum((x - mean_raw)**3 for x in raw_readings) / (len(raw_readings) * std_dev_raw**3)

# Actual relevant transformation: group by magnitude bands
band_map = defaultdict(int)
for val in cleaned_data:
    band = int(val // 2) * 2  # Group into bands of size 2
    band_map[band] += 1

# Create transformed_data with frequency counts per band
transformed_data = dict(band_map)

# Decoy function that looks important but is unused
def legacy_recalibrate(data, factor=1.0):
    return [x * factor for x in data if x > 3]

# Another decoy: recursive filter not used in main logic
def recursive_denoise(seq, level=0):
    if level >= 2 or len(seq) < 3:
        return seq
    filtered = [seq[i] for i in range(1, len(seq)-1) 
                if abs(seq[i] - (seq[i-1]+seq[i+1])/2) < 1.5]
    return recursive_denoise(filtered, level + 1)

# Build threshold map using only specific bands (core logic)
threshold_map = {}
for band in transformed_data:
    if band >= 4:
        # Threshold depends on squared band divided by count
        thresh = (band ** 2) / (transformed_data[band] + 1)
        threshold_map[band] = round(thresh, 3)

# Secondary processing: derive pattern features
pattern_features = []
for key in sorted(transformed_data.keys()):
    count = transformed_data[key]
    feature_val = (key * count) % 7
    pattern_features.append(feature_val)

# Fake anomaly detection using irrelevant logic (distractor)
anomaly_flags = []
running_avg = 0
for i, feat in enumerate(pattern_features):
    running_avg = (running_avg * 0.8) + (feat * 0.2)
    if abs(feat - running_avg) > 1.1:
        anomaly_flags.append(i)

# Core analysis function that determines final result
def analyze_pattern(data_dict, thresholds):
    total_score = 0
    contribution_log = Counter()
    
    for k, v in data_dict.items():
        if k in thresholds:
            # Scoring based on key-threshold interaction
            raw_contribution = int(v * thresholds[k])
            adjusted = raw_contribution >> 1  # Bit shift as computation
            total_score += adjusted
            contribution_log[k] = adjusted
            
            # Additional logic path with conditional bit operations
            if v >= 3 and k >= 6:
                bonus = (v ^ int(thresholds[k])) & 7  # XOR and mask
                total_score += bonus
    
    # Process log for secondary adjustment
    keys_used = list(contribution_log.keys())
    if len(keys_used) > 2:
        mid_key = keys_used[len(keys_used)//2]
        adjustment = abs(mid_key - 5)
        total_score -= adjustment  # Penalty or bonus depending on midpoint
    
    return total_score + len(contribution_log)  # Final formula

# Execute critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")