import math

# Simulated sensor array diagnostics with signal processing
raw_data_points = [12, 15, 23, 45, 67, 89, 101, 110, 115, 120]
baseline_offset = 10
noise_floor = 3
amplification_factor = 2.5

# Irrelevant calibration constants (distractors)
calibration_a = 0.987
reference_potential = 220
temperature_compensation = -0.05
voltage_regulation = 1.02

# Step 1: Apply baseline correction and noise filtering
corrected_signals = [x - baseline_offset for x in raw_data_points if (x - baseline_offset) > noise_floor]

# Step 2: Amplify relevant signals
amplified_signals = [val * amplification_factor for val in corrected_signals]

# Step 3: Compute rolling average over 3-point window (used later)
def rolling_average(data, window=3):
    if len(data) < window:
        return [0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

# Step 4: Detect peaks above dynamic threshold
dynamic_threshold = sum(amplified_signals) / len(amplified_signals) * 1.2
peak_indices = [i for i, val in enumerate(amplified_signals) if val > dynamic_threshold]

# Step 5: Transform peak regions into diagnostic features
peak_regions = [amplified_signals[i-1:i+2] for i in peak_indices if i > 0 and i < len(amplified_signals)-1]
flattened_peaks = [item for sublist in peak_regions for item in sublist]

# Step 6: Normalize peak values using logarithmic scale
normalized_peaks = [math.log(val) if val > 0 else 0 for val in flattened_peaks]

# Step 7: Compute entropy-like measure of signal disorder
total_energy = sum([x**2 for x in normalized_peaks])
probabilities = [(x**2) / total_energy for x in normalized_peaks] if total_energy > 0 else [0]*len(normalized_peaks)
signal_entropy = -sum([p * math.log(p) for p in probabilities if p > 0])

# Step 8: Process signals through dummy transformation chain (unused path - red herring)
shadow_buffer = []
for x in amplified_signals:
    temp = x * 0.9
    temp -= 1.1
    temp = max(temp, 0)
    shadow_buffer.append(int(temp))  # Dead path - never used again

# Step 9: Destructuring assignment to extract key waveform characteristics
if len(rolling_average(amplified_signals)) >= 3:
    first_avg, *middle_avgs, last_avg = rolling_average(amplified_signals)
else:
    first_avg, last_avg = 0, 0

# Step 10: Simulate recursive harmonic analysis (only called if condition met)
def compute_harmonic_depth(signal_part, depth=0):
    if not signal_part or depth >= 3:
        return depth
    split_point = len(signal_part) // 2
    left_half = signal_part[:split_point]
    right_half = signal_part[split_point:]
    return compute_harmonic_depth(left_half, depth + 1)

# Recursive call only on specific subset
harmonic_diagnostic = compute_harmonic_depth(flattened_peaks[:5])

# Step 11: Final signal processing pipeline
processed_signals = {
    'entropy': round(signal_entropy, 4),
    'peaks': len(peak_indices),
    'amplitude': max(amplified_signals) if amplified_signals else 0,
    'stability': last_avg - first_avg,
    'complexity': harmonic_diagnostic
}

# Step 12: Analyze readings to produce final diagnostic score
def analyze_readings(data_dict):
    # Multiple factors contribute nonlinearly
    base_score = data_dict['entropy'] * 100
    peak_bonus = data_dict['peaks'] * 15
    stability_penalty = abs(data_dict['stability']) * 2
    complexity_multiplier = 1 + (data_dict['complexity'] * 0.25)
    
    # Final computation
    raw_diagnostic = (base_score + peak_bonus - stability_penalty) * complexity_multiplier
    
    # Red herring computation (looks important but unused)
    theoretical_max = 300 + (data_dict['complexity'] ** 3) * 10
    efficiency_ratio = raw_diagnostic / theoretical_max if theoretical_max > 0 else 0
    
    return int(round(raw_diagnostic))

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")