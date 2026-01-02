import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_values = [23.7, 19.1, 45.6, 30.2, 51.8, 28.9, 37.4, 40.0]
    scale_factor = 1.08
    adjusted = [v * scale_factor for v in raw_values]
    return adjusted

# Irrelevant helper - dead code path (red herring)
def deprecated_filter(x):
    return [i for i in x if i > 30]  # Unused in logic

# Signal processing pipeline
def clean_noise(data, level=1.05):
    cleaned = []
    for val in data:
        if val < 25.0:
            cleaned.append(val * level)
        elif val > 40.0:
            cleaned.append(val * (level - 0.02))
        else:
            cleaned.append(val)
    return cleaned

# Bit manipulation for checksum (distractor)
def compute_legacy_checksum(arr):
    total = 0
    for num in arr:
        shifted = int(num) << 2
        total ^= shifted & 0xFFFF
    return total % 1000  # Not used in final result

# Data transformation using string methods (required feature)
def encode_metrics(values):
    labels = []
    for v in values:
        tag = f"M{int(v * 3.1)}"
        tag = tag.replace('0', 'X').zfill(5)  # String manipulation distractor
        labels.append(tag)
    return labels  # Never consumed

# Core analysis function
def generate_threshold_map(config_level):
    base_map = {}
    for i in range(8):
        key = f"sensor_{i}"
        # Complex threshold formula with unused branches
        if i % 4 == 0:
            base_map[key] = 30.5 + config_level * 0.7
        elif i % 3 == 0:
            base_map[key] = 28.9 + config_level * 0.3
        else:
            base_map[key] = 32.1 - (config_level * 0.2)
    return base_map

# Main diagnostic engine
def analyze_signal(data, thresholds):
    diagnostics = []
    for i, val in enumerate(data):
        t_val = thresholds.get(f"sensor_{i}", 30.0)
        if val > t_val:
            diagnostics.append(1)
        else:
            diagnostics.append(0)
    
    # Multi-step reduction logic
    count_above = sum(diagnostics)
    ratio = count_above / len(diagnostics)
    weighted_score = ratio * 100
    
    # Secondary adjustment based on pattern
    pattern_sum = 0
    for j in range(1, len(diagnostics)):
        if diagnostics[j] != diagnostics[j-1]:
            pattern_sum += 1
    
    stability_penalty = pattern_sum * 1.5
    adjusted_score = weighted_score - stability_penalty
    
    # Final non-linear transformation
    if adjusted_score > 50:
        final = math.log(adjusted_score) * 12.4
    else:
        final = math.sqrt(adjusted_score) * 8.7
    
    return round(final, 4)

# === START OF EXECUTION ===
sensor_data = collect_sensor_readings()
processed_data = clean_noise(sensor_data, level=1.05)

# Distractor variables and operations
checksum = compute_legacy_checksum(processed_data)  # Red herring
encoded_tags = encode_metrics(processed_data)       # Dead end
aux_data = [x for x in processed_data if x > 35]   # Unused subset

config_preset = "HIGH"
level_modifier = 2.0 if config_preset == "HIGH" else 1.0
threshold_map = generate_threshold_map(level_modifier)

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")