import itertools

# System diagnostics module for signal processing pipeline

def collect_timing_samples(base_offset, sample_count):
    samples = []
    accumulator = base_offset
    for i in range(sample_count):
        if i % 3 == 0:
            accumulator += (i * 2) + 1
        elif i % 5 == 0:
            accumulator -= (i // 2)
        else:
            accumulator ^= (i & 7)
        samples.append(accumulator)
    return samples

# Irrelevant auxiliary function - dead code path
def deprecated_normalization(data):
    factor = 0.98
    return [x * factor for x in data if x > 0]

# Signal calibration logic
def generate_calibration_mask(length):
    mask = [0] * length
    for i in range(length):
        if i < length // 3:
            mask[i] = (i + 1) * 3
        elif i < 2 * length // 3:
            mask[i] = (i + 5) ** 0.5
        else:
            mask[i] = abs(i - length) * 2
    return mask

# Complex data transformation with slicing and filtering
def filter_anomalies(raw_data, threshold=150):
    filtered = []
    window_size = 5
    for i in range(len(raw_data)):
        start = max(0, i - window_size // 2)
        end = min(len(raw_data), i + window_size // 2 + 1)
        local_window = raw_data[start:end]
        avg = sum(local_window) / len(local_window)
        if abs(raw_data[i] - avg) < threshold:
            filtered.append(raw_data[i])
    return filtered

# Decoy function using itertools - not actually used in main flow
def generate_combinations():
    items = [1, 2, 3, 4]
    combo_result = []
    for r in range(1, 4):
        combo_result.extend(list(itertools.combinations(items, r)))
    return len(combo_result)

# Core metric aggregator - this will be called
def compute_signal_quality(measurements):
    quality_scores = []
    for val in measurements:
        if isinstance(val, int) and val > 0:
            score = (val % 17) * 1.25
        elif isinstance(val, float):
            score = round(val / 3.7, 2)
        else:
            score = 0.5
        quality_scores.append(score)
    return [q for q in quality_scores if q > 1.0]

# Main aggregation logic
def aggregate_metrics(log_data, calib):
    # Misleading intermediate variables
    temp_buffer = log_data[::2]  # slicing every other element
    scratch_pad = [x * 1.1 for x in calib[:len(log_data)]]
    
    # Real computation begins
    weighted_sum = 0.0
    for i in range(min(len(log_data), len(calib))):
        if i % 4 == 0:
            contribution = log_data[i] * (calib[i] / 8.0)
        elif i % 4 == 1:
            contribution = (log_data[i] + calib[i]) * 0.33
        elif i % 4 == 2:
            contribution = (log_data[i] ^ (i & 15)) * 0.75  # bitwise distraction
        else:
            contribution = abs(log_data[i] - calib[i]) * 1.2
        weighted_sum += contribution
    
    # Secondary adjustment based on filtered characteristics
    valid_entries = [x for x in log_data if x > 10]  # list comprehension
    adjustment_factor = len(valid_entries) * 0.42
    
    # Final diagnostic calculation
    final_diagnostic = int(weighted_sum - adjustment_factor + 5)
    
    # Unused but plausible-looking computations
    shadow_metric = sum(scratch_pad) / len(scratch_pad) if scratch_pad else 0
    backup_check = ''.join([chr(i % 26 + 97) for i in log_data[:3]])  # red herring
    
    return final_diagnostic

# Entry point
if __name__ == '__main__':
    # Generate primary data streams
    timing_log = collect_timing_samples(base_offset=13, sample_count=25)
    calibration_sequence = generate_calibration_mask(30)
    
    # Spurious operations to distract
    _ = deprecated_normalization(timing_log)
    _ = generate_combinations()
    _ = filter_anomalies(calibration_sequence, threshold=200)
    
    # Actual critical execution point
    final_diagnostic = aggregate_metrics(timing_log, calibration_sequence)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")