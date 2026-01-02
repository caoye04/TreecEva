import math

def analyze_pattern(sequence):
    # Irrelevant analysis function (dead end)
    count = 0
    for item in sequence:
        if isinstance(item, str) and 'error' in item.lower():
            count += 1
    return count

def transform_value(x):
    # Distractor: used in decoy path
    return (x ** 2 + 3 * x + 1) % 100

def decode_signal(signal):
    # Unused but plausible-sounding function
    return [int(s) for s in signal if s.isdigit()]

def filter_outliers(arr):
    mean_val = sum(arr) / len(arr)
    std_dev = (sum((x - mean_val) ** 2 for x in arr) / len(arr)) ** 0.5
    return [x for x in arr if abs(x - mean_val) <= 2 * std_dev]

def evaluate_threshold(state, limit=50):
    # Misleading intermediate logic
    temp_result = 0
    for i in range(len(state)):
        if i % 3 == 0:
            temp_result += state[i] * 2
        elif i % 4 == 0:
            temp_result -= state[i]
    return temp_result > limit

def compute_checksum(chunk):
    # Relevant but obfuscated part of processing
    checksum = 0
    for i, val in enumerate(chunk):
        if i % 2 == 0:
            checksum += val * 3
        else:
            checksum -= val
    return abs(checksum)

def extract_features(raw_data):
    # Extracts key values through string manipulation
    features = []
    for entry in raw_data:
        if isinstance(entry, str):
            clean = entry.strip().lower().replace('_', '').replace('-', '')
            if clean.isalpha():
                features.append(len(clean) % 25)
            elif clean.isdigit():
                features.append(int(clean) % 25)
            elif 'temp' in clean:
                features.append(15)
    return features

def process_sequence(stream):
    # Core logic embedded within distractions
    
    # Step 1: Extract numeric features from mixed stream using string methods
    feature_vector = extract_features(stream)
    
    # Step 2: Decoy usage — looks important but not affecting final output
    dummy_analysis = analyze_pattern(stream)
    temp_snapshot = [transform_value(x) for x in range(5)]
    
    # Step 3: Actual relevant transformation chain
    base_signal = [x * 4 + 7 for x in feature_vector]  # Linear transformation
    
    # Step 4: Filtering — only even indices matter
    filtered_signal = [base_signal[i] for i in range(len(base_signal)) if i % 2 == 0]
    
    # Step 5: Checksum computation on filtered data
    signal_hash = compute_checksum(filtered_signal)
    
    # Step 6: Conditional adjustment based on length parity
    if len(filtered_signal) % 2 == 1:
        signal_hash = (signal_hash + 113) % 897
    else:
        signal_hash = (signal_hash * 2) % 897
    
    # Step 7: Final non-linear mapping
    final_scalar = int(math.sin(math.radians(signal_hash)) * 1000) + 424
    
    # Step 8: Add constant derived from unused logic to obscure traceability
    final_scalar += 0  # No-op placeholder simulating interference
    
    return final_scalar

# Simulated sensor data stream with mixed types and red herrings
data_stream = [
    "ERROR_302",           # Triggers analyze_pattern but irrelevant
    "temp_read",           # Maps to 15 via extract_features
    "sensor_abc",          # len=10 → 10%25=10
    "status_ok",           # len=9 → 9%25=9
    "data-456",            # has digits? no direct use; treated as alpha -> len=8 → 8
    "heartbeat",           # len=9 → 9
    "TEMP_ALERT",          # triggers 'temp' → 15
    "normal_state"         # len=10 → 10
]

# Dead code paths that look active
unused_signal = decode_signal("A1B2C3")
evaluation_flag = evaluate_threshold([1, 2, 3, 4, 5])
cleaned_data = filter_outliers([10, 12, 15, 100, 14, 11])  # 100 is outlier

# Key execution point
final_output = process_sequence(data_stream)
print(f"Result: {final_output}")