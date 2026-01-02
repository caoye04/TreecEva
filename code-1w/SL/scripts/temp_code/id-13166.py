import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw_samples = [127, 255, 192, 64, 8, 31, 156]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

def apply_filter(signal, threshold=100):
    # Irrelevant filtering (distractor)
    filtered = [x for x in signal if x > threshold]
    normalization_constant = 1.0 / (sum(filtered) or 1)
    return [x * normalization_constant for x in filtered]

def generate_checksum(sequence):
    # Unused function - red herring
    checksum = 0
    for val in sequence:
        checksum ^= int(val)
    return checksum % 256

def transform_sequence(data_stream):
    # Complex transformation with relevant and irrelevant parts
    temp_buffer = []
    shift_key = 3
    mask = 0xFF
    multiplier = lambda x: (x ** 2) + 1  # Used later

    for item in data_stream:
        processed = int(item)
        # Bit manipulation - partly relevant
        processed = (processed << 1) & mask
        processed = multiplier(processed)  # This line is critical
        temp_buffer.append(processed)
    
    # Dead code path - misleading
    if len(temp_buffer) > 10:
        temp_buffer = temp_buffer[::-1]
    
    # Linear search for specific pattern (only one element matters)
    target_candidate = None
    for val in temp_buffer:
        if val % 17 == 0 and val > 50:
            target_candidate = val
            break  # Only first match considered

    # Distractor computation
    aggregate_entropy = sum(math.log(x) for x in temp_buffer if x > 1) / len(temp_buffer)
    entropy_flag = aggregate_entropy > 3

    # Critical transformation - modifies target_candidate
    if target_candidate:
        target_candidate = (target_candidate >> 2) ^ 42  # Key step
    
    return temp_buffer, target_candidate, entropy_flag

def evaluate_stability(metrics):
    # Unused stability analysis - dead end
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    return variance < 50

def analyze_pattern(dataset, limit):
    # Core logic hidden among distractions
    base_values = [x for x in dataset if x < limit]
    offset = 5
    accumulator = 0
    
    for i, v in enumerate(base_values):
        if i % 2 == 0:
            accumulator += v // (i + 1)
        else:
            accumulator -= v % 10
    
    # Secondary manipulation
    accumulator = abs(accumulator)
    accumulator = (accumulator ^ 184) + 7  # Final transformation
    return accumulator

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()
    filtered_readings = apply_filter(readings)
    
    # Transform data - returns buffer, candidate, flag
    transformed_data, candidate_hint, noise_level = transform_sequence(readings)
    
    # Decoy usage of outputs
    if noise_level:
        candidate_hint *= 2  # Never actually used later
    
    # Generate unused checksums
    _ = generate_checksum(transformed_data)
    _ = generate_checksum(readings)
    
    # Sorting distractor
    sorted_data = sorted(transformed_data, reverse=True)
    median_estimate = sorted_data[len(sorted_data)//2]
    
    # Conditional dead branch
    if median_estimate < 100:
        evaluate_stability(transformed_data)
    
    # Key threshold derived from modular arithmetic
    key_threshold = (sum(transformed_data) % 89) + 23  # Evaluates to 61
    
    # Critical assignment - this is where the answer forms
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")