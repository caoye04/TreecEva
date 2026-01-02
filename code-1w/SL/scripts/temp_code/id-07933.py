def process_timing_data(raw_intervals):
    adjusted_intervals = [x * 1.05 for x in raw_intervals if x > 0]
    cumulative_shift = 0
    for i, val in enumerate(adjusted_intervals):
        if i % 2 == 0:
            cumulative_shift += val ** 0.5
        else:
            cumulative_shift -= val / 100
    return cumulative_shift


def validate_checksum(sequence):
    checksum = 0
    for idx, num in enumerate(sequence):
        if idx % 3 == 0:
            checksum += num * 2
        elif idx % 3 == 1:
            checksum += num
        else:
            checksum -= num // 4
    return checksum % 17 == 0


def generate_calibration_points(base_seed):
    points = []
    temp = base_seed
    for _ in range(8):
        temp = (temp * 7 + 13) % 1000
        points.append(temp)
    return [p for p in points if p % 2 == 1]


def compute_entropy(signal):
    entropy = 0.0
    for s in signal:
        if s > 0:
            entropy -= s * __import__('math').log(s)
    return round(entropy, 4)


def aggregate_metrics(log_entries, calib_seq):
    timing_sum = sum(log_entries)
    offset = len(calib_seq) * 0.25
    adjustment_factor = 1.0
    
    # Distractor: irrelevant entropy computation
    dummy_signal = [0.1, 0.3, 0.6]
    _ = compute_entropy(dummy_signal)
    
    # Distractor: unused validation
    _ = validate_checksum(calib_seq)
    
    # Real logic path
    for i, entry in enumerate(log_entries):
        if i < len(calib_seq) and calib_seq[i] > 500:
            adjustment_factor *= 0.9
        elif entry > 100:
            adjustment_factor *= 1.1
    
    intermediate = timing_sum * adjustment_factor - offset
    
    # Distractor: dead code with misleading unpacking
    metadata_tags = ['A', 'B', 'C']
    status_flags = [True, False, True]
    for tag, flag in zip(metadata_tags, status_flags):
        _ = f"Debug: {tag}={flag}"  # unused
    
    # Core result computation
    diagnostic_score = 0
    for i, (t, c) in enumerate(zip(log_entries, calib_seq)):
        if i % 2 == 0:
            diagnostic_score += t // (c % 7 + 1)
        else:
            diagnostic_score -= (t % 5) * (c // 100)
    
    final_diagnostic = int(intermediate + diagnostic_score)
    return final_diagnostic

# Main execution
raw_timing_data = [120, -50, 200, 300, 180, 90, 250]
timing_log = process_timing_data(raw_timing_data)
calibration_sequence = generate_calibration_points(123)

# Irrelevant data structures - red herrings
diagnostic_cache = {f"entry_{i}": i*11 for i in range(10)}
system_snapshot = {"load": 0.75, "temp": 65, "uptime": 12400}

# Unused recursive function
def explore_tree(node_id, depth=0):
    if depth > 3:
        return 0
    return node_id + explore_tree(node_id+1, depth+1)

_ = explore_tree(5)

# Key assignment point
final_diagnostic = aggregate_metrics(timing_log, calibration_sequence)
print(f"Result: {final_diagnostic}")