import itertools

# Simulated sensor data preprocessing with red herrings
def fetch_sensor_metadata():
    return {'version': '2.1', 'calibration': 0.98, 'units': 'mV'}

def legacy_checksum(data):
    # Unused legacy function (dead code path)
    return sum(d % 256 for d in data) // len(data)

def generate_time_vector(n):
    # Irrelevant time vector generation
    return [round(0.01 * i, 4) for i in range(n)]

def filter_outliers(data, threshold=30):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) < threshold]

def augment_data_sequence(data):
    # Adds mirrored data (distractor transformation)
    reversed_part = [x * 0.95 for x in reversed(data)]
    return data + reversed_part

def normalize_signal(data):
    max_val = max(data)
    return [round(x / max_val, 6) for x in data]

def extract_features_windowed(data, size=5):
    # Complex feature extraction with unused outputs
    features = []
    for i in range(0, len(data) - size + 1, size):
        window = data[i:i+size]
        avg = sum(window) / len(window)
        peak = max(window)
        entropy_like = round(sum(-abs(x) * 0.1 for x in window), 4)  # Fake entropy
        features.append((avg, peak, entropy_like))
    return features

def compress_data_rle(data):
    # Run-length encoding - irrelevant to final result
    compressed = []
    current, count = data[0], 1
    for x in data[1:]:
        if x == current:
            count += 1
        else:
            compressed.append((current, count))
            current, count = x, 1
    compressed.append((current, count))
    return compressed

def analyze_signal(data):
    # Core analysis logic
    filtered = [x for x in data if x > 0.5]  # Only values above threshold matter
    grouped = [list(group) for k, group in itertools.groupby(filtered, key=lambda x: x > 0.75)]
    lengths = [len(g) for g in grouped]
    
    # Critical computation
    primary_metric = sum(lengths[::2]) * 1.5 if lengths else 0
    secondary_metric = sum(1 for x in data if 0.6 < x < 0.85)
    
    # Final diagnostic calculation (answer depends only on this)
    final_diagnostic = int(primary_metric * 2 + secondary_metric * 3)
    
    # Dead assignment and decoy logic
    temp_analysis = {"score": final_diagnostic * 0.1, "status": "processed"}
    if temp_analysis["score"] > 10:
        temp_analysis["level"] = "high"
    else:
        temp_analysis["level"] = "low"
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    raw_data = [
        120, 140, 85, 90, 200, 210, 180,  # Raw voltage readings (will be normalized)
        75, 80, 95, 100, 110, 130, 150
    ]
    
    # Irrelevant metadata fetch
    metadata = fetch_sensor_metadata()
    
    # Time vector (unused)
    timestamps = generate_time_vector(len(raw_data))
    
    # Normalize signal
    scaled_data = [x * metadata['calibration'] for x in raw_data]
    normalized = normalize_signal(scaled_data)
    
    # Outlier filtering (no effect due to high threshold)
    cleaned = filter_outliers(normalized, threshold=30)
    
    # Augment with mirror (adds symmetric low values)
    extended = augment_data_sequence(cleaned)
    
    # Extract windowed features (not used in final logic)
    features = extract_features_windowed(extended)
    
    # Compress data (irrelevant)
    compressed = compress_data_rle([int(x * 100) for x in extended])
    
    # Processed data fed into analysis
    processed_data = extended  # This is what gets analyzed
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")