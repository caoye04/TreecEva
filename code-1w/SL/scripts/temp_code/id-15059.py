import math

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            peaks += 1
    return peaks

def filter_noise(data, limit):
    # Irrelevant filtering function (dead path)
    cleaned = [x for x in data if abs(x) <= limit]
    scaling_factor = 1.7
    adjusted = [int(x * scaling_factor) for x in cleaned]
    return adjusted

def compute_entropy(values):
    # Misleading computation
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [abs(v / total) for v in values if v != 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def extract_features(signal):
    # Distractor: complex but unused feature extraction
    magnitude = sum(abs(x) for x in signal)
    energy = sum(x**2 for x in signal)
    avg = magnitude / len(signal)
    fluctuation_index = energy / (avg + 1e-8)
    trend = signal[-1] - signal[0]
    return {
        'mag': magnitude,
        'energy': energy,
        'fluct': fluctuation_index,
        'trend': trend
    }

def validate_calibration(reference):
    # Unused validation logic (red herring)
    base = reference[:len(reference)//2]
    mirror = reference[::-1]
    if base == mirror[len(mirror)//2:]:
        return True
    else:
        temp_sum = 0
        for i in range(len(reference)):
            temp_sum += reference[i] * (-1)**i
        return temp_sum % 2 == 0

def process_readings(readings, cutoff):
    # Core relevant logic embedded in distractions
    segment_a = readings[::2]  # slicing
    segment_b = readings[1::2] # slicing
    
    # Redundant transformations
    transformed_a = [x + 2 for x in segment_a]
    transformed_b = [x - 1 for x in segment_b]
    
    # Real computation begins here
    combined = []
    for i in range(min(len(transformed_a), len(transformed_b))):
        combined.append(transformed_a[i])
        combined.append(transformed_b[i])
    
    if len(combined) == 0:
        return 0
    
    # Compute moving average of window size 3
    smoothed = []
    for i in range(2, len(combined)):
        window_avg = (combined[i-2] + combined[i-1] + combined[i]) / 3
        smoothed.append(window_avg)
    
    # Apply threshold filtering (key step)
    filtered = [val for val in smoothed if val > cutoff]
    
    # Count how many exceed double the cutoff (critical logic)
    strict_count = sum(1 for v in filtered if v > 2 * cutoff)
    
    # Secondary check: pattern analysis on original slice
    sample_window = readings[2:8]  # slicing
    peak_count = analyze_pattern(sample_window)
    
    # Final diagnostic depends on both strict_count and peak_count
    result_offset = 3 * peak_count
    final_score = strict_count * 17 + result_offset
    
    # Dead code branch below (never reached due to return above)
    if final_score < 0:
        backup = compute_entropy(readings)
        return int(backup * 100)
    
    return final_score

# Main execution
sensor_array = [3, 1, 4, 5, 2, 6, 7, 3, 2, 5, 1]
config_flag = True
diagnostic_mode = "advanced"
baseline_ref = [1, 2, 3, 2, 1]
threshold = 3.5

# Unused intermediate variables (distractors)
calibration_valid = validate_calibration(baseline_ref)
features = extract_features(sensor_array)
noise_filtered = filter_noise(sensor_array, 10)
raw_entropy = compute_entropy(noise_filtered)

# Key assignment
final_diagnostic = process_readings(sensor_array, threshold)

Result: {final_diagnostic}