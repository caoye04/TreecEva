import itertools

# Simulated bio-signal processing pipeline for neural diagnostics

# Core signal parameters (relevant)
def generate_waveform(baseline, harmonics):
    return lambda t: baseline + sum((i+1) * 0.5 * (t % (2**(4-i))) for i in range(harmonics) if t % (2**(3-i)) != 0)

# Irrelevant helper - visual artifact generator (distraction)
def generate_pattern(n):
    seq = [0, 1]
    for _ in range(n-2):
        seq.append(seq[-1] + seq[-2])
    return [x % 7 for x in seq]

# Data normalization (relevant but complex path)
def normalize(signal, ref_range):
    raw_min, raw_max = min(signal), max(signal)
    norm_factor = ref_range[1] - ref_range[0]
    return [(x - raw_min) / (raw_max - raw_min) * norm_factor + ref_range[0] for x in signal]

# Decoy function - unused in final flow (dead code path)
def legacy_calibrate(x):
    return (x * 3.14159) % 256

# Signal coherence validator (used indirectly)
def is_coherent(stream, tolerance=0.15):
    diffs = [abs(stream[i+1] - stream[i]) for i in range(len(stream)-1)]
    avg_change = sum(diffs) / len(diffs)
    return all(abs(d - avg_change) < tolerance * avg_change for d in diffs)

# Main diagnostic processor (critical path)
def process_metrics(signature, thresholds):
    # Step 1: Extract frequency envelope
    envelope = [abs(x * 0.85) for x in signature if x > -1.0]
    
    # Step 2: Compute harmonic distortion index
    hdi = sum((envelope[i] - envelope[i-1])**2 for i in range(1, len(envelope))) / len(envelope)
    
    # Step 3: Apply dynamic thresholding
    t_key = tuple(sorted(thresholds.keys()))
    t_val = [thresholds[k] for k in t_key]
    adjusted = hdi * (t_val[0] * 0.7 + t_val[1] * 0.3) if len(t_val) >= 2 else hdi
n    
    # Step 4: Noise floor correction
    noise_floor = 0.231
    corrected = max(adjusted - noise_floor, 0.0)
    
    # Step 5: Final quantization (answer derived here)
    return int(corrected * 10000) / 100.0  # Two decimal precision

# Irrelevant artifact: spatial mapping grid (distractor)
spatial_grid = [[(i*j + i**2) % 19 for j in range(6)] for i in range(6)]
grid_hash = sum(spatial_grid[i][i] for i in range(6)) * 0.001

# Generate time domain samples (key input generation)
time_points = list(range(1, 17))
signal_fn = generate_waveform(baseline=0.42, harmonics=4)
raw_signal = [signal_fn(t) for t in time_points]

# Normalize to diagnostic range (relevant)
normalized_signal = normalize(raw_signal, ref_range=[-1.2, 2.1])

# Validate signal quality (used in logic)
valid = is_coherent(normalized_signal, tolerance=0.15)

# Threshold configuration map (critical input)
threshold_map = {
    'alpha': 1.8,
    'beta': 2.4
}

# Conditional override simulation (red herring - not triggered)
if sum(normalized_signal) / len(normalized_signal) < 0.1:
    threshold_map['beta'] *= 1.5  # Unused path

# Generate health signature (actual used data)
health_signature = []
for i, val in enumerate(normalized_signal):
    if i % 3 == 0:
        health_signature.append(val * 0.9)
    elif i % 4 == 0:
        health_signature.append(val * 1.1)
    else:
        health_signature.append(val * 1.0)

# Apply secondary filtering using itertools (relevant: combinatorics)
pairs = list(itertools.combinations([hs for hs in health_signature if hs > 0.5], 2))
if pairs:
    avg_pair = sum(a + b for a, b in pairs[:3]) / (len(pairs[:3]) * 2)
    health_signature.append(avg_pair * 0.7)

# MAIN EXECUTION POINT - critical assignment
final_diagnostic = process_metrics(health_signature, threshold_map)

# Dead code: unused diagnostic chain
redundant_check = any(x > 1.9 for x in normalized_signal)
backup_score = (grid_hash + 42) if redundant_check else 0

# Output target result
print(f"Result: {final_diagnostic}")