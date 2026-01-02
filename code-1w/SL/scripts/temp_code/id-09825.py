def process_node(value, mode='encode'):
    if mode == 'encode':
        return (value ^ 243) + 7
    else:
        return (value - 7) ^ 243

# Irrelevant signal processing chain (dead path)
def legacy_transform(x):
    return ((x << 3) | (x >> 2)) & 255

def generate_hamming_sequence(n):
    seq = [1]
    for i in range(1, n):
        seq.append(seq[-1] * 2 + (i % 3))
    return seq[:n]

def evaluate_health_status(signal_set, threshold):
    score = 0
    for s in signal_set:
        if s > threshold:
            score += 1
        elif s == threshold:
            score -= 1
    return score > 0

# Distractor: unused health check logic
def assess_stability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return variance < 50

def filter_anomalies(data_stream, limit=50):
    cleaned = []
    for item in data_stream:
        if 10 <= item <= 90 and item % 2 == 1:
            cleaned.append(item)
    return cleaned

# Core diagnostic logic with distractors
def analyze_pattern(signals, threshold):
    # Irrelevant preprocessing (distractor block)
    temp_buffer = [s * 2 + 3 for s in signals if s % 4 == 0]
    extended_data = temp_buffer + [threshold] * 2
n    checksum = 0
    for val in extended_data:
        checksum ^= val

    # Real computation begins here
    active_nodes = set()
    backup_queue = set()

    for idx, sig in enumerate(signals):
        processed = process_node(sig)
        if processed > threshold * 1.5:
            active_nodes.add(idx)
        if sig % 5 == 0:
            backup_queue.add(idx)

    # Use set operations meaningfully
    primary_focus = active_nodes - backup_queue
    if len(primary_focus) == 0:
        fallback_mode = True
        recovery_index = -1
        for i in range(len(signals)):
            if signals[i] < threshold and i not in backup_queue:
                recovery_index = i
                break
    else:
        fallback_mode = False
        recovery_index = min(primary_focus)

    # Complex conditional with red herring variables
    adjustment_factor = 0
    debug_trace = []
    for i in range(3):
        temp = (threshold >> i) & 1
        adjustment_factor += temp * (i + 1)
        debug_trace.append(temp)  # Unused trace

    # Final computation with multiple steps
    base_metric = sum(signals) // len(signals)
    peak_response = max(signals) - min(signals)
    influence_score = len(active_nodes) * 17

    intermediate = (base_metric + peak_response) * adjustment_factor
    if fallback_mode:
        intermediate -= 23
    else:
        intermediate += influence_score

    # Final diagnostic calculation
    final_diagnostic = intermediate + recovery_index

    # Dead code path - never executed due to logic above
    if len(backup_queue) > 100:
        emergency_override = True
        final_diagnostic *= 2

    return final_diagnostic

# Simulate collected signals
sequence_pool = generate_hamming_sequence(12)
collected_signals = [process_node(x, 'encode') for x in sequence_pool]
system_threshold = 350

# Key execution point
final_diagnostic = analyze_pattern(collected_signals, system_threshold)
print(f"Result: {final_diagnostic}")