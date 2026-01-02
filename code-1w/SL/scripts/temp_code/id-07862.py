import math

# Simulated sensor data preprocessing with multiple red herrings
def analyze_sequence(raw_values):
    temp_log = []
    cumulative = 0
    for val in raw_values:
        if val > 30:
            temp_log.append(val * 0.85)
        elif val < 10:
            temp_log.append(val * 1.2)
        else:
            temp_log.append(val)
    return [round(x, 2) for x in temp_log]

# Irrelevant transformation - dead code path (never called)
def encrypt_sequence(data):
    encrypted = ''
    for d in data:
        encrypted += chr((d % 26) + 97)
    return encrypted.lower().replace('a', 'x')

# Distractor function: looks important but unused in critical path
def validate_checksum(arr):
    checksum = 0
    for i, v in enumerate(arr):
        checksum += v * (i + 1)
    return checksum % 100 == 0

# Real signal processing chain
def filter_anomalies(dataset, limit):
    result = []
    for item in dataset:
        if abs(item - sum(dataset) / len(dataset)) < limit:
            result.append(item)
    return result

# Bit manipulation decoy - appears complex but irrelevant
def scramble_bits(x):
    x = (x ^ 61) ^ (x >> 4)
    x = (x + 37) | (x << 2)
    x = x % 7919  # arbitrary prime
    return x * 0.01

# String-based distractor using python methods
def generate_tag(metadata):
    tag = ''
    for k, v in metadata.items():
        tag += str(v)[:2]
    tag = tag.upper().lstrip('X').replace('5', '9')
    return tag[::-1]  # reverse string

# Core logic buried among noise
def process_signal(data, level):
    base = 0
    adjustment = 1.0
    
    # Hidden correct path begins here
    for i in range(len(data)):
        if i % 3 == 0:
            base += math.sin(data[i] * 0.1)
        elif i % 3 == 1:
            base -= math.cos(data[i] * 0.05)
        else:
            base += math.log(abs(data[i]) + 1) * 0.2
    
    # Apply nonlinear scaling
    if base > 0:
        adjustment = 1 / (1 + math.exp(-base))
    else:
        adjustment = math.tanh(base / 2)
    
    # Final computation
    output = int((base * adjustment * 10000) % 8765)
    
    # Decoy operations below (no effect on final_output)
    dummy = [scramble_bits(output + j) for j in range(5)]
    _ = generate_tag({'id': 'XYZ', 'ver': 55, 'seq': 123})
    
    return output

# Main execution block
if __name__ == '__main__':
    # Initial data set
    readings = [12, 45, 8, 67, 23, 9, 55, 14, 33, 72, 18, 41]
    
    # Irrelevant pre-processing steps (red herrings)
    processed = analyze_sequence(readings)
    metadata_checksum = sum([len(str(r)) for r in readings]) * 17
    
    # Real filtering step (looks similar to distractors)
    filtered_data = filter_anomalies(processed, 20.0)
    
    # Unused variables and misleading intermediate values
    outlier_count = len(readings) - len(filtered_data)
    normalized_total = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    cryptic_id = encrypt_sequence([int(f) for f in filtered_data])
    
    # Key threshold derived from dummy calculation
    threshold = abs(int(sum(readings) / 100)) or 1
    
    # Critical statement
    final_output = process_signal(filtered_data, threshold)
    
    # Print final answer as required
    print(f"Result: {final_output}")