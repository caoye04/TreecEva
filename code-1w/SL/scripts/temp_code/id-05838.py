def normalize(value, min_val, max_val):
    """Irrelevant normalization function (distractor)"""
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0


def decode_signal(sequence):
    """Decodes bit-like patterns in string sequences (partially relevant)"""
    count = 0
    for char in sequence:
        if char in '1A':  # Simulate binary presence
            count += 1
    return count % 7

def accumulate_diagnostics(logs):
    """Accumulates diagnostic codes (red herring)"""
    total = 0
    for log in logs:
        if isinstance(log, str) and 'ERR' in log:
            total += 1
    return total * 100

def extract_features(data_list):
    """Extracts numeric features from mixed data (distractor with side relevance)"""
    features = []
    for item in data_list:
        if isinstance(item, str):
            cleaned = item.strip('X').replace('-', '')
            if cleaned.isdigit():
                features.append(int(cleaned))
    return features

def filter_outliers(values, limit=500):
    """Removes values above limit (misleading filter)"""
    return [v for v in values if v <= limit]

def compute_entropy(readings):
    """Computes pseudo-entropy from frequency distribution"""
    from math import log
    freq_map = {}
    for r in readings:
        freq_map[r] = freq_map.get(r, 0) + 1
    total = len(readings)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 6)

def analyze_readings(readings, thresh):
    """Core analysis function: counts readings above threshold"""
    count_above = 0
    for reading in readings:
        if reading > thresh:
            count_above += 1
    return count_above

# Simulated sensor data ingestion
raw_input = ['X123-', 'X456-', 'X789-', 'X101-', 'X202-', 'X303-', 'X404-', 'X505-']

# Step 1: Extract numerical values from strings (uses string method)
extracted_numbers = []
for entry in raw_input:
    digits = entry.strip('X').replace('-', '')
    if digits.isdigit():
        extracted_numbers.append(int(digits))

# Step 2: Apply irrelevant transformation chain
normalized_data = [normalize(x, 100, 999) for x in extracted_numbers]  # Distractor
smoothed_data = [x * 0.9 for x in extracted_numbers]  # Dead processing path

# Step 3: Simulate auxiliary diagnostic logs (irrelevant)
diag_logs = ['STATUS_OK', 'ERR_01', 'STATUS_OK', 'ERR_01', 'STATUS_OK']
diag_total = accumulate_diagnostics(diag_logs)  # Red herring variable

# Step 4: Filter data using misleading criteria (distractor logic)
clean_readings = filter_outliers(extracted_numbers, limit=400)  # Removes some values

# Step 5: Add back excluded values conditionally (complex misdirection)
temp_buffer = []
for val in extracted_numbers:
    if val not in clean_readings:
        temp_buffer.append(val - 100)  # Alters excluded values

# Step 6: Reconstruct dataset with transformed outliers
processed_data = clean_readings + temp_buffer  # Final data used

# Step 7: Compute irrelevant entropy feature
entropy_value = compute_entropy(processed_data)  # Looks important but unused in answer

# Step 8: Decode hidden pattern in original format (distraction)
signal_code = decode_signal(''.join([entry[1] for entry in raw_input]))  # Uses string indexing

# Step 9: Extract features again (redundant)
duplicate_features = extract_features(raw_input)

# Step 10: Critical execution point — actual answer computation
threshold = 400
final_diagnostic = analyze_readings(processed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")