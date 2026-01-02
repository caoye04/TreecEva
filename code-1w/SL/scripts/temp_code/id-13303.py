def preprocess_logs(raw):
    cleaned = []
    for entry in raw:
        if 'ERROR' in entry or 'CRITICAL' in entry:
            cleaned.append(entry.strip().lower())
    return cleaned

# Irrelevant data transformation (distractor)
def encrypt_sequence(seq):
    return [pow(x, 3, 17) for x in seq]

# Decoy function with misleading intermediate output
def compute_health_score(metrics):
    score = 0
    for val in metrics:
        if val > 50:
            score += val * 0.1
    # This score is never used in final result
    return round(score, 4)

# Unused utility (dead code path)
def validate_checksum(data):
    checksum = 0
    for c in str(data):
        checksum ^= ord(c)
    return checksum == 0xFF

# Auxiliary function for bit analysis
def extract_signatures(flags):
    sig = 0
    for f in flags:
        if f & 0x8:
            sig ^= f >> 2
        elif f & 0x2:
            sig += f & 0x5
    return sig

# Core logic disguised among distractors
def evaluate_threshold(sequence, limit):
    temp = 0
    count = 0
    for num in sequence:
        if num < 0:
            continue
        temp += pow(num, 0.5) if num > 0 else 0
        count += 1
        if count >= limit:
            break
    return int(temp)

# String-based pattern analyzer with red herring computations
def detect_anomalies(entries):
    patterns = {"reboot": 0, "timeout": 0, "overflow": 0}
    decoy_sum = 0
    
    for line in entries:
        if 'reboot' in line:
            patterns["reboot"] += 1
        if 'timeout' in line:
            patterns["timeout"] += 2
        if 'overflow' in line:
            patterns["overflow"] += 3
        # Misleading accumulation
        decoy_sum += len(line) % 7
    
    # Real signal buried in noise
    anomaly_score = patterns["reboot"] * 10 + patterns["timeout"] * 5 + patterns["overflow"] * 2
    return anomaly_score  # Used later

# Main analysis combining multiple concepts
def analyze_pattern(logs, flags):
    # Step 1: Filter and normalize logs
    relevant_logs = [log for log in logs if 'CRITICAL' in log]
    processed = preprocess_logs(relevant_logs)
    
    # Step 2: Extract numeric traces (irrelevant to final answer but looks important)
    trace_data = [len(log.split()) for log in relevant_logs]
    masked_data = encrypt_sequence([x * 2 + 1 for x in trace_data])  # Dead end
    
    # Step 3: Compute decoy health metric (never used)
    _ = compute_health_score(trace_data)
    
    # Step 4: Analyze string patterns (this contributes)
    base_score = detect_anomalies(processed)
    
    # Step 5: Use flag signatures (contributes)
    flag_signature = extract_signatures(flags)
    
    # Step 6: Evaluate threshold on artificial sequence
    dummy_sequence = [abs(hash(log)) % 100 for log in logs]  # Includes all logs
    threshold_value = evaluate_threshold(dummy_sequence, 5)
    
    # Step 7: Combine real components with obfuscation
    adjustment = 0
    for i, log in enumerate(logs):
        if i % 3 == 0 and 'ERROR' in log:
            adjustment += len(log.split()[::-1][0])  # Last word length when index divisible by 3
    
    # Final computation: only base_score, flag_signature, and adjustment matter
    # Others are distractions
    final_diagnostic = (base_score + flag_signature) * 3 - adjustment
    
    # OUTPUT REQUIRED FOR EVALUATION
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data setup
raw_log_input = [
    "SYSTEM CRITICAL: reboot sequence initiated due to overflow",
    "NETWORK ERROR: timeout detected in node 3",
    "MEMORY CRITICAL: overflow in buffer 7",
    "DISK ERROR: write failure at sector 12",
    "SECURITY CRITICAL: unauthorized access attempt"
]

system_flags_config = [0x1A, 0x0C, 0x0F, 0x11, 0x09]

# Execution point of interest
final_diagnostic = analyze_pattern(raw_log_input, system_flags_config)