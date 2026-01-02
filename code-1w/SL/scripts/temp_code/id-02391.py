import itertools

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_signals = [18, 22, 15, 47, 33, 12, 8, 51]
    calibration_offsets = [3, -1, 2, 0, -2, 1, 4, -3]
    
    # Irrelevant transformation: frequency harmonics (dead path)
    harmonic_analysis = [x * 1.5 for x in raw_signals[::2]]
    normalized_power = [(x + y) ** 0.5 for x, y in zip(raw_signals, calibration_offsets)]
    
    # Core data preparation
    adjusted_readings = [raw_signals[i] + calibration_offsets[i] for i in range(len(raw_signals))]
    grouped_batches = list(itertools.batched(adjusted_readings, 4))  # Python 3.12+ batched

    # Decoy statistical summary (not used later)
    mean_reading = sum(adjusted_readings) / len(adjusted_readings)
    variance_proxy = sum((x - mean_reading) ** 2 for x in adjusted_readings)
    entropy_approx = len(set(adjusted_readings)) / len(adjusted_readings)

    # Real processing begins: filter anomalies using dynamic thresholds
    def detect_anomalies(data, base_threshold=20):
        result_flags = []
        for val in data:
            dynamic_t = base_threshold + (val // 10)
            is_alert = val > dynamic_t and (val % 3 != 0)
            result_flags.append(1 if is_alert else 0)
        return result_flags

    # Apply anomaly detection per batch
    alert_patterns = []
    for batch in grouped_batches:
        pattern = detect_anomalies(batch)
        alert_patterns.extend(pattern)

    # Red herring: bit manipulation on offsets (unused)
    shifted_mask = 0
    for offset in calibration_offsets:
        shifted_mask ^= (abs(offset) << 2) | (offset & 3)
    inverted_mask = (~shifted_mask) & 255

    # Construct threshold map with dummy entries
    threshold_map = {
        'low': lambda x: x < 18,
        'medium': lambda x: 18 <= x < 30,
        'high': lambda x: x >= 30,
        'critical': lambda x: x > 50  # unreachable due to data range
    }

    # Aggregation function with distractor logic
    def aggregate_batch(batch, flags):
        valid_sum = 0
        count = 0
        penalty_factor = 0.0  # unused distraction
        for val, flag in zip(batch, flags):
            if flag == 1:
                valid_sum += val * 1.1  # boosted contribution
            else:
                valid_sum += val * 0.9  # reduced contribution
            # Distractor computation chain
            temp_score = (val ** 2) / (flag + 1)
            adjustment = temp_score % 7
            penalty_factor += adjustment  # accumulated but unused
        return round(valid_sum)

    # Process each batch with corresponding alert pattern
    aggregated_data = []
    for i, batch in enumerate(grouped_batches):
        start_idx = i * 4
        end_idx = start_idx + 4
        flags = alert_patterns[start_idx:end_idx]
        aggregated_value = aggregate_batch(batch, flags)
        aggregated_data.append(aggregated_value)

    # Secondary decoy: recursive checksum (never called)
    def recursive_checksum(seq, pos=0):
        if pos >= len(seq):
            return 0
        return (seq[pos] * (pos + 1)) ^ recursive_checksum(seq, pos + 1)

    # Final processing function
    def process_readings(data_list, th_map):
        # Unused categorization
        categories = []
        for x in data_list:
            for name, pred in th_map.items():
                if pred(x):
                    categories.append(name)
                    break

        # Actual computation path
        base_total = sum(data_list)
        modifier = 0
        for i, val in enumerate(data_list):
            if val % 2 == 0:
                modifier += (i + 1) * 3
            else:
                modifier -= (i + 1) * 2
        
        # Key transformation
        intermediate = base_total + modifier
        # Final nonlinear adjustment
        final_score = int((intermediate * 0.85) + (len(data_list) ** 2.1))
        
        # Dead code: string encoding path
        encoded = ''.join(chr(97 + (x % 26)) for x in data_list)
        reversed_encoded = encoded[::-1]
        
        return final_score

    final_diagnostic = process_readings(aggregated_data, threshold_map)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

if __name__ == "__main__":
    collect_diagnostics()