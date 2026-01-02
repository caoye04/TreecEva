import math

# Simulated sensor data processing with diagnostic analysis
raw_samples = [i * 0.1 for i in range(1, 101)]
baseline_offset = 42.0
sampling_rate = 100.0

# Irrelevant calibration constants (distractors)
calibration_a = 0.987
reference_phase = 1.5708
max_theoretical_bandwidth = 2000
noise_floor_db = -90.5

temp_buffer = []
filtered_data = set()
sample_magnitudes = tuple()

# Step 1: Apply nonlinear transformation to raw samples
for s in raw_samples:
    if s < 0.5:
        adjusted = math.sin(s * math.pi / 2) * baseline_offset
    elif s > 5.0:
        adjusted = math.log(s) * 10
    else:
        adjusted = s * 15.5
    temp_buffer.append(adjusted)

# Step 2: Filter and normalize (only even-indexed values used)
normalized_samples = []
for idx, val in enumerate(temp_buffer):
    if idx % 2 == 0:
        normalized = abs(val) / 10.0
        if normalized > 1.0:
            normalized = 1.0
        normalized_samples.append(normalized)

# Dead code path - never executed due to prior filtering (red herring)
if len(filtered_data) > 10:
    backup_recalibrate = True
    for x in filtered_data:
        x *= 1.1  # No effect

# Step 3: Quantize normalized values into discrete levels
quantized_levels = []
decoy_accumulator = 0
for val in normalized_samples:
    level = int(val * 63)  # 6-bit quantization
    quantized_levels.append(level)
    # Misleading accumulation (not used later)
    decoy_accumulator += level * 0.01

# Step 4: Compute spectral centroid approximation
spectral_sum = 0.0
magnitude_sum = 0.0
for i, mag in enumerate(quantized_levels):
    frequency_weight = i * sampling_rate / len(quantized_levels)
    weighted_contribution = mag * frequency_weight
    spectral_sum += weighted_contribution
    magnitude_sum += mag

if magnitude_sum > 0:
    spectral_centroid = spectral_sum / magnitude_sum
else:
    spectral_centroid = 0.0

# Step 5: Extract peak characteristics
sorted_levels = sorted(quantized_levels, reverse=True)
top_peak = sorted_levels[0] if sorted_levels else 0
second_peak = sorted_levels[1] if len(sorted_levels) > 1 else 0
peak_ratio = (second_peak / top_peak) if top_peak != 0 else 0

# Step 6: Generate harmonic distortion estimate (irrelevant computation)
harmonic_energy = 0.0
for i in range(2, 6):
    if i * 5 < len(quantized_levels):
        harmonic_energy += quantized_levels[i * 5] ** 2
rms_harmonic = math.sqrt(harmonic_energy / 4) if harmonic_energy > 0 else 0

# Step 7: Process samples through diagnostic pipeline
def process_noise_profile(levels):
    total_energy = sum([x*x for x in levels])
    avg_energy = total_energy / len(levels) if levels else 0
    return avg_energy * 0.05

# Unused function - distractor
def legacy_calibration(x):
    return (x * 0.87) + 5.2

# Step 8: Main signal processing
processed_samples = []
for lv in quantized_levels:
    # Nonlinear companding
    if lv > 32:
        compressed = 32 + math.sqrt(lv - 32)
    else:
        compressed = lv * 0.9
    processed_samples.append(int(compressed))

# Step 9: Diagnostic analysis function
def analyze_signal(signal):
    if not signal:
        return 0.0
    
    # Compute RMS of signal
    rms = math.sqrt(sum([x*x for x in signal]) / len(signal))
    
    # Count zero-crossings (conceptually irrelevant here)
    zero_crossings = 0
    for i in range(1, len(signal)):
        if (signal[i-1] < 30) != (signal[i] < 30):  # arbitrary threshold
            zero_crossings += 1
    
    # Primary diagnostic metric: weighted combination
    length_factor = len(signal) / 100.0
    peak_val = max(signal) if signal else 0
    
    # Key formula - determines final result
    diagnostic_score = (rms * 2.3) + (peak_val * 0.7) + (length_factor * 10)
    
    # Conditional adjustment based on signal characteristics
    adjustment = 5.0 if rms > 20 else -3.5
    
    # Final diagnostic with conditional expression
    return diagnostic_score + adjustment if zero_crossings > 10 else diagnostic_score - 1.5

# Step 10: Execute key statement
final_diagnostic = analyze_signal(processed_samples)

# Print result as required
print(f"Target result: {final_diagnostic}")