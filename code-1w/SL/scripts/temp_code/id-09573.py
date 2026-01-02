import itertools
import math

def analyze_signal_strength(raw_data, threshold):
    filtered = [x for x in raw_data if x > threshold]
    if len(filtered) == 0:
        return 0.0
    avg = sum(filtered) / len(filtered)
    return avg * 0.87

def compute_phase_shift(frequency, time_delay):
    shift = (frequency * time_delay) % 1.0
    return shift * 2 * math.pi

def generate_combinations(elements):
    # Distractor: unused function
    return list(itertools.combinations(elements, 2))

def process_calibration_sequence(calib_values):
    calibrated = []
    for val in calib_values:
        adjusted = val * 1.05
        if adjusted > 100:
            adjusted = 95
        calibrated.append(adjusted)
    return sorted(calibrated, reverse=True)

def detect_anomalies(signal_stream):
    anomalies = 0
    moving_avg = sum(signal_stream[:3]) / 3
    for i in range(3, len(signal_stream)):
        if abs(signal_stream[i] - moving_avg) > 0.6 * moving_avg:
            anomalies += 1
        moving_avg = (moving_avg * 2 + signal_stream[i]) / 3
    return anomalies

def normalize_vector(vec):
    # Distractor: irrelevant computation
    magnitude = math.sqrt(sum(x ** 2 for x in vec))
    return [v / magnitude for v in vec] if magnitude else vec

def aggregate_metrics(signals, flags):
    base_score = sum(math.ceil(s) for s in signals)
    flag_penalty = 0
    for f in flags:
        if f & 0b1010:  # Check specific bit pattern
            flag_penalty += 3
    temp_result = base_score - flag_penalty
    adjustment = len([x for x in signals if x < 10]) * 1.5
    final_value = int(temp_result + adjustment)
    return final_value

def main():
    # Real input data
    sensor_readings = [12.3, 15.7, 8.9, 23.1, 6.4, 18.5, 9.2]
    system_status_codes = [0b1101, 0b0100, 0b1011, 0b1110]
    
    # Irrelevant variables and decoy computations
    theoretical_max = 99.9
    calibration_curve = [1.1, 2.2, 3.3, 4.4]
    phase_corrections = []
    for t in range(5):
        phase_corrections.append(compute_phase_shift(440, t * 0.01))
    
    # Unused intermediate results
    normalized_vector = normalize_vector([3, 4, 5])
    combo_pairs = generate_combinations([1, 2, 3, 4])
    
    # Core relevant logic (but obscured)
    processed_signals = []
    for reading in sensor_readings:
        adjusted = reading * 0.91
        if adjusted < 10:
            adjusted = math.floor(adjusted)
        else:
            adjusted = math.ceil(adjusted)
        processed_signals.append(adjusted)
    
    # Another distractor: dead code path
    if False:
        dummy_cache = {}
        for k in range(10):
            dummy_cache[k] = k ** 3
    
    # Additional red herring: anomaly detection not used in final result
    _ = detect_anomalies(sensor_readings)
    
    # Actual critical computation chain
    normalized_signals = [analyze_signal_strength([s*1.1], 5) for s in processed_signals]
    system_flags = [code ^ 0b0011 for code in system_status_codes]
    
    # Key statement
    final_diagnostic = aggregate_metrics(normalized_signals, system_flags)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()