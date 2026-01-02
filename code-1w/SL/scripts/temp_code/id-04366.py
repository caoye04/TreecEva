import itertools

def analyze_sequence(data, window_size):
    # Irrelevant helper function – never called in execution path
    return [sum(data[i:i+window_size]) for i in range(len(data)-window_size+1)]

def corrupt_signal(x):
    # Distractor function: looks important but unused
    return (x << 2) ^ 0xFF

def main():
    # Simulated system log data with diagnostic codes
    log_entries = [
        {'code': 200, 'latency': 120, 'size': 1024},
        {'code': 500, 'latency': 80,  'size': 512},
        {'code': 200, 'latency': 150, 'size': 2048},
        {'code': 404, 'latency': 90,  'size': 256},
        {'code': 200, 'latency': 110, 'size': 768}
    ]

    # System thresholds – some fields are red herrings
    system_thresholds = {
        'latency_cap': 100,
        'size_floor': 500,
        'error_codes': {500, 403, 404},
        'retries_allowed': 3,  # Unused field
        'bandwidth_limit': 10000  # Distractor
    }

    # Irrelevant list comprehensions and string operations
    status_labels = ['OK', 'Error', 'Timeout', 'Redirect']
    label_map = {i: label.lower() for i, label in enumerate(status_labels)}
    encoded_tags = [hash(label * 2) % 100 for label in status_labels]

    # Misleading bit manipulation block
    checksum = 0
    for i, tag in enumerate(encoded_tags):
        checksum ^= (tag << 1) | (i & 1)
    checksum = ~checksum & 0xFFFF  # Looks important, not used later

    # Real computation begins here
    valid_count = 0
    latency_sum = 0
    high_volume_count = 0

    # Primary analysis loop
    for entry in log_entries:
        code = entry['code']
        latency = entry['latency']
        size = entry['size']

        # Filter by error code exclusion
        if code not in system_thresholds['error_codes']:
            valid_count += 1
            latency_sum += latency

        # Track large payloads – only those above 1000 bytes
        if size > 1000:
            high_volume_count += 1

    # Compute average latency for non-error responses
    avg_latency = latency_sum / valid_count if valid_count > 0 else 0

    # Use zip to pair indices with high-volume entries (overkill, but idiomatic)
    volume_flags = [e['size'] > 1000 for e in log_entries]
    indexed_volume = list(zip(itertools.count(), volume_flags))
    first_high_vol_index = None
    for idx, is_high in indexed_volume:
        if is_high:
            first_high_vol_index = idx
            break

    # Dummy transformation using enumerate (distractor)
    transformed = []
    for i, entry in enumerate(log_entries):
        transformed.append(f"Entry{i}:{entry['code']}")
    serialized = "|".join(transformed)
    split_len = len(serialized.split('|'))  # Red herring

    # Core metric: weighted score combining multiple factors
    # Weight formula: (valid responses * 10) - (average latency) + (high volume bonus)
    high_volume_bonus = high_volume_count * 25
    weighted_score = (valid_count * 10) - avg_latency + high_volume_bonus

    # Final processing function defined inside main to obscure flow
    def process_metrics(entries, thresholds):
        # Nested filtering logic
        critical_count = 0
        total_priority = 0
        for e in entries:
            c = e['code']
            lat = e['latency']
            # Priority based on latency bands
            if lat > thresholds['latency_cap']:
                priority = 2
            elif c in thresholds['error_codes']:
                priority = 3
            else:
                priority = 1
            total_priority += priority
            if c == 500 and lat < 100:
                critical_count += 1  # Rare condition

        # Secondary metrics
        success_rate = sum(1 for e in entries if e['code'] == 200) / len(entries)
        adjusted_priority = total_priority * success_rate

        # Final diagnostic uses only a subset of computed values
        # Despite many variables, only weighted_score from outer scope matters
        local_diagnostic = int(weighted_score + adjusted_priority)
        return local_diagnostic

    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()