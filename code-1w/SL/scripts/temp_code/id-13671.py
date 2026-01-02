import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [14, 28, 19, 42, 35, 71, 63, 55]
baseline_offset = 13
calibration_factor = 2.5

# Irrelevant temperature simulation (red herring)
temp_samples = [21.3, 22.1, 19.8, 23.0, 20.5]
avg_temp = sum(temp_samples) / len(temp_samples)
adjusted_temps = [t * 1.05 for t in temp_samples if t > 20]

def apply_filter(data, threshold):
    # Applies high-pass filter equivalent
    return [x for x in data if x > threshold]

def generate_pairs(seq):
    # Creates overlapping pairs (distractor function - not used in main path)
    return list(itertools.combinations(seq, 2))

def integrate_signal(values, factor):
    # Weighted accumulation with calibration
    acc = 0
    for i, v in enumerate(values):
        acc += (v - baseline_offset) * factor * (0.9 ** i)  # Exponential decay weighting
    return acc

# Signal preprocessing stages
filtered_readings = apply_filter(raw_readings, 20)
sorted_readings = sorted(filtered_readings, reverse=True)

# Frame segmentation (meaningful but partially obfuscated)
frames = []
for i in range(0, len(sorted_readings), 2):
    if i + 1 < len(sorted_readings):
        frames.append((sorted_readings[i], sorted_readings[i+1]))
    else:
        frames.append((sorted_readings[i], 0))

# Extract magnitude features
magnitudes = [a + b for a, b in frames if a > b]

# Decoy statistical analysis (dead code path)
if len(magnitudes) > 10:
    variance = sum((x - sum(magnitudes)/len(magnitudes))**2 for x in magnitudes) / len(magnitudes)
    z_scores = [abs(x - sum(magnitudes)/len(magnitudes)) / (variance**0.5) for x in magnitudes]
else:
    outlier_flags = [False] * len(magnitudes)  # Unused branch

# Real processing begins: transform frames into analyzable units
processed_frames = []
for mag in magnitudes:
    # Apply non-linear transformation
    transformed = int((mag ** 1.5) // calibration_factor)
    if transformed % 2 == 0:
        processed_frames.append(transformed + 3)
    else:
        processed_frames.append(transformed - 2)

# Additional irrelevant set operation (distractor)
unique_mags = set(magnitudes)
duplicate_count = len(magnitudes) - len(unique_mags)

# Conditional expression mix (uses python idiom)
scaling_mode = 'aggressive' if sum(processed_frames) > 300 else 'conservative'
effective_scale = 1.75 if scaling_mode == 'aggressive' else 1.25

# Core integration step (hidden among distractions)
weighted_total = integrate_signal(processed_frames, effective_scale)

# Diagnostic logic with tuple unpacking and comparison chain
status_codes = [(x, 'stable') if x < 150 else (x, 'elevated') for x in processed_frames]
high_alerts = [code for val, code in status_codes if code == 'elevated']

# Final computation path - depends on prior transformations
threshold_set = {x for x in processed_frames if x > 100}

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)

# Supporting function defined late to obscure flow
def analyze_signal(signal_list):
    base = sum(signal_list) // len(signal_list)
    peak = max(signal_list)
    adjustment = len(threshold_set) * 0.8  # Uses outer scope set
    
    # Complex conditional expression combining arithmetic and logic
    modifier = (2.1 if base > 90 else 1.4) + (0.7 if len(signal_list) % 3 == 0 else 0)
    
    # Final result built from multiple reasoning steps
    result = (base * modifier) + (peak / 4) + adjustment
    
    # Additional decoy logic (never reached)
    if result < 0:
        return abs(result) * 1.5
    elif result > 500:
        fallback = sum([x*0.5 for x in signal_list if x%4==0])
        return fallback  # Not triggered
    
    return result

# Print required result
Target result: {final_diagnostic}