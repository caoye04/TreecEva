from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition
def acquire_sensor_data():
    raw_signals = [
        'A1:23.5|B2:45.1|C3:67.8',
        'A1:24.3|B2:44.7|C3:68.0',
        'A1:23.9|B2:45.3|C3:67.5'
    ]
    return raw_signals

# Parse raw string signals into numeric readings
def parse_signals(raw_signals):
    parsed = defaultdict(list)
    for entry in raw_signals:
        parts = entry.split('|')
        for part in parts:
            sensor_id, value_str = part.split(':')
            parsed[sensor_id].append(float(value_str))
    return parsed

# Normalize values using z-score (irrelevant for final result)
def normalize_readings(data):
    normalized = {}
    for key, values in data.items():
        mean_val = sum(values) / len(values)
        std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
        normalized[key] = [(x - mean_val) / (std_dev + 1e-9) for x in values]
    return normalized

# Calculate moving average – red herring function, not used later
def smooth_signal(signal_list, window=2):
    smoothed = []
    for i in range(len(signal_list)):
        start = max(0, i - window)
        smoothed.append(sum(signal_list[start:i+1]) / (i - start + 1))
    return smoothed

# Transform A1 readings through multiple steps
def process_a1_series(a1_values):
    squared_chain = [x ** 2 for x in a1_values]
    shifted = [y - 500 for y in squared_chain]  # Bring into negative range
    adjusted = [z + 10 for z in shifted]        # Minor correction
    return adjusted

# Dummy transformation for B2 – dead code path
def transform_b2(b2_values):
    log_scaled = [math.log(x + 1) for x in b2_values]
    reversed_order = log_scaled[::-1]
    return [round(r, 2) for r in reversed_order]

# Core processing function with meaningful computation
def compute_entropy(values):
    count_dict = Counter([round(v, 1) for v in values])
    total = len(values)
    entropy = 0.0
    for count in count_dict.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Analyze signal using computed metrics
def analyze_signal(data):
    # Extract relevant processed stream
    primary_stream = data.get('diagnostics', [])
    
    # Redundant checks and misleading branches
    if len(primary_stream) == 0:
        fallback = data.get('backup', [0]*5)
        return sum(fallback) % 100
    elif len(primary_stream) > 10:
        truncated = primary_stream[:10]
        return sum(truncated) // len(truncated)
    else:
        # Actual logic path
        base_score = sum(primary_stream)
        adjustment_factor = len(primary_stream) * 0.5
        temp_key = base_score * adjustment_factor
        
        # Apply non-linear correction based on character count in dummy string
        metadata_tag = "DX_LOG_2024"
        char_shift = len(metadata_tag.lower().replace("_", ""))  # 8 characters
        final_adjustment = temp_key - (char_shift ** 2)  # subtract 64
        
        # Additional distraction: unused conditional
        if 'X' in metadata_tag:
            final_adjustment += 100  # never executed
        
        return int(final_adjustment)

# Irrelevant utility: counts vowels in header (distractor)
def count_vowels_in_headers(headers):
    vowels = 'aeiou'
    total = 0
    for h in headers:
        total += sum(1 for c in h if c.lower() in vowels)
    return total

# Main execution flow
if __name__ == "__main__":
    # Step 1: Acquire raw data
    raw_data = acquire_sensor_data()
    
    # Step 2: Parse into structured format
    parsed_data = parse_signals(raw_data)
    
    # Step 3: Normalize (not used in final path)
    normalized_data = normalize_readings(parsed_data)
    
    # Step 4: Process A1 series through transformation chain
    processed_a1 = process_a1_series(parsed_data['A1'])  # [547.56, 590.49, 571.21] -> [-452.44, -409.51, -428.79]
    
    # Step 5: Compute entropy of A1 as diagnostic feature
    entropy_metric = compute_entropy(parsed_data['A1'])  # Based on original A1: [23.5, 24.3, 23.9]
    
    # Step 6: Build diagnostic vector
    diagnostics_vector = [
        abs(processed_a1[0]),      # 452.44
        abs(processed_a1[1]),      # 409.51
        abs(processed_a1[2]),      # 428.79
        entropy_metric * 100       # ~460.5 (since entropy ≈ 4.605)
    ]
    
    # Step 7: Prepare input structure for analysis
    processed_data = {
        'diagnostics': [int(round(x)) for x in diagnostics_vector],  # [452, 410, 429, 460]
        'source_count': len(raw_data),
        'backup': [10, 20, 30]
    }
    
    # Step 8: Final diagnostic calculation
    final_diagnostic = analyze_signal(processed_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")