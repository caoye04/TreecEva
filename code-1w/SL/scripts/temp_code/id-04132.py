import math

# Simulated sensor data stream with noise and calibration offsets
data_stream = [0.7, 1.2, 3.1, -0.4, 2.8, 5.0, 1.9, 0.0, 4.4, -1.1]

# Irrelevant calibration constants (distractors)
CALIBRATION_OFFSET_A = 0.023
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 128
TEMPORAL_DRIFT = 0.001

# Decoy functions that are defined but not used in the main logic
def analyze_coherence(signal):
    return sum([abs(x) ** 1.5 for x in signal]) / len(signal)

def compute_entropy(data):
    return -sum(p * math.log(p) for p in data if p > 0)

def normalize_signal(x):
    return (x + 1) / 2 if x < 1 else x / 2

# Core processing pipeline
scale_factor = 1.5
gain_stages = [0.8, 1.1, 1.0, 0.9]

# Noise threshold computed via irrelevant statistical moment (red herring)
moment_3 = sum((x - sum(data_stream)/len(data_stream))**3 for x in data_stream) / len(data_stream)
noise_threshold = abs(moment_3) * scale_factor

# Filter design parameters (some are decoys)
cutoff_frequency = 2.5
filter_order = 4
attenuation_db = 40
phase_shift = 0.125

# Lambda-based dynamic filter gate (actual relevant code)
adaptive_gate = lambda x: abs(x) > 0.5

# Signal conditioning chain
def apply_gain(signal, stage_multiplier):
    return [x * stage_multiplier for x in signal]

def mask_transient_noise(signal, threshold):
    return [x if abs(x) > threshold else 0.0 for x in signal]

def fold_signal(signal):
    return [abs(x) for x in signal]

def integrate_and_clip(signal):
    integrated = 0
    result = []
    for val in signal:
        integrated += val
        result.append(min(integrated, 5.0))
    return result

# Actual processing sequence (key path)
def process_sequence(input_data):
    # Step 1: Apply gain staging
    staged = apply_gain(input_data, gain_stages[2])
    
    # Step 2: Fold negative components
    folded = fold_signal(staged)
    
    # Step 3: Dynamic adaptive filtering
    filtered = [x for x in folded if adaptive_gate(x)]
    
    # Step 4: Mask residual low-amplitude noise
    cleaned = mask_transient_noise(filtered, noise_threshold * 0.7)
    
    # Step 5: Integrate and clip
    output = integrate_and_clip(cleaned)
    
    # Dead code branch - never executed (distractor)
    if len(output) > 100:
        fallback = [x * phase_shift for x in output]
        return fallback
    
    return output

# Validation logic with comparison operations and tuple unpacking
def validate_purity(signal_chunk):
    if not signal_chunk:
        return 0.0
    
    # Compute multiple metrics (only one is actually used)
    peak_val = max(signal_chunk)
    avg_val = sum(signal_chunk) / len(signal_chunk)
    variance = sum((x - avg_val) ** 2 for x in signal_chunk) / len(signal_chunk)
    normalized_energy = sum(x**2 for x in signal_chunk) / len(signal_chunk)
    
    # Tuple unpacking with dummy placeholder (real computation)
    (energy, length) = (normalized_energy, len(signal_chunk))
    
    # Complex conditional with short-circuit evaluation (relevant)
    quality_flag = (energy > 1.0) and (length >= 3) or (peak_val > 2.5)
    
    # Redundant bit manipulation on float (misleading, no effect)
    fake_digital_signature = int(avg_val * 100) ^ int(variance * 10)
    
    # Final score calculation — only this matters
    base_score = energy * 100
    adjustment = 10 if quality_flag else -5
    
    # Multiple assignment distraction
    temp_min, temp_max = min(signal_chunk), max(signal_chunk)
    range_ratio = temp_min / (temp_max + 1e-8)
    
    # Irrelevant trigonometric transformation (dead-end)
    angular_projection = math.sin(avg_val) + math.cos(variance)
    
    # The actual answer-determining expression
    return base_score + adjustment

# Execution point of interest
filtration_score = validate_purity(process_sequence(data_stream))

# Print final result
print(f"Target result: {filtration_score}")