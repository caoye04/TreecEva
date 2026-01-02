from collections import defaultdict
import math

# Simulated sensor network data processing with diagnostic evaluation

def preprocess_readings(raw_samples):
    filtered = []
    noise_floor = 0.05
    for sample in raw_samples:
        if abs(sample) > noise_floor:
            filtered.append(round(sample ** 2, 6))
    return filtered


def generate_signature(data_chunk):
    # Irrelevant red herring function: generates hash-like signature not used in final result
    sig = 1
    for val in data_chunk:
        sig = (sig * int(val * 100)) % 97
    return sig


def evaluate_stability(metric):
    # Misleading intermediate calculation
    if metric < 0.1:
        return 'STABLE'
    elif metric < 1.0:
        return 'FLUCTUATING'
    else:
        return 'UNSTABLE'


def build_threshold_map(levels):
    # Correctly constructs mapping used later
    t_map = defaultdict(float)
    for key, value in levels.items():
        t_map[key] = math.log(value) if value > 0 else 0.0
    # Decoy modification
    t_map['aux'] = sum(t_map.values()) / len(t_map)
    return t_map


def compute_entropy(values):
    # Dead code path — never called
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)


def validate_calibration(readings):
    # Distractor function with misleading side-effect appearance
    baseline = sum(readings) / len(readings)
    deviation = sum(abs(r - baseline) for r in readings)
    return deviation < 5.0


def integrate_series(points):
    # Unused integration logic to distract
    integral = 0.0
    for i in range(1, len(points)):
        integral += (points[i] + points[i-1]) * 0.5
    return integral


def transform_coordinates(x_list):
    # Red herring transformation
    return [math.sin(x) + math.cos(x) for x in x_list]


def analyze_readings(data, thresholds):
    temp_result = 0
    state_log = []
    
    # Core relevant logic hidden among distractions
    for i, val in enumerate(data):
        key = 'low' if val < 2.0 else 'high'
        adjustment = thresholds.get(key, 0.5)
        
        # Real computation step
        temp_result += int(val * adjustment)
        
        # Irrelevant logging operation
        status = evaluate_stability(val)
        state_log.append(f'{i}:{status}')
    
    # Additional distraction: unused conditional expression
    fallback = 42 if len(state_log) % 2 == 0 else -99
    
    # Actual answer derivation
    final_score = temp_result - len([x for x in data if x > 3.0])
    
    # Final red herring: decoy adjustment
    if fallback == -100:
        final_score *= 2  # unreachable
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Sensor input simulation
    raw_sensor_data = [0.12, -0.34, 0.89, 1.23, 0.45, 3.67, 2.11, 0.08, 4.51, 1.78]
    
    # Irrelevant preprocessing
    coordinates = [1.0, 2.5, 3.3, 4.1]
    transformed_coords = transform_coordinates(coordinates)
    
    # Real pipeline begins
    processed_data = preprocess_readings(raw_sensor_data)
    
    # Unused entropy check
    # entropy_value = compute_entropy(processed_data)  # commented dead code
    
    config_levels = {
        'low': 2.718,
        'mid': 7.5,
        'high': 10.0
    }
    
    threshold_map = build_threshold_map(config_levels)
    
    # Validate system (distractor call)
    calibration_ok = validate_calibration(processed_data)
    
    # Signature generation (completely irrelevant)
    signature = generate_signature(processed_data)
    
    # Key statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")