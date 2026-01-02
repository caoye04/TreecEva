import math

# Simulated system telemetry data with mixed relevance
def generate_logs():
    raw_data = [15, 23, 8, 42, 7, 19, 4, 31, 11, 27, 5, 34, 9]
    timestamps = [t * 0.87 for t in range(len(raw_data))]  # Irrelevant time scaling
    log_entries = []
    for i in range(len(raw_data)):
        entry = {
            'id': i + 1000,
            'value': raw_data[i],
            'timestamp': timestamps[i],
            'checksum': (raw_data[i] ^ 255) + 10,  # Distractor computation
            'flagged': raw_data[i] > 30
        }
        log_entries.append(entry)
    return log_entries

# Decoy function – looks relevant but unused in critical path
def analyze_anomalies(entries):
    anomalies = 0
    for e in entries:
        if e['value'] % 7 == 0 and e['flagged']:
            anomalies += 1
    return anomalies

# Auxiliary transformation – partially relevant but contains red herrings
def extract_signals(entries):
    signals = [e['value'] for e in entries if e['value'] % 2 == 1]  # Only odd values kept
    filtered = [s for s in signals if s > 10]  # Additional filter
    normalized = [round(s / 3.0, 2) for s in filtered]  # Red herring: not used later
    return filtered  # Critical return

# Bit manipulation layer – includes misleading shifts and masks
def compute_diagnostic(signal_list):
    base = 0
    for val in signal_list:
        temp = (val << 2) ^ 17  # Left shift and XOR – distractor
        if temp > 100:
            base += val % 13
        else:
            base += (val + 5) // 2  # Integer division used
    return base

# Main processing chain with decoy logic paths
def validate_integrity(entries):
    total = 0
    for e in entries:
        total += e['checksum']  # Uses irrelevant field
    return total % 19 == 0  # Dead-end boolean check

# Core aggregation with sorting red herring
def aggregate_trends(values):
    sorted_vals = sorted(values, reverse=True)
    top_half = sorted_vals[:len(sorted_vals)//2]
    return sum(top_half) * 0.95  # Not actually used in final result

# Final metric processor – only this affects the answer
def process_metrics(entries, threshold):
    # Step 1: Extract relevant signal values
    signals = extract_signals(entries)
    
    # Step 2: Apply threshold filtering (key operation)
    active_signals = [s for s in signals if s >= threshold]
    
    # Step 3: Character counting distraction (string conversion with no impact)
    hex_codes = [hex(s)[2:] for s in signals]
    char_count = sum(len(h) for h in hex_codes)  # Computed but unused
    
    # Step 4: Compute diagnostic using integer arithmetic
    diag_value = 0
    for x in active_signals:
        if x % 3 == 0:
            diag_value += int(math.sqrt(x))  # Truncating square root
        else:
            diag_value += (x + 1) // 2  # Integer division and rounding
    
    # Step 5: Apply bitwise adjustment (only one branch matters)
    if len(active_signals) > 3:
        diag_value = diag_value ^ 256  # Unused path
    else:
        diag_value = (diag_value << 1) + 7  # Key transformation: left shift and add
    
    # Step 6: Final adjustment with irrelevant trigonometric call
    angle = math.radians(diag_value % 90)
    dummy_correction = int(100 * math.sin(angle))  # Calculated but ignored
    
    return diag_value

# Orchestration block
if __name__ == '__main__':
    # Generate logs
    logs = generate_logs()
    
    # Run decoy analysis (no effect on output)
    anomaly_count = analyze_anomalies(logs)
    integrity_ok = validate_integrity(logs)
    
    # Extract core signals
    signal_values = extract_signals(logs)
    
    # Compute side metrics (distractors)
    trend_score = aggregate_trends(signal_values)
    base_diagnostic = compute_diagnostic(signal_values)
    
    # Real threshold for activation
    system_threshold = 15
    
    # Critical execution point
    final_diagnostic = process_metrics(logs, system_threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")