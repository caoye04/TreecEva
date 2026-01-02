import math

def preprocess_logs(raw):
    # Irrelevant preprocessing with decoy transformations
    cleaned = [r.strip().lower() for r in raw if r]
    filtered = [c for c in cleaned if 'error' not in c and 'timeout' not in c]
    return [f.split(' ') for f in filtered]

def compute_hash(sequence):
    # Distractor: complex but unused hash function
    h = 0
    for s in sequence:
        h = (h * 31 + sum([ord(c) % 7 for c in s])) % 99991
    return h

def analyze_frequency(tokens):
    # Misleading frequency analysis (dead code path)
    freq = {}
    for t in tokens:
        for w in t:
            freq[w] = freq.get(w, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: -x[1])
    top_five = [k for k, v in sorted_freq[:5]]
    return len(top_five)

def extract_timestamps(log_blocks):
    # Unused timestamp extractor (red herring)
    timestamps = []
    for block in log_blocks:
        for entry in block:
            if entry.startswith('202') and ':' in entry:
                try:
                    ts = float(entry.split(':')[0]) % 1000
                    timestamps.append(ts)
                except:
                    continue
    return timestamps

def validate_integrity(data, threshold=0.85):
    # Decoy integrity check that looks important but is irrelevant
    total = len(data)
    valid_count = sum(1 for d in data if isinstance(d, list) and len(d) > 2)
    ratio = valid_count / total if total else 0
    return ratio >= threshold

def calculate_risk_factor(entries):
    # Another distractor: computes risk but never used
    base_risk = 0
    for e in entries:
        if len(e) > 4:
            base_risk += (len(e) * 7) % 13
    adjustment = math.sin(base_risk / 10) * 2
    return round(base_risk + adjustment, 3)

def decode_signals(packets):
    # Bit manipulation decoy with XOR shifts
    signal_value = 0
    for p in packets:
        for char in p:
            signal_value ^= ord(char) << 2
            signal_value %= 65536
    return signal_value & 0xFFFF

def aggregate_performance(log_data, weight_map):
    # Core relevant logic hidden among noise
    token_lengths = [len(entry) for entry in log_data if len(entry) > 0]
    
    # Step 1: Count non-empty entries
    count = len(token_lengths)
    
    # Step 2: Compute average length
    avg_len = sum(token_lengths) / count if count else 0
    
    # Step 3: Find maximum length
    max_len = max(token_lengths) if token_lengths else 0
    
    # Step 4: Count entries above average
    above_avg = sum(1 for l in token_lengths if l > avg_len)
    
    # Step 5: Apply modular arithmetic weighting
    mod_weight = (max_len * 17) % 23
    
    # Step 6: Use set to eliminate duplicates in flattened data
    flat_tokens = [item for sublist in log_data for item in sublist]
    unique_tokens = len(set(flat_tokens))
    
    # Step 7: Combine using weight map values
    w1 = weight_map['base']      # 3
    w2 = weight_map['diversity'] # 5
    w3 = weight_map['balance']   # 2
    
    # Step 8: Final score computation
    diversity_score = unique_tokens * w2
    balance_score = abs(count - avg_len) * w3
    base_score = (avg_len + max_len + above_avg) * w1
    
    # Step 9: Aggregate
    final_score = base_score + diversity_score - balance_score
    
    # Step 10: Clamp via modular constraint
    final_score = int(final_score % 99997)
    
    return final_score

# Main execution with extensive irrelevant setup
if __name__ == '__main__':
    # Real input data
    raw_log_input = [
        'USER LOGIN SUCCESS',
        'FILE ACCESS GRANTED DATA_READ',
        'ENCRYPTION ENABLED AES256',
        'SESSION REFRESH TOKEN_RENEWED',
        'DATA TRANSFER COMPLETE SIZE_1024',
        'SECURITY CHECKPOINT PASSED',
        'CACHE CLEARED TEMP_FILES_DELETED'
    ]

    # Irrelevant hashes
    _ = compute_hash(raw_log_input)
    _ = compute_hash([s[::-1] for s in raw_log_input])

    # Parse logs (only this matters)
    parsed_logs = preprocess_logs(raw_log_input)

    # More decoys
    _ = analyze_frequency(parsed_logs)
    _ = extract_timestamps(parsed_logs)
    _ = validate_integrity(parsed_logs, threshold=0.7)
    _ = calculate_risk_factor(parsed_logs)
    _ = decode_signals(raw_log_input)

    # Weight configuration (critical)
    weights = {
        'base': 3,
        'diversity': 5,
        'balance': 2
    }

    # Key statement
    final_score = aggregate_performance(parsed_logs, weights)
    print(f"Result: {final_score}")