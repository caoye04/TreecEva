from collections import defaultdict, Counter
from itertools import cycle, islice

def monitor_system_load(base_timestamps, thresholds):
    # Irrelevant transformation - distractor
    normalized = [t % 3600 for t in base_timestamps if t > 100]
    snapshot = defaultdict(lambda: 0)
    
    for i, val in enumerate(normalized):
        if i % 3 == 0:
            snapshot[f'node_{i % 5}'] += val * 0.1

    # Dead code path - misleading
    if len(snapshot) > 10:
        return sorted(snapshot.values(), reverse=True)
    else:
        temp_debug = sum(snapshot[k] for k in snapshot if 'node_2' in k)  # unused

    # Real but hidden logic begins
    trigger_events = []
    for i, t in enumerate(base_timestamps):
        if t % 7 == 0 and i % 4 != 0:
            trigger_events.append(i * 2 + (t % 9))
    return trigger_events

def evaluate_response_time(entries):
    # Unused function - red herring
    stats = Counter()
    for e in entries:
        stats['bucket_' + str(e % 4)] += 1
    return dict(stats)

def decode_signal_pattern(signal_sequence):
    # Bit manipulation decoy
    masked_values = []
    for s in signal_sequence:
        masked = (s << 2) ^ 0b1010
        if masked > 100:
            masked_values.append(masked % 50)
    return masked_values  # never used

def aggregate_metrics(log_entries, flags):
    state_track = defaultdict(int)
    timing_offsets = []    
    for entry in log_entries:
        if entry < 0:
            continue
        offset = (entry * 3) % 17
        timing_offsets.append(offset)
        state_track[offset] += 1

    # Core calculation buried in noise
    cumulative = 0
    for i, offset in enumerate(timing_offsets):
        if i % 2 == 0 and offset in flags:
            cumulative += offset * (i + 1)
    
    # Distractor: complex-looking but unused structure
    analysis_grid = [[(i + j) % 8 for j in range(5)] for i in range(len(timing_offsets)) if i % 3 == 0]
    grid_sum = sum(sum(row) for row in analysis_grid)  # looks important, not used

    # Actual answer derivation
    adjustment = 0
    for key, count in state_track.items():
        if count >= 2:
            adjustment += key // 2
    
    return cumulative - adjustment

# Main execution with extensive distractions
raw_timestamps = list(range(45, 68))
timing_log = monitor_system_load(raw_timestamps, thresholds=[1.0, 2.5])

# Fake data structures to mislead
response_profile = evaluate_response_time(raw_timestamps)
signal_input = [x ^ 3 for x in raw_timestamps]
decoded_noise = decode_signal_pattern(signal_input)

# Critical flag set - subtle but essential
system_flags = {x for x in timing_log if x % 4 == 1}
system_flags.add(999)  # red herring value
system_flags.discard(999)

# Decoy computations
snapshot_cycle = list(islice(cycle([1, 0, 1]), 0, 100))
shadow_weight = sum(snapshot_cycle[i] * i for i in range(0, 100, 7)) % 1000  # unused

# Key statement
final_diagnostic = aggregate_metrics(timing_log, system_flags)

print(f"Result: {final_diagnostic}")