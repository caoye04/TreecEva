import math

# Simulated sensor array data processing with diagnostic validation
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-9) for x in filtered]
    return [round(val, 6) for val in normalized]

# Irrelevant transformation: frequency domain mock (dead path)
def compute_fourier_components(signal):
    dummy_result = []
    for i in range(len(signal)):
        dummy_result.append(math.sin(signal[i] * 2 * math.pi / len(signal)))
    return dummy_result  # Never used

# Data shift correction using modular arithmetic
def apply_phase_shift(data, shift):
    if not data:
        return data
    shifted = [data[(i - shift) % len(data)] for i in range(len(data))]
    return shifted

# Conditional data inversion based on control flag
def invert_if_required(data, flags, threshold=0.5):
    control_state = sum(flags) / len(flags) if flags else 0
    if control_state > threshold:
        return [1 - x for x in data]
    return [x * 2 for x in data]  # alternate path

# Core pattern analyzer: computes weighted diagnostic score
def analyze_pattern(seq, settings):
    weight = settings['multiplier']
    offset = settings['offset']
    parity_adjust = 0

    # Determine adjustment based on sequence characteristics
    above_half = sum(1 for x in seq if x > 0.5)
    below_half = len(seq) - above_half
    
    if above_half > below_half:
        parity_adjust = 0.25
    elif above_half == below_half:
        parity_adjust = -0.1
    else:
        parity_adjust = 0.05

    # Weighted sum with adjustment
    base_score = sum(seq) * weight + offset
    adjusted_score = base_score + parity_adjust * len(seq)
    
    # Apply non-linear boost if conditions met
    if len(seq) % 3 == 0 and seq[-1] < 0.75:
        adjusted_score = math.log(adjusted_score + 10) * 2
    
    return round(adjusted_score, 6)

# Misleading auxiliary function: looks important but unused
def generate_calibration_sequence(length):
    return [math.cos(i * 0.5) ** 2 for i in range(length)]

def main():
    # Raw sensor inputs (simulated)
    raw_sensor_data = [0.05, -0.3, 0.72, 1.1, -0.01, 0.45, 0.88, 0.02, 0.63]
    
    # Irrelevant metadata
    device_id = "SENS-X9"
    firmware_version = "2.1.7"
    calibration_matrix = [[1, 0], [0, 1]]  # Unused
    timestamp_log = [1712345678, 1712345679, 1712345680]  # Dead variable
    
    # Preprocessing pipeline
    cleaned_data = preprocess_sensor_readings(raw_sensor_data)
    
    # Control flags from configuration
    activation_flags = [True, False, True, True]
    safety_engaged = any(not f for f in activation_flags)  # Used indirectly
    
    # Configuration parameters
    system_config = {
        'multiplier': 3.7,
        'offset': -2.1,
        'mode': 'diagnostic'
    }
    
    # Transform data through multiple stages
    shifted_data = apply_phase_shift(cleaned_data, shift=2)
    processed_data = invert_if_required(shifted_data, activation_flags, threshold=0.6)
    
    # Introduce red herring variables
    temp_amplitude = max(processed_data) - min(processed_data)  # Looks useful
    stability_index = len([x for x in processed_data if 0.4 <= x <= 0.6])  # Distractor
    noise_floor = 0.05 * temp_amplitude  # Meaningless extra
    
    # Transform again: create final input
    transformed_data = [math.sqrt(x * x + 1e-6) for x in processed_data]  # Avoid zero
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, system_config)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()