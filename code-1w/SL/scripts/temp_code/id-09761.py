import math

# Simulated sensor data processing with decoy functions and variables
def acquire_signal(raw=True):
    if raw:
        return [0.1, -0.5, 2.3, -1.2, 4.4, -3.1, 0.0, 1.8]
    else:
        return []

# Irrelevant transformation (dead function)
def encrypt_data(data):
    return [int(x * 101) ^ 255 for x in data]

# Unused helper (distractor)
def moving_average(signal, window=3):
    result = []
    for i in range(len(signal) - window + 1):
        result.append(sum(signal[i:i+window]) / window)
    return result

# Decoy statistical analysis
def compute_entropy(data):
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0.0
    probs = [abs(x)/total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Actual relevant transformation with conditional expression
def transform_signal(data, mode='advanced'):
    scaled = [x * 2.5 for x in data]
    adjusted = [val if val >= 0 else abs(val) * 0.5 for val in scaled]  # conditional expression used
    normalized = [x / (max(adjusted) + 1e-9) for x in adjusted]
    return [round(x, 6) for x in normalized]

# Red herring: checksum validation (never called in main logic)
def validate_checksum(processed):
    base = int(sum(x * 1000 for x in processed))
    return (base % 256) == ((base >> 8) % 256)

# Core processing with nested logic and multiple concepts
def process_signal(data, limit):
    count_above = 0
    running_sum = 0.0
    temp_flags = []
    
    for idx, value in enumerate(data):
        # Simulated filter condition
        if value < 0.1:
            temp_flags.append(False)
            continue
        
        # Bit manipulation red herring (value masked but not used later)
        shifted = int(value * 100) << 2
        masked = shifted & 0xFF
        
        # Logical operation with short-circuiting
        is_significant = (masked > limit) and (idx % 2 == 0 or value > 0.5)
        
        if is_significant or (value > 0.75):
            count_above += 1
            running_sum += value * (1 + (idx % 3))  # complex weight
            
    # Final aggregation using modular arithmetic and integer division
    multiplier = (count_above % 7) or 1
    adjustment = (int(running_sum) // 3) % 5
    
    # Conditional expression determining final result
    result = running_sum * multiplier if count_above > 2 else running_sum / (multiplier + 1)
    
    # Irrelevant secondary computation (distractor)
    outlier_score = sum(1 for v in data if v > 0.9)
    compression_ratio = len(data) / (outlier_score + 1)
    
    return round(result, 6)

# --- Main execution with hidden signal flow ---
raw_sensor_data = acquire_signal(True)

# Dead assignment (unused path)
decrypted_buffer = encrypt_data(raw_sensor_data)

# Real processing begins here
transformed_data = transform_signal(raw_sensor_data, mode='advanced')

# Spurious intermediate check (no effect on output)
entropy_value = compute_entropy(transformed_data)

threshold = 45  # Used in process_signal's masked logic

# Key statement
final_output = process_signal(transformed_data, threshold)

# Output the target result
print(f"Result: {final_output}")