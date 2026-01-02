import math

# Simulated sensor data processing with embedded logic anomalies
raw_readings = [14, 7, 23, 11, 5, 19, 3, 17]
def apply_filter(sequence):
    filtered = []
    for val in sequence:
        if val % 2 == 1:
            filtered.append(val * 3 + 1)
        else:
            filtered.append(val // 2)
    return filtered

# Irrelevant transformation: frequency analysis (dead-end computation)
def compute_frequency(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

frequency_diagnostic = compute_frequency(raw_readings)  # Distractor assignment

# Signal conditioning chain
conditioned_signal = apply_filter(raw_readings)
scaling_factor = 1.75
scaled_output = [round(x * scaling_factor) for x in conditioned_signal]

# Decoy system state (unused but plausible)
system_health = {
    'status': 'nominal',
    'anomaly_count': 0,
    'last_reset': 'N/A'
}

# Core logic: pattern analyzer with lambda-based threshold
defect_counter = 0
def detect_spikes(data):
    global defect_counter
    spike_count = 0
    for i in range(1, len(data)):
        if data[i] - data[i-1] > 10:
            spike_count += 1
            defect_counter += 1
    return spike_count

spike_index = detect_spikes(scaled_output)  # Intermediate result, partial relevance

# Red herring: checksum validation (never used)
total_checksum = sum(scaled_output) * 7 % 13

# Primary analysis function with embedded branching logic
def analyze_pattern(seq, threshold_fn):
    cumulative_score = 0
    history_log = []
    
    # Nested conditional with mixed arithmetic and logic
    for idx, val in enumerate(seq):
        if threshold_fn(val) and (idx + 1) % 3 != 0:
            adjustment = math.floor(math.log(val + 5, 2))
            if val > 40:
                adjustment -= 3
            elif val > 25:
                adjustment += idx % 4
            cumulative_score += adjustment * (idx % 5 + 1)
            history_log.append(cumulative_score)
        elif val % 7 == 0:
            cumulative_score -= 2  # Penalty branch
    
    # Secondary correction pass
    for log_val in history_log:
        if log_val % 6 == 0:
            cumulative_score += 1
    
    # Final modulation using bit manipulation
    modulated = cumulative_score ^ 0b1101
    modulated = (modulated << 1) & 0b111111  # Shift and mask
    modulated = modulated >> 1
    return modulated

# Threshold logic using lambda abstraction
critical_threshold = lambda x: x > 20

# Misleading auxiliary computation (distractor)
avg_value = sum(scaled_output) / len(scaled_output)
adjusted_avg = avg_value * 0.85 if avg_value > 25 else avg_value * 1.15

# Key statement that produces the target variable
final_diagnostic = analyze_pattern(scaled_output, critical_threshold)

# Dead code path: safety override (never invoked)
def trigger_override():
    system_health['status'] = 'override'
    return -999

# Result output (required format)
print(f"Result: {final_diagnostic}")