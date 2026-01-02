import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_readings):
    filtered = []
    for x in raw_readings:
        if x < -50 or x > 50:
            continue
        filtered.append(x * 0.87 + 3.2)
    return filtered

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(data):
    return [d * 0.95 for d in data if d > 0]

# Transform data using non-linear scaling (relevant)
def apply_enhancement(signal):
    enhanced = []
    accumulator = 0.0
    for val in signal:
        temp = abs(val) ** 0.5 * math.sin(val / 10)
        accumulator += temp
        enhanced.append(temp)
    scale_factor = 1.5 if accumulator > 0 else 2.0
    return [e * scale_factor for e in enhanced], accumulator

# Misleading pattern matcher (partial distractor)
def detect_anomaly(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] > 5:
            count += 1
    return count > 3  # Not used in final logic

# Core pattern analyzer (used)
def evaluate_coherence(stream):
    total = 0
    for idx, value in enumerate(stream):
        if idx % 2 == 0:
            total += int(value) & 7
        else:
            total -= int(abs(value)) % 5
    return abs(total)

# Conditional expression heavy transformation
# Also includes bit manipulation and logical masking
def transform_readings(readings):
    processed = []
    stats = {'positive': 0, 'negative': 0, 'zero': 0}
    for r in readings:
        adjusted = r + (12 if r > 0 else -8)
        masked = int(adjusted) & 0xFF  # Keep within byte range
        inverted = (~masked & 0xFF) if masked < 100 else masked
        # Conditional expression with side effect mimicry
        category = 'A' if inverted > 200 else 'B' if inverted > 100 else 'C'
        if category == 'A':
            stats['positive'] += 1
        elif category == 'B':
            stats['negative'] += 1
        else:
            stats['zero'] += 1
        processed.append(inverted)
    # Return transformed data and ignored stats
    return processed

# Final analysis function combining multiple concepts
def analyze_pattern(data, limit):
    magnitude = sum(d ** 2 for d in data if d < limit)
    avg = magnitude / len(data) if data else 0
    peak = max(data) if data else 0
    
    # Logical operations with short-circuiting
    flag = (avg > 50) and (peak < 250) or (len(data) == 0)
    
    # Bitwise combination with arithmetic
    signature = (int(avg) & 0xF) ^ (peak >> 4) & 0x7
    
    # Conditional expression determines output
    result = (signature * 3) if not flag else (signature + 1000)
    
    # Additional red herring computation (unused)
    decoy = 0
    for i in range(len(data)):
        decoy += (data[i] ^ signature) % 7
    decoy = decoy * 13 // max(1, signature)
    
    return result

# Unused auxiliary function (distractor)
def compute_baseline(samples):
    return sum(samples) / len(samples) if samples else 0

# --- Main execution ---
if __name__ == "__main__":
    # Initial sensor input (simulated)
    raw_sensor_data = [
        -65, 12, 45, -23, 78, 31, -89, 19, 54, -11,
        67, -34, 22, 81, -44, 39, 73, -29, 16, 58
    ]
    
    # Step 1: Filter out-of-range values
    clean_signal = preprocess_signal(raw_sensor_data)
    
    # Step 2: Apply non-linear enhancement (returns tuple)
    enhanced_data, net_flow = apply_enhancement(clean_signal)
    
    # Step 3: Transform using byte-level manipulations
    transformed_data = transform_readings(enhanced_data)
    
    # Irrelevant branching (dead code - distractor)
    if len(transformed_data) > 50:
        backup = legacy_calibrate(transformed_data)
    else:
        debug_info = evaluate_coherence(transformed_data)  # Computed but unused
    
    # Threshold derived from conditional expression
    base_threshold = 150 if net_flow > 0 else 200
    adjustment = 25 if len(transformed_data) % 2 == 1 else 0
    threshold = base_threshold + adjustment
    
    # Key statement: final diagnostic calculation
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")