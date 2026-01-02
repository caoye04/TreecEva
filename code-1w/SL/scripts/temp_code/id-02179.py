from collections import defaultdict

# Simulate sensor phase readings over time with noise filtering
def filter_noisy_readings(readings):
    filtered = []
    for i, val in enumerate(readings):
        if i == 0:
            filtered.append(val)
        else:
            diff = abs(val - filtered[-1])
            if diff < 30:  # Arbitrary noise threshold
                filtered.append(val)
            else:
                corrected = filtered[-1] + (val - filtered[-1]) * 0.3
                filtered.append(round(corrected))
    return filtered

# Apply weighted transformation to phase components
def apply_transform(components, factor):
    transformed = []
    temp_store = defaultdict(float)
    for idx, comp in enumerate(components):
        temp_val = comp * factor * (idx + 1)
        temp_store[f'temp_{idx}'] = temp_val
        transformed.append(temp_val + 5)  # Artificial offset
    # Unused computation - red herring
    cumulative = sum(temp_store[k] for k in temp_store if 'temp_' in k)
    scaling_factor = len(transformed) / (cumulative + 1e-5)
    return [x * scaling_factor for x in transformed]

# Main processing function combining multiple logic chains
def process_phases(phases, weights):
    adjusted = []
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Distractor: Precompute squared deviations (not used later)
    mean_phase = sum(phases) / len(phases)
    deviations = [(p - mean_phase)**2 for p in phases]
    variance_estimate = sum(deviations) / len(deviations) if deviations else 0
    
    # Real logic: Weighted phase shift accumulation
    shifted = [phases[i] * normalized_weights[i] for i in range(len(phases))]
    compensated = [s * 1.5 for s in shifted]  # System gain compensation
    
    # Introduce auxiliary transformation (only final sum matters)
    enhanced = apply_transform(compensated, 0.8)
    
    # Accumulate net effect through conditional adjustments
    accumulator = 0
    for val in enhanced:
        if val > 10:
            accumulator += val * 0.7
        elif val > 0:
            accumulator += val * 0.4
        else:
            accumulator -= abs(val) * 0.2
    
    # Final integration step
    adjustment = accumulator / len(enhanced)
    return adjustment

# Sensor data simulation (in degrees)
raw_phase_input = [120, -45, 90, 180, -135, 60]
noise_filtered = filter_noisy_readings(raw_phase_input)

# Frequency channel weights (arbitrary calibration values)
channel_weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.15]

# Phase alignment tuples from reference grid
alignment_pairs = list(zip(noise_filtered, [x % 90 for x in noise_filtered]))
index_map = {i: v[0] for i, v in enumerate(alignment_pairs)}

# Secondary validation check (unused in final result)
valid_count = 0
for idx, (orig, aligned) in enumerate(alignment_pairs):
    if orig - aligned > 30:
        valid_count += 1

# Weight redistribution based on signal strength (distractor logic)
redistributed = [w + 0.02 for w in channel_weights]
total_redist = sum(redistributed)
norm_redist = [r / total_redist for r in redistributed]

# Core execution
phase_data = [x * 0.95 for x in noise_filtered]  # Minor calibration
weights = channel_weights
final_adjustment = process_phases(phase_data, weights)

# Key derived variable
net_phase_shift = round(final_adjustment + 17.5, 2)

# Intermediate diagnostics (irrelevant to answer)
diagnostics = []
for i, val in enumerate(noise_filtered):
    zipped = list(zip([val]*3, norm_redist[:3]))
    avg_zip = sum(a*b for a,b in zipped) / len(zipped)
    diagnostics.append(avg_zip)

print(f"Result: {net_phase_shift}")