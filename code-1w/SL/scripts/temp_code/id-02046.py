def analyze_component_health(reading, baseline, tolerance=0.1):
    return abs(reading - baseline) <= tolerance * baseline

def generate_diagnostics(data_stream):
    stats = {}
    anomalies = []
    total = 0
    for val in data_stream:
        total += val
    avg = total / len(data_stream) if data_stream else 0
    
    # Irrelevant transformation (distractor)
    hex_codes = [hex(int(x))[2:] for x in data_stream]
    checksum = sum(int(c, 16) for c in hex_codes if c.isdigit())
    
    # Real logic masked by noise
    threshold = avg * 1.5
    count_valid = 0
    for x in data_stream:
        if x > threshold:
            anomalies.append(x)
        else:
            count_valid += 1
    stats['valid_count'] = count_valid
    stats['anomalies'] = len(anomalies)
    return stats

def encode_sequence(seq):
    # Dead function - never used in main logic
    return ''.join(chr((int(s) % 26) + 97) for s in seq if str(s).isdigit())

def decode_payload(payload):
    # Decoy function with misleading intermediate results
    temp = []
    for p in payload:
        if isinstance(p, str) and p.isalpha():
            temp.append(ord(p.lower()) - 96)
    return [t**2 for t in temp]

def filter_critical_entries(entries, flags):
    # Unused filtering path (red herring)
    result = []
    for e, f in zip(entries, flags):
        if f & 0x01 and not (f & 0x08):
            result.append(e * 2)
    return result

def compute_aggregate_score(records):
    # Complex but irrelevant scoring mechanism
    score = 0
    for r in records:
        if 'q' in r:
            score += len(r.split('q'))
    return score * 1.75

def extract_timestamp_signals(raw_logs):
    # Extracts numeric parts from log strings
    signals = []    
    for log in raw_logs:
        digits = ''.join([c for c in log if c.isdigit()])
        if digits:
            signals.append(int(digits[:4]))  # First 4 digits as signal
    return signals

def validate_signal_integrity(signal_list, pattern_mask=[3, 7, 1]):
    # Bit manipulation distractor
    validated = []
    mask_cycle = 0
    for s in signal_list:
        masked = s ^ pattern_mask[mask_cycle % 3]
        if bin(masked).count('1') % 2 == 0:  # Even parity
            validated.append(masked)
        mask_cycle += 1
    return validated

def process_metrics(log_entries, system_thresholds):
    # Core logic embedded in distractions
    
    # Step 1: Extract numerical signals from logs
    raw_signals = extract_timestamp_signals(log_entries)
    
    # Step 2: Validate integrity using XOR mask (partially relevant)
    clean_signals = validate_signal_integrity(raw_signals)
    
    # Step 3: Compute base metric
    base_metric = sum(clean_signals) / len(clean_signals) if clean_signals else 0
    
    # Step 4: Apply thresholds
    upper_lim = system_thresholds.get('max', 9000)
    lower_lim = system_thresholds.get('min', 100)
    
    # Step 5: Count out-of-bound signals
    oob_count = 0
    for sig in clean_signals:
        if sig > upper_lim or sig < lower_lim:
            oob_count += 1
    
    # Step 6: Calculate adjustment factor
    adjustment = 1.0
    if oob_count > 0:
        adjustment = (len(clean_signals) - oob_count) / len(clean_signals)
    
    # Step 7: Apply secondary correction based on string length patterns
    total_char_weight = 0
    for entry in log_entries:
        stripped = entry.strip().lower()
        vowel_count = sum(1 for c in stripped if c in 'aeiou')
        consonant_count = sum(1 for c in stripped if c.isalpha() and c not in 'aeiou')
        if vowel_count > 0:
            total_char_weight += consonant_count / vowel_count
    char_factor = total_char_weight / len(log_entries) if log_entries else 0
    
    # Step 8: Final diagnostic computation
    final_diagnostic = int((base_metric * adjustment) + (char_factor * 100))
    
    # Red herring: unused intermediate
    diagnostic_code = encode_sequence([final_diagnostic])
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    
    # Simulated log entries with embedded numbers
    log_entries = [
        "LOG:ERR@2024-10-05T13:45:22Z|CODE=4096|SRC=MOD_A",
        "DEBUG|TIMESTAMP:20241005134601|VAL=7321|NODE=X7",
        "INFO|SEQ:8832|STATUS=OK|REGION=US-EAST",
        "CRITICAL|TIME=13:47:19|ID=5012|PRIORITY=HIGHEST",
        "UPDATE|REF=3099|VER=2.1.0|CHKSUM=AA1F"
    ]
    
    # System thresholds
    system_thresholds = {
        'min': 3000,
        'max': 8000,
        'crit_window': 60
    }
    
    # Misleading pre-processing (distractor)
    preliminary_analysis = [entry.split('|') for entry in log_entries]
    header_flags = [len(section) for section in preliminary_analysis]
    filtered_headers = filter_critical_entries(preliminary_analysis, header_flags)
    
    # Health check on dummy data (irrelevant)
    sensor_readings = [0.98, 1.02, 0.99, 1.01, 0.97]
    health_status = [analyze_component_health(r, 1.0) for r in sensor_readings]
    
    # Generate unused diagnostics
    dummy_data = [12, 15, 18, 22, 9]
    dummy_stats = generate_diagnostics(dummy_data)
    
    # Core call
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output result
    print(f"Target result: {final_diagnostic}")