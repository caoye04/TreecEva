def analyze_readings(readings):
    cumulative_score = 0
    for i, val in enumerate(readings):
        if i % 2 == 0:
            cumulative_score += val * 1.5
        else:
            cumulative_score -= val * 0.5
    return int(cumulative_score)

# Irrelevant preprocessing function (dead path)
def preprocess_signal(signal):
    filtered = [x * 0.95 for x in signal if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return normalized  # Never used

# Misleading transformation chain
def transform_sequence(seq):
    temp_result = []
    for idx, item in enumerate(seq):
        shifted = item << 2
        masked = shifted & 255
        temp_result.append(masked)
    reshaped = [temp_result[i:i+4] for i in range(0, len(temp_result), 4)]
    transposed = list(zip(*reshaped)) if len(reshaped) > 1 else reshaped
    return transposed  # Computationally heavy but unused

# Core logic disguised among distractors
def compute_baseline(data_chunk):
    total = 0
    count = 0
    for num in data_chunk:
        if num > 0 and num % 3 == 1:
            total += num ** 0.5
            count += 1
    return round(total / count, 4) if count else 0.0

# Another red herring: checksum validation (never invoked)
def validate_integrity(trace):
    checksum = 0
    for j, val in enumerate(trace):
        checksum ^= (val + j) % 256
    return format(checksum, '02x')

# Real processing begins here — obscured by prior noise
def extract_signatures(values, config):
    signatures = []
    for v in values:
        if config['mode'] == 'aggressive' and v > config['limit']:
            signatures.append(v * 3)
        elif config['mode'] == 'conservative':
            signatures.append(v * 2)
    return signatures or [0]

# Distractor: unused statistical summary
def generate_summary(samples):
    mean_val = sum(samples) / len(samples)
    variance = sum((x - mean_val) ** 2 for x in samples) / len(samples)
    peak_noise_ratio = max(samples) / (min(samples) + 1e-8)
    return {
        'mean': mean_val,
        'variance': variance,
        'ratio': peak_noise_ratio
    }

# Actual main computation path hidden in complexity
def process_metrics(dataset, criteria):
    # Step 1: Filter relevant entries
    filtered_data = [v for v in dataset if v >= criteria['floor']]
    
    # Step 2: Apply weighted scoring using enumerate
    weighted_sum = 0
    for index, value in enumerate(filtered_data):
        weight = 1.1 if index % 3 == 0 else 0.9
        weighted_sum += value * weight
    
    # Step 3: Count qualifying patterns with zip
    paired_checks = list(zip(filtered_data, filtered_data[1:]))
    rise_count = 0
    for prev, curr in paired_checks:
        if curr > prev and (prev + curr) % 2 == 1:
            rise_count += 1
    
    # Step 4: Combine with secondary metric
    base_metric = compute_baseline(filtered_data)
    auxiliary_score = analyze_readings(filtered_data)
    
    # Step 5: Decision logic with decoy variables
    threshold_met = auxiliary_score > 50
    volatility_index = len(paired_checks) / (rise_count + 1)
    adjustment_factor = 0.85 if volatility_index > 2.0 else 1.15
    
    # Step 6: Final aggregation (this produces the answer)
    intermediate = (weighted_sum + base_metric * 100) * adjustment_factor
    final_value = int(intermediate // 3)  # Integer division and rounding
    
    # Dead code below — looks important but unused
    diagnostic_log = {
        'entries': len(filtered_data),
        'adjusted': intermediate,
        'index': volatility_index,
        'noise_level': 'low' if rise_count > 5 else 'high'
    }
    
    # Correct result assigned here
    final_diagnostic = final_value
    return final_diagnostic

# Global decoy variables
system_status = 'nominal'
heartbeat_interval = 1000
payload_buffer = [0] * 16
active_mode_flag = False
sync_offset = 24.7

# Input data with meaningfully named variables
health_data = [12, 15, 18, 22, 27, 33, 40, 48, 57, 66, 76, 87, 99, 112]
thresholds = {
    'floor': 20,
    'limit': 50,
    'mode': 'aggressive'
}

# Trigger point: this assignment determines the answer
final_diagnostic = process_metrics(health_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")