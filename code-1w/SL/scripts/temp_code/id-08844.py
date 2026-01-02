from collections import defaultdict, Counter
import math

# Simulated sensor fusion module for environmental monitoring
def collect_diagnostics(raw):
    temp_readings = [x for x in raw if 10 <= x <= 50]
    pressure_readings = [x for x in raw if 900 <= x <= 1100]
    aux_signals = [x for x in raw if x < 0]

    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    avg_pressure = sum(pressure_readings) / len(pressure_readings) if pressure_readings else 1013.25

    # Irrelevant transformation: signal harmonics (dead-end computation)
    harmonic_distortion = 0
    for i in range(len(aux_signals)):
        harmonic_distortion += abs(aux_signals[i]) ** 1.5
    normalized_harmonic = harmonic_distortion / (len(aux_signals) + 1)

    # Critical diagnostic baseline
    base_index = (avg_temp * 1.8) + 32 if avg_pressure > 1000 else (avg_temp * 1.5) + 40

    return base_index, avg_pressure, normalized_harmonic

def analyze_pattern(sequence):
    # Analyze repeating cycles in data (distractor function)
    freq = Counter(sequence)
    mode = freq.most_common(1)[0][1]
    unique_count = len(freq)
    entropy = -sum((count / len(sequence)) * math.log2(count / len(sequence)) for count in freq.values())
    return entropy > 2.5  # unused return in main logic

def validate_calibration(signal):
    # Bit manipulation based calibration check (mixed relevance)
    calibrated = True
    for s in signal:
        if s > 0:
            binary_rep = bin(int(s))[2:]
            ones = binary_rep.count('1')
            zeros = binary_rep.count('0')
            if ones < zeros and s % 7 == 0:
                calibrated = False  # red herring flag
    return True  # always returns True regardless

def extract_features(data):
    # Feature extraction with multiple distractors
    features = defaultdict(float)
    squared_sum = 0
    cube_sum = 0
    valid_magnitude = []

    for d in data:
        if d > 100:
            continue
        if d < 0:
            continue
        squared_sum += d ** 2
        cube_sum += d ** 3
        valid_magnitude.append(d)

    # Distractor accumulations
    features['rms'] = (squared_sum / len(valid_magnitude)) ** 0.5 if valid_magnitude else 0
    features['skew_hint'] = cube_sum / (squared_sum ** 1.5) if squared_sum != 0 else 0

    # Real feature used later
    features['magnitude_avg'] = sum(valid_magnitude) / len(valid_magnitude) if valid_magnitude else 0

    # Unused complex calculation
    phi = 1.618
    features['golden_ratio_match'] = sum(1 for v in valid_magnitude if abs(v - phi * 10) < 5)

    return features

def process_readings(readings):
    # Main processing chain
    base_diag, pressure, distortion = collect_diagnostics(readings)

    # Distractor conditional (never affects outcome due to prior logic)
    if pressure < 950 or pressure > 1050:
        adjustment_factor = 0.85
    elif pressure >= 1013:
        adjustment_factor = 1.05
    else:
        adjustment_factor = 1.0

    # Red herring: pattern analysis
    has_complex_pattern = analyze_pattern(readings)
    is_calibrated = validate_calibration(readings)

    # Extract key features
    feats = extract_features(readings)
    magnitude_center = feats['magnitude_avg']

    # Core calculation path (depends on base_diag and magnitude_center)
    intermediate = base_diag * 0.7 + magnitude_center * 1.3

    # Secondary adjustment using irrelevant harmonic data (but variable exists)
    noise_offset = distortion * 0.01  # minimal impact but looks important

    # Final non-linear transformation
    final_score = math.log(intermediate + 1) * 50 + noise_offset

    # Conditional override that looks critical but is actually stable
    final_diagnostic = final_score if final_score > 100 else final_score + 20

    # Dead code: advanced correction matrix (unreachable)
    # correction_matrix = [[1, 0], [0, 1]]
    # if has_complex_pattern and not is_calibrated:
    #     final_diagnostic *= 0.9

    return final_diagnostic

# Simulated IoT sensor array data stream
sensor_data = [23, 25, 24, 26, 22, 1012, 1015, 1010, -5, -3, 105, 200, 300, 18, 19, 21]

# Execute main logic
diag_result = process_readings(sensor_data)
final_diagnostic = diag_result

# Output result
print(f"Target result: {final_diagnostic}")