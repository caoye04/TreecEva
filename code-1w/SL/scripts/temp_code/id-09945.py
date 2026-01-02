from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulate a sensor data processing pipeline with diagnostic flags
def preprocess_sensors(raw_readings):
    processed = []
    for idx, val in enumerate(raw_readings):
        if idx % 7 == 0:
            # Irrelevant smoothing logic (dead path due to condition)
            smoothed = sum(raw_readings[max(0, idx-2):idx+1]) / (idx + 1)
        elif val < 0:
            processed.append(abs(val) * 2)
        else:
            processed.append(val ^ 3)
    return processed

# Misleading transformation chain
def encrypt_sequence(seq):
    key_shift = 5
    encrypted = []
    for i, x in enumerate(seq):
        encrypted.append((x + key_shift) * 3 % 256)
    return encrypted  # Never actually used in final computation

def generate_control_vector(length, seed=13):
    vec = [0] * length
    a, b = 1, seed
    for i in range(length):
        a, b = b, (a + b) % 17
        vec[i] = b
    return vec[:length]

def filter_anomalies(data, threshold=150):
    counts = Counter(data)
    return [x for x in data if counts[x] > 1 and x < threshold]

# Core analysis function - only this affects the answer
def analyze_pattern(arr, ctrl):
    state = 0
    freq_map = defaultdict(int)
    for x in arr:
        freq_map[x] += 1
    
    # Critical logic steps (8-12 inference steps)
    temp = 0
    for i, c in enumerate(ctrl):
        if i >= len(arr): break
        temp ^= arr[i]
        temp += c % 4
        
    temp *= 3
    temp -= sum(ctrl[:len(arr)]) // 7
    
    # Combine frequency-weighted sum
    weighted = 0
    for k, v in freq_map.items():
        if v >= 2:
            weighted += k * v
    
    state = (temp + weighted) % 10000
    
    # Decoy branches below
    if state > 5000:
        state = (state // 2) ^ 123
    elif state < 1000:
        state = state * 5 + 44
    else:
        pass  # No change — misleading expectation of transformation
        
    return state

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == "__main__":
    # Real input data
    sensor_input = [12, 45, 12, 67, 45, 89, 12, 45, 33, 67]
    
    # Irrelevant variables and computations (distractors)
    backup_copy = sensor_input.copy()
    normalization_factor = sum(x ** 2 for x in backup_copy) ** 0.5
    normalized = [round(x / normalization_factor, 3) for x in backup_copy]
    checksum = sum(normalized) * 1000
    
    # Unused function calls (red herring)
    encrypted_layers = encrypt_sequence(sensor_input)
    audit_log = {"encrypted_checksum": sum(encrypted_layers) % 997}
    
    # Actual relevant processing path
    cleaned = preprocess_sensors(sensor_input)
    control_sequence = generate_control_vector(len(cleaned), seed=13)
    filtered = filter_anomalies(cleaned, threshold=100)  # Some side filtering
    transformed_data = [x + 1 for x in cleaned]  # Final relevant transform
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, control_sequence)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")