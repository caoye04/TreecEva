import math

# Simulated sensor data preprocessing with distractions
def generate_noise(length):
    return [math.sin(i * 0.1) + 0.5 for i in range(length)]

def dummy_analysis(data):
    # Irrelevant function: performs unused statistical analysis
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return {'mean': mean_val, 'variance': variance}

def filter_outliers(data, limit=3.0):
    # Unused filtering function (dead code path)
    avg = sum(data) / len(data)
    return [x for x in data if abs(x - avg) < limit]

def extract_features(signal):
    # Extracts frequency-like features using slicing and transformations
    N = len(signal)
    first_half = signal[:N//2]
    second_half = signal[N//2:]
    
    # Decoy computations
    temp_sum_1 = sum(first_half)
    temp_sum_2 = sum(second_half)
    dummy_ratio = temp_sum_1 / (temp_sum_2 + 1e-8)
    
    # Real feature: difference in energy
    energy_diff = sum(x**2 for x in first_half) - sum(x**2 for x in second_half)
    return abs(energy_diff)

def transform_signal(raw):
    # Applies transformation with lambda and string-based control (distractor)
    operation_code = 'lambda x: x * 2'
    if 'lambda' in operation_code:
        multiplier = 1.5  # Misleading: looks like it's used but isn't
    parsed_func = lambda x: x * 1.8  # Actual transformation (obscured)
    
    # Apply transformation and add offset
    adjusted = [parsed_func(x) + 0.2 for x in raw]
    
    # String distraction
    metadata_tag = "processed_v2"
    version_check = metadata_tag.split('_')[-1]  # v2
    
    # Unused conditional branch
    if version_check == "v1":
        adjusted = [x * 0.9 for x in adjusted]
    
    return adjusted

def evaluate_threshold(value):
    # Complex threshold logic with red herring conditions
    if value < 0:
        return 10
    elif value < 50:
        return 25
    elif value < 100:
        return 50
    else:
        return 75  # This path is not taken

def process_signal(data, thresh):
    # Core processing logic
    base_metric = sum(data) * 0.1
    feature_score = extract_features(data)
    
    # Multiple comparison operations and short-circuit logic
    if feature_score > thresh and len(data) > 0 or base_metric < 0:
        adjustment = 1.2
    else:
        adjustment = 0.8
    
    # Critical computation
    result = (base_metric + feature_score) * adjustment
    
    # Distractor: irrelevant bitwise and modular arithmetic
    decoy_value = (int(result) & 255) ^ 128
    modulo_trace = int(result) % 97
    
    # Final output influenced by adjustment
    return int(result)

# Main execution flow
if __name__ == "__main__":
    # Generate initial data
    raw_sensor_data = [0.1 * i for i in range(40)]  # Linear ramp
    
    # Add noise (relevant)
    noise_component = generate_noise(40)
    combined_signal = [raw_sensor_data[i] + noise_component[i] for i in range(40)]
    
    # Apply transformation (key step)
    transformed_data = transform_signal(combined_signal)
    
    # Dummy analysis call (irrelevant usage)
    stats = dummy_analysis(transformed_data)
    
    # Extract threshold via indirect logic
    signal_length = len(transformed_data)
    threshold_basis = extract_features(transformed_data)
    threshold = min(int(threshold_basis / 2), 40)  # Evaluates to 20
    
    # UNUSED: another dead-end function
    def legacy_mode(data):
        return [x for x in data if x > 0.5]
    
    # Key statement
    final_output = process_signal(transformed_data, threshold)
    
    # Print result
    print(f"Result: {final_output}")