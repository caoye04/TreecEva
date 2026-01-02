import math

# Simulated sensor data processing with red herrings and complex transformations
def preprocess_signal(raw_input):
    offset = 107
    scaled = [x * 1.5 + offset for x in raw_input]
    filtered = [x for x in scaled if x > 110]
    return filtered[::-1]  # Reverse after filtering (slicing)

def compute_checksum(data):
    # Irrelevant checksum calculation (dead-end function)
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1)
    return checksum % 1000

def generate_sequence(n):
    # Distractor: generates Fibonacci-like sequence not directly used
    seq = [1, 1]
    for i in range(2, n * 2):
        seq.append(seq[i-1] + seq[i-2])
    return seq[n:]

def transform_readings(readings):
    # Key transformation with slicing and arithmetic
    readings_shifted = [r - 95 for r in readings]
    squared_noises = [math.sin(r) ** 2 + 0.1 for r in readings_shifted]
    base_power = sum(readings_shifted[:len(readings_shifted)//2])
    
    # Heavily disguised accumulation via trigonometric smoothing
    smoothed = []
    for i in range(len(readings_shifted)):
        angle = readings_shifted[i] * math.pi / 180
        smoothed.append(math.cos(angle) * 100)
    
    # Real key path: slice middle segment and sum absolute deviations
    mid_section = smoothed[1:-1]  # Exclude first and last
    deviation_sum = sum(abs(x) for x in mid_section) // 1  # Floor to int
    
    # Decoy assignment
    magic_factor = len(generate_sequence(5))  # Calls distractor function
    dummy_correction = compute_checksum(smoothed)  # Use irrelevant function
    
    return deviation_sum, dummy_correction, magic_factor

def evaluate_integrity(diag):
    # Complex logical checks that ultimately don't affect final result
    if diag < 100:
        return diag * 3
    elif diag < 200:
        return diag + 50
    else:
        temp = diag
        for _ in range(3):
            temp = (temp // 2) + 10
        return temp

# Unused recursive decoy
def predict_failure(threshold, depth=3):
    if depth == 0:
        return threshold * 0.8
    return predict_failure(threshold * 0.9, depth - 1)

def analyze_pattern(processed_tuple):
    raw_value = processed_tuple[0]  # Extract actual computed value
    adjusted = raw_value * 1.1
    
    # Apply conditional floor/ceil based on parity (red herring logic)
    if int(adjusted) % 2 == 0:
        adjusted = math.floor(adjusted)
    else:
        adjusted = math.ceil(adjusted)
    
    # Final manipulation using slicing on artificial string representation
    str_rep = str(int(adjusted * 100))
    sliced_str = str_rep[1:4]  # Take middle digits
    final_numeric = int(sliced_str) if sliced_str else 0
    
    # Final adjustment: only hundreds digit matters due to earlier slicing
    return final_numeric

# Main execution flow
if __name__ == '__main__':
    sensor_log = [78, 82, 85, 90, 93, 94, 95, 96, 97, 98, 100]
    
    # Preprocess with reversal and offset
    cleaned = preprocess_signal(sensor_log)
    
    # Core computation tuple: (deviation_sum, dummy_correction, magic_factor)
    transformed_data = transform_readings(cleaned)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")