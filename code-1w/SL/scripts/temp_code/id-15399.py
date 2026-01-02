def preprocess_records(raw_logs):
    cleaned = {}
    for key, val in raw_logs.items():
        if isinstance(val, str):
            cleaned[key] = val.strip().lower().replace(' ', '_')
        else:
            cleaned[key] = val * 0.95  # minor adjustment
    return cleaned

# Irrelevant function - decoy for data sanitization
def sanitize_input(data):
    if isinstance(data, dict):
        return {k: str(v).upper() for k, v in data.items()}
    return data

# Misleading transformation chain
def transform_metrics(metrics):
    temp = {}
    for k, v in metrics.items():
        if 'temp' in k:
            temp[k] = v + 273.15  # Kelvin conversion (unused later)
        elif 'pressure' in k:
            temp[k] = v * 0.145  # psi conversion (dead path)
    return temp

# Unused recursive helper - red herring
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Simulates environmental factors (distractor)
def compute_microclimate_score(factors):
    score = 0
    for f in factors:
        if f > 10:
            score += f * 0.3
        else:
            score += f * 0.1
    return round(score, 2)

# Core logic disguised among noise
regional_data = {
    'zone_a': [120, 150, 130],
    'zone_b': [80, 90],
    'zone_c': [200, 180, 190, 170]
}

threshold_map = {
    'zone_a': 135,
    'zone_b': 85,
    'zone_c': 185
}

auxiliary_config = {
    'calibration_factor': 0.92,
    'tolerance': 5,
    'debug_mode': True
}

# Fake data processing pipeline
staged_buffers = []
for zone, values in regional_data.items():
    avg_val = sum(values) / len(values)
    staged_buffers.append(f'{zone}: {avg_val:.1f}')

# Real but non-obvious core function
def calculate_harvest(zones, thresholds):
    total_yield = 0
    adjustment_factor = auxiliary_config['calibration_factor']
    
    # Iterate over each zone and apply conditional filtering
    for zone, readings in zones.items():
        threshold = thresholds[zone]
        above_threshold = [r for r in readings if r >= threshold]
        below_threshold = [r for r in readings if r < threshold]
        
        # Only above-threshold values contribute to final yield
        zone_base = sum(above_threshold)
        
        # Conditional bonus logic (bit manipulation distraction)
        bonus_flag = len(above_threshold) > len(below_threshold)
        bonus_modifier = 1.1 if bonus_flag else 1.0
        
        # Case conversion on string version (irrelevant but plausible)
        flag_str = str(bonus_flag).upper()
        flag_len = len(flag_str)  # distractor
        
        # Actual contribution
        zone_contribution = zone_base * bonus_modifier * adjustment_factor
        total_yield += zone_contribution
        
        # Dead assignment with misleading name
        peak_ratio = max(readings) / min(readings) if min(readings) > 0 else 1.0
        
    # Final nonlinear adjustment based on number of zones
    num_zones = len(zones)
    if num_zones == 3:
        total_yield = int(total_yield // 1)  # integer division
    else:
        total_yield = round(total_yield, 2)
    
    return total_yield

# Secondary fake aggregation
aggregated_diagnostics = []
for log_entry in staged_buffers:
    parts = log_entry.split(': ')
    try:
        val = float(parts[1])
        if val > 100:
            aggregated_diagnostics.append(f"HIGH:{parts[0]}")
    except:
        continue

# Critical execution point
final_yield = calculate_harvest(regional_data, threshold_map)

# Print result as required
print(f"Result: {final_yield}")