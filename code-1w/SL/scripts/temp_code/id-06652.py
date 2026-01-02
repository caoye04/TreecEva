def analyze_pattern(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
    return count

# Simulate sensor data drift (irrelevant computation)
def calculate_drift_correction(readings):
    corrected = []
    baseline = sum(readings[:5]) / 5
    for val in readings:
        corrected.append(val - baseline)
    return corrected

# Misleading auxiliary function dealing with string transformations
def transform_labels(labels):
    result = []
    for label in labels:
        temp = label.upper().replace('A', 'X').split('I')
        result.extend(temp)
    return [r for r in result if r]

# Core logic to compute score based on thresholded segments
def compute_segment_power(arr, thres):
    power = 0
    segment = arr[1:-1]  # Remove edges
    filtered = [x for x in segment if x > thres]
    for val in filtered:
        if val % 2 == 0:
            power += val ** 1.5
        else:
            power += val ** 1.2
    return int(power)

# Main scoring function
def compute_final_score(raw_data, limits):
    # Step 1: Preprocess with slicing and filtering
    trimmed = raw_data[3:13]  # Focus on window of interest
    
    # Irrelevant transformation (distractor)
    inverted = [1.0 / (x + 1) for x in trimmed if x != -1]
    inversion_sum = sum(inverted)
    
    # Step 2: Count upward trends (real but indirect contribution)
    trend_strength = analyze_pattern(trimmed)
    
    # Step 3: Apply dynamic threshold from input
    threshold = limits['t1']
    base_power = compute_segment_power(trimmed, threshold)
    
    # Step 4: Conditional boost based on trend
    adjustment_factor = 1.0
    if trend_strength > 4:
        adjustment_factor = 1.3
    elif trend_strength == 3:
        adjustment_factor = 1.1
    
    # Step 5: Compute secondary metric (unused red herring)
    mean_val = sum(trimmed) / len(trimmed)
    variance_proxy = sum((x - mean_val) ** 2 for x in trimmed) / len(trimmed)
    stability_score = 100 / (1 + variance_proxy)  # Not used later
    
    # Step 6: Final composition
    intermediate = base_power * adjustment_factor
    
    # Apply bonus only if specific slice has descending property
    mid_slice = trimmed[2:6]
    if all(mid_slice[i] >= mid_slice[i+1] for i in range(len(mid_slice)-1)):
        intermediate += 25
    
    # Final nonlinear scaling
    final_value = int(intermediate ** 0.9)
    
    return final_value

# Input data
sensor_data = [5, 8, 6, 12, 14, 13, 11, 9, 10, 7, 5, 4, 3, 2, 1, 0]
config = {'t1': 8, 't2': 15}

# Unused preprocessing (distractor path)
data_str = "sens1,sens2,sens3,sens4"
labels_list = transform_labels(data_str.split(','))
drift_corrected = calculate_drift_correction(sensor_data)

# Key execution point
final_score = compute_final_score(sensor_data, config)
print(f"Result: {final_score}")