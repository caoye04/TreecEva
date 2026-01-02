import math

# Simulated sensor array diagnostics with noise filtering and signal analysis
def collect_sensor_data():
    raw_values = [127, 255, 64, 192, 32, 224, 16, 240]
    noise_floor = 15
    filtered = [x for x in raw_values if x > noise_floor]  # Remove low-level noise
    return filtered

def apply_calibration(signal_batch):
    calibrated = []
    gain_factor = 1.05
    offset = -3.2
    temp_accumulator = 0  # Irrelevant tracking
    
    for val in signal_batch:
        corrected = (val * gain_factor) + offset
        if corrected > 100:
            temp_accumulator += 1  # Red herring counter
        calibrated.append(int(corrected))
    
    # Dead code path - never executed due to data range
    if len(calibrated) > 20:
        backup_mode = True
        calibrated = [x // 2 for x in calibrated]
    
    return calibrated

def compute_entropy(data):
    total = sum(data)
    probabilities = [ (x / total) for x in data if x > 0 ]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def detect_outliers(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    threshold = 2.5 * std_dev
    outliers = [x for x in values if abs(x - mean_val) > threshold]
    return outliers  # Computed but not used later

def flag_anomalies(pattern):
    flags = []
    for i in range(len(pattern)):
        if i > 0 and pattern[i] < pattern[i-1]:
            flags.append(i | 0b1000)  # Bitwise marking
    return flags if flags else [0]

def generate_checksum(sequence):
    checksum = 0
    for num in sequence:
        checksum ^= num  # XOR folding
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)  # Rotate left 1 bit
    return checksum & 0xFF

def normalize_signal(seq):
    max_val = max(seq)
    return [round(x / max_val, 6) for x in seq]

def aggregate_metrics(norm_seq, raw_seq):
    power = sum(x**2 for x in norm_seq)
    coherence = len([x for x in norm_seq if x > 0.5])
    stability = raw_seq[0] - raw_seq[-1] if len(raw_seq) > 1 else 0
    return {
        'power': power,
        'coherence': coherence,
        'stability': stability,
        'composite': power * 0.4 + coherence * 0.3 + abs(stability) * 0.3
    }

def analyze_readings(signals):
    if not signals:
        return -1
    
    # Step 1: Normalize
    normalized = normalize_signal(signals)
    
    # Step 2: Compute auxiliary metrics (some irrelevant)
    dummy_flag = flag_anomalies(signals)  # Result not used
    entropy_measure = compute_entropy(signals)
    
    # Step 3: Aggregate key metrics
    metrics = aggregate_metrics(normalized, signals)
    
    # Step 4: Apply diagnostic logic
    diagnostic_score = 0
    diagnostic_score += int(metrics['power'] * 100)
    diagnostic_score += metrics['coherence'] * 5
    diagnostic_score -= abs(metrics['stability']) // 10
    
    # Hidden dependency: entropy adjusts score only if above threshold
    if entropy_measure > 1.8:
        diagnostic_score += 17
    else:
        diagnostic_score -= 5
    
    # Final adjustment based on checksum (security check)
    chk = generate_checksum(signals)
    if chk % 7 == 0:
        diagnostic_score += 3
    
    return diagnostic_score

# Main execution flow
raw_sensor_data = collect_sensor_data()
processed_signals = apply_calibration(raw_sensor_data)
extraneous_stats = detect_outliers(processed_signals)  # Unused result
intermediate_diagnostic = compute_entropy(processed_signals)  # Distractor variable
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")