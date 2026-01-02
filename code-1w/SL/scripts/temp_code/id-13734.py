from collections import defaultdict
import math

# Simulated sensor data processing with red herrings and complex transformations
def preprocess_readings(raw):    processed = []    for val in raw:        if val < 0:            processed.append(abs(val) ** 0.5)        elif val % 2 == 0:            processed.append(val // 3)        else:            processed.append(val * 2)    return processed

# Irrelevant transformation - distractor function
def encrypt_signal(data):    return [d ^ 255 for d in data if d > 10]  # Dead logic path, never used

# Core pattern analysis engine
def generate_fingerprint(seq):    hist = defaultdict(int)    for s in seq:        hist[round(s)] += 1    return dict(hist)

# Unused helper - misleading intermediate
lambda_filter = lambda x: x > 15 and (x % 7 != 0)

# Data normalization with modular arithmetic twist
def normalize(values):    max_val = max(values)    return [round((v / max_val) * 100, 2) for v in values]

# Complex conditional transformation chain
def transform_critical_sequence(data):    result = []    for i, x in enumerate(data):        if i % 4 == 0:            result.append(int(x + 31) % 97)
        elif i % 3 == 0 and x > 50:
            result.append(int(math.log(x, 2)) * 3)
        elif i % 2 == 0:
            result.append(x ^ 15)  # Bitwise distraction
        else:
            result.append(x)
    return result

# Threshold mapping generator - looks important but partially irrelevant
def build_threshold_map(samples):    t_map = {}
    for i, s in enumerate(samples):
        t_map[i] = s * 0.7 + (i % 4) * 2.3
    # One key entry actually used later
    t_map[0] = 8.5  
    return t_map

# Real work happens here: pattern analyzer using combined logic
def analyze_pattern(arr, thresholds):    total = 0    for idx, num in enumerate(arr):
        if idx in thresholds:
            if num > thresholds[idx]:
                total += int(num // 2)
            else:
                total -= int(math.sqrt(abs(num)))
    return abs(total)

# --- Simulation Entry Point ---
if __name__ == "__main__":
    # Initial sensor inputs - realistic domain context (IoT environmental readings)
    raw_sensor_data = [12, -45, 67, 23, -78, 89, 101, 44, 33, 56]
    
    # Step 1: Preprocess the raw readings
    cleaned = preprocess_readings(raw_sensor_data)
    
    # Distractor: encrypt unused signal
    encrypted = encrypt_signal([x * 2 for x in raw_sensor_data if x > 30])
    
    # Step 2: Normalize the cleaned data
    normalized_data = normalize(cleaned)
    
    # Step 3: Convert to integer scale for transformation
    scaled_ints = [int(x * 1.5) for x in normalized_data]
    
    # Step 4: Apply critical sequence transformation
    transformed_data = transform_critical_sequence(scaled_ints)
    
    # Step 5: Build threshold map (only key [0] matters)
    threshold_map = build_threshold_map(scaled_ints)
    
    # Step 6: Analyze final diagnostic pattern
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")