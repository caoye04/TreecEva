import math

def collect_sensor_data():
    # Simulated sensor readings (relevant)
    return [14.2, 17.5, 23.1, 9.8, 31.0, 11.3, 25.7]

def filter_outliers(data, limit=35.0):
    # Irrelevant filtering (distractor - no outliers above 35)
    return [x for x in data if x < limit]

def transform_scale(readings):
    # Applies logarithmic scaling (red herring, not used in final path)
    return [math.log(x + 1) for x in readings]

def compute_rolling_average(data, window=3):
    # Dead code path - not used in main logic
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def generate_signature(values):
    # Unrelated hash-like operation (distractor)
    sig = 0
    for v in values:
        sig ^= int(v * 10) % 255
    return sig

def decode_flags(code_str):
    # Misleading bit manipulation (not part of critical path)
    flags = {}
    for i, c in enumerate(code_str):
        flags[f'flag_{i}'] = ord(c) & 0x01
    return flags

def normalize_readings(raw):
    base = min(raw)
    return [round((x - base) * 1.5, 2) for x in raw]  # Scale differences from minimum

def classify_range(val):
    if val < 10.0:
        return 'LOW'
    elif val < 20.0:
        return 'MEDIUM'
    else:
        return 'HIGH'

def build_category_map(items):
    # Uses dictionary and set operations (required Python features)
    categories = {}
    seen = set()
    for item in items:
        category = classify_range(item)
        if category not in seen:
            categories[category] = len(seen)
            seen.add(category)
    return categories

def apply_correction(values, factor=0.9):
    # Irrelevant correction (values are not actually corrected in final path)
    return [v * factor for v in values]

def recursive_sum(arr, n):
    # Simple recursion (suggested paradigm) - used in checksum
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

def calculate_checksum(data):
    # Used to derive a key threshold
    return recursive_sum([int(x) for x in data], len(data)) % 17

def process_diagnostics(raw_readings):
    # Core processing chain
    normalized = normalize_readings(raw_readings)
    
    # Distractor: transform with unused scale
    scaled = transform_scale(normalized)
    
    # Build category-to-index mapping using dict and set
    type_map = build_category_map(normalized)
    
    # Another red herring: signature generation
    _ = generate_signature(normalized)
    
    # Compute checksum used later
    chk = calculate_checksum(raw_readings)
    
    # Real work: categorize all values
    classifications = [classify_range(x) for x in normalized]
    
    # Create frequency map (dictionary op)
    freq = {}
    for cls in classifications:
        freq[cls] = freq.get(cls, 0) + 1
    
    # Construct threshold map based on checksum and categories
    base_threshold = 13.5 + chk
    threshold_map = {
        'LOW': base_threshold,
        'MEDIUM': base_threshold + 5.2,
        'HIGH': base_threshold + 12.7
    }
    
    # Return both processed data and thresholds
    return {'values': normalized, 'freq': freq}, threshold_map

def analyze_readings(data_dict, thresholds):
    readings = data_dict['values']
    freq = data_dict['freq']
    total = 0
    for val in readings:
        cat = classify_range(val)
        if val > thresholds[cat]:
            total += int(val)
    # Final diagnostic score
    return total + sum(freq.values())

# Main execution flow
if __name__ == '__main__':
    raw_data = collect_sensor_data()
    filtered_data = filter_outliers(raw_data)  # Distraction
    processed_data, threshold_map = process_diagnostics(filtered_data)
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    print(f"Result: {final_diagnostic}")