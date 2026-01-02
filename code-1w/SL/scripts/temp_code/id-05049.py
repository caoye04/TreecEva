from collections import defaultdict
import math

# Simulate sensor data preprocessing with noise filtering and signal extraction
def preprocess_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    normalized = [abs(x - baseline) for x in filtered]
    return normalized

# Misleading auxiliary function - never called but looks important
def analyze_turbulence(data):
    variance = sum((x - sum(data)/len(data))**2 for x in data) / len(data)
    return math.sqrt(variance) if variance > 1 else 0

# Core recursive transformation function
def transform_sequence(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq
    shifted = [(seq[i] + seq[(i+1)%len(seq)]) // 2 for i in range(len(seq))]
    return transform_sequence(shifted, depth + 1)

# Main equilibrium calculation with multiple red herrings
def calculate_equilibrium(readings, threshold):
    # Irrelevant statistical computations (distractors)
    stats = defaultdict(int)
    for val in readings:
        if val > threshold:
            stats['high'] += 1
        elif val < threshold:
            stats['low'] += 1
        else:
            stats['equal'] += 1
    
    # Unused intermediate transformations
    inverted = [100 - x for x in readings if x % 2 == 0]
    compressed = [readings[i] for i in range(0, len(readings), 2)]
    
    # Key processing path
    processed = preprocess_sensor_data(readings)
    if not processed:
        return 0
    
    transformed = transform_sequence(processed)
    
    # Decoy control flow with early return that won't trigger
    if sum(transformed) < 50:
        return -1  # dead path under this input
    
    # Actual computation of equilibrium score
    positive_flux = sum(1 for x in transformed if x > threshold)
    negative_flux = sum(1 for x in transformed if x < threshold)
    neutral_flux = len(transformed) - positive_flux - negative_flux
    
    # Introduce bit manipulation decoy
    mask = 0b101010
    masked_value = positive_flux ^ mask & negative_flux
    
    # Real result computation (obscured among distractors)
    equilibrium_score = (positive_flux * 3) - (negative_flux * 2) + (neutral_flux * 1)
    
    # Multiple assignments to obscure tracking
    temp_a = neutral_flux
    temp_b = positive_flux
    temp_c = negative_flux
    temp_d = temp_a + temp_b - temp_c
    
    # Red herring: unused list comprehension with complex logic
    _ = [math.floor(math.log(x + 1)) for x in readings if x > 0 and x % 7 == 0]
    
    return equilibrium_score

# Simulated input data (real signal embedded in noise)
raw_sensor_input = [85, 12, 67, 90, 11, 66, 88, 13, 64, 15]
config_threshold = 50

# Dead code path - looks like system calibration
if __name__ == "__main__":
    calibration_sequence = [1, 1, 2, 3, 5, 8, 13]
    for step in calibration_sequence:
        adjustment = step * 0.5

# Actual execution sequence
flow_series = preprocess_sensor_data(raw_sensor_input)
equilibrium_score = calculate_equilibrium(flow_series, config_threshold)

# Critical output statement
Result: {equilibrium_score}