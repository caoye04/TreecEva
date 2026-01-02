import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw_signals = [127, 255, 192, 64, 31, 8, 16]
    processed = []
    for val in raw_signals:
        if val > 100:
            processed.append(val ^ 0xAA)  # Bit manipulation distraction
        elif val > 50:
            processed.append(val << 1)
        else:
            processed.append(int(math.sqrt(val)))
    return processed

# Irrelevant utility function (decoy)
def calculate_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d * 3
    return checksum % 256

# Data transformation with meaningful and irrelevant steps
def transform_readings(raw_data):
    scaled = [x * 1.5 for x in raw_data]  # List comprehension - relevant
    offset = sum(scaled) / len(scaled) + 10  # Red herring calculation
    adjusted = [int(x - offset) for x in scaled]
    filtered = [x for x in adjusted if x > -20]  # Another list comp - partially relevant
    
    # Dead code path (never executed due to prior filter)
    anomalies = []
    for v in adjusted:
        if v < -1000:  # Impossible condition
            anomalies.append(v)
    
    # Meaningful transformation buried in noise
    packed = tuple(abs(x) % 100 for x in filtered)  # Tuple generation
    return packed

# Core analysis logic
def evaluate_entropy(sequence):
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(sequence)
    for count in freq_map.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return round(entropy, 4)

# Decoy function that looks important but isn't used in main flow
def predict_next_value(pattern):
    if len(pattern) < 3:
        return -1
    return pattern[-1] + (pattern[-1] - pattern[-2])

# Main diagnostic analyzer
def analyze_pattern(data, limit):
    # Linear search through transformed data
    significant = []
    for x in data:
        if x > limit:
            significant.append(x)
    
    # Secondary filtering based on digit properties (distraction)
    special_count = 0
    for num in significant:
        digits = [int(d) for d in str(num)]
        if sum(digits) % 3 == 0 and len(digits) < 3:
            special_count += 1
    
    # Critical computation
    base_score = sum(significant)
    penalty = special_count * 15
    final_score = base_score - penalty
    
    # Misleading alternate path (unused)
    alternative = 0
    if len(significant) == 0:
        alternative = 999
    
    return final_score

# Orchestration with red herrings
if __name__ == "__main__":
    readings = collect_readings()                    # Step 1
    checksum = calculate_checksum(readings)           # Distractor variable
    transformed_data = transform_readings(readings)  # Step 2: key transformation
    
    # Fake error injection check (always false)
    error_flag = False
    for val in readings:
        if val < 0 and val > 1000:
            error_flag = True
    
    threshold = 45
    final_diagnostic = analyze_pattern(transformed_data, threshold)  # Key statement
    
    # Unused variables to increase interference
    debug_trace = [readings, transformed_data, checksum]
    metadata_summary = f"Processed {len(readings)} inputs"
    
    print(f"Result: {final_diagnostic}")