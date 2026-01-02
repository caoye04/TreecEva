import itertools

def analyze_readings(data_sequence):
    # Irrelevant analysis function (dead code path)
    cumulative_noise = 0
    for val in data_sequence:
        if val % 7 == 0:
            cumulative_noise += val ** 0.5
    return cumulative_noise

def validate_sensor_range(values):
    # Misleading validation logic (not actually used in main path)
    threshold = 255
    for v in values:
        if v > threshold:
            return False
    return True

def transform_signal(signal_stream):
    # Distractor transformation with unused result
    shifted = [(x << 2) & 255 for x in signal_stream]
    inverted = [~x & 255 for x in shifted]
    return inverted

def extract_frequency_peaks(samples):
    # Another decoy function that computes but doesn't affect final result
    peaks = []
    for i in range(1, len(samples) - 1):
        if samples[i] > samples[i-1] and samples[i] > samples[i+1]:
            peaks.append(i * samples[i])
    return sum(peaks) % 1000

def calculate_stellar_flux(readings, calib):
    # Core relevant logic buried among distractions
    base_sum = 0
    adjustment_factor = calib['gain'] * 0.85
    
    # Real computation begins
    filtered = [r for r in readings if r > 50]
    
    # Use of enumerate and zip (required features)
    for idx, (val, offset) in enumerate(zip(filtered, itertools.cycle(calib['offsets']))):
        if idx % 3 == 0:
            base_sum += val * adjustment_factor + offset
        elif idx % 5 == 0:
            base_sum -= val / adjustment_factor
        else:
            base_sum += (val + offset) // (idx + 1)
    
    # Final transformation using bit manipulation
    temp_result = int(base_sum ^ 0xAA) + (base_sum >> 4)
    final_result = (temp_result * calib['multiplier']) & 0xFFFF
    
    # Decoy branch — never executed due to data constraints
    if len(readings) < 10 and calib['multiplier'] < 0:
        return extract_frequency_peaks(readings)
        
    return final_result

# Main execution block
if __name__ == '__main__':
    # Sensor readings from deep-space array (real input data)
    raw_readings = [120, 85, 210, 93, 167, 74, 198, 134, 205, 176, 143, 188]
    
    # Calibration data structure with meaningful fields
    calibration_data = {
        'gain': 1.25,
        'offsets': [3, -7, 12],
        'multiplier': 4
    }
    
    # Irrelevant pre-processing steps (distractors)
    noise_floor = analyze_readings(raw_readings)
    signal_envelope = transform_signal(raw_readings)
    is_valid = validate_sensor_range(raw_readings)
    peak_score = extract_frequency_peaks(raw_readings)
    
    # Key statement where answer is computed
    final_flux = calculate_stellar_flux(raw_readings, calibration_data)
    
    # Output result as required
    print(f"Result: {final_flux}")