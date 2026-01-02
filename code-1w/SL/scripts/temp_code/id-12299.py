import math

# Simulated sensor array data (irrelevant initial setup)
raw_readings = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
scale_factor = 2.5
dummy_offset = sum([x ** 0.5 for x in raw_readings]) / len(raw_readings)  # Unused computation

# Irrelevant transformation chain
shifted_values = [math.sin(x * scale_factor) for x in raw_readings]
filtered_noise = list(map(lambda x: abs(x) if x < 0.5 else 0, shifted_values))
aggregated_noise = sum(filtered_noise)  # Dead-end variable

# Real processing begins: frequency envelope extraction
def extract_envelope(signal):
    envelope = []
    for i in range(1, len(signal) - 1):
        prev, curr, next_val = signal[i-1], signal[i], signal[i+1]
        slope_rise = curr - prev
        slope_fall = next_val - curr
        if slope_rise > 0 and slope_fall <= 0:
            envelope.append(curr)
    return envelope

envelope_peaks = extract_envelope(raw_readings)
peak_magnitudes = [p * 10 for p in envelope_peaks]  # Amplify for analysis

# Generate control thresholds (partly irrelevant)
baseline = 5.0
threshold_map = {level: baseline * (1.2 ** level) for level in range(5)}
thresh_copy = threshold_map.copy()  # Distractor
unused_adjustment = {k: v * 0.95 for k, v in thresh_copy.items()}  # More red herring

# Data windowing with slicing - relevant operation
windowed_data = peak_magnitudes[1:-1]  # Remove edge outliers using slice
expanded_data = windowed_data + [windowed_data[-1] * 1.1]  # Slight augmentation

# Conditional data correction based on magnitude class
adjusted_data = []
for val in expanded_data:
    category = 3 if val > 15 else (2 if val > 10 else 1)
    correction = threshold_map[category] * 0.1 if category > 1 else 0
    adjusted_data.append(val - correction if val > 12 else val + 1)

processed_data = [round(x, 2) for x in adjusted_data]  # Final processed input

# Decoy analysis function
def legacy_analysis(data):
    return sum([d ** 2 for d in data]) / 1000  # Unused path

legacy_score = legacy_analysis(processed_data)  # Misleading intermediate result

# Core diagnostic engine
valid_levels = set(range(1, 6))
def analyze_signal(data, thresholds):
    total_weight = 0.0
    contribution_log = []  # For debugging only

    for idx, reading in enumerate(data):
        # Determine impact tier using conditional expression
        tier = 4 if reading >= 14 else (3 if reading >= 11 else (2 if reading >= 8 else 1))
        
        # Apply dynamic penalty if oscillation detected (simulated condition)
        prev_val = data[idx - 1] if idx > 0 else reading
        delta = abs(reading - prev_val)
        volatility_penalty = 0.7 if delta > 2.5 else 1.0
        
        # Weighted contribution with bit-shift scaling (bit manipulation red herring)
        base_influence = reading * (volatility_penalty)
        scaled_influence = base_influence * (1 << 1) / 2  # Neutral transformation (x2 then /2)
        
        # Conditional filtering: ignore low-tier readings below threshold
        required = thresholds.get(tier, 0)
        if tier < 3 and reading < required * 0.8:
            continue  # Skip minor anomalies below noise floor
            
        total_weight += scaled_influence
        
        # Embedded dead logic (never reached due to continue above)
        if tier == 1:
            fallback_mode = True
            total_weight -= 0.5  # This never executes

    # Secondary adjustment based on data shape
    if len(data) > 4:
        shape_correction = len(data) // 2
        total_weight += shape_correction * 0.3
    else:
        total_weight += 0.1

    # Final nonlinear calibration
    calibrated = math.log(total_weight + 1) * 10
    return round(calibrated, 6)

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")