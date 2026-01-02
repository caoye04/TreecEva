from collections import defaultdict, Counter
import itertools

# Simulated system telemetry processing with diagnostic filtering

def analyze_latency_bursts(latency_samples):
    burst_count = 0
    current_streak = 0
    threshold = 85
    for sample in latency_samples:
        if sample > threshold:
            current_streak += 1
        else:
            if current_streak >= 3:
                burst_count += 1
            current_streak = 0
    if current_streak >= 3:
        burst_count += 1
    return burst_count


def compute_packet_loss_rate(sent, received):
    # Irrelevant helper - distractor
    if sent == 0:
        return 0.0
    return (sent - received) / sent * 100


def generate_sequence_signature(data_stream):
    # Complex but irrelevant transformation
    signature = 0
    for i, val in enumerate(data_stream):
        signature ^= (val << (i % 8))
    return signature & 0xFFFF

# Main telemetry data (simulated)
timing_log = [78, 92, 94, 88, 76, 95, 96, 97, 83, 72, 70, 91, 93, 94, 87]
data_frames = [255, 192, 128, 64, 32, 16, 8, 4, 2, 1]
error_counters = {"E1": 5, "E2": 3, "E3": 0, "E4": 7}

# Distractor variables and dead computations
redundant_shift = (sum(data_frames) >> 3) & 0xFF
rolling_hash = 0
for b in data_frames:
    rolling_hash = (rolling_hash * 31 + b) % 10007

# Unused statistical summary
frame_stats = {
    'min': min(data_frames),
    'max': max(data_frames),
    'avg': sum(data_frames) / len(data_frames)
}

# Simulated failure flags from various subsystems
failure_flags = [
    len(error_counters) > 5,
    analyze_latency_bursts(timing_log) >= 2,
    any(value > 100 for value in timing_log),
    sum(1 for x in timing_log if x > 90) < 4
]

# Auxiliary diagnostic: not used in final result
baseline_deviation = abs(len(timing_log) - 10) * 1.5

# Complex aggregation using collections
def aggregate_metrics(log, flags):
    stats = defaultdict(int)
    critical_events = 0

    # Real logic path
    for val in log:
        if val > 90:
            stats['high'] += 1
        elif val > 75:
            stats['moderate'] += 1
        else:
            stats['normal'] += 1

    # Key decision logic interwoven with noise
    temp_result = 0
    for flag in flags:
        if flag:
            temp_result += 1
    temp_result *= 2

    # Actual core computation
    sequence_pairs = list(itertools.combinations([x for x in log if x > 85], 2))
    pair_proximity = sum(1 for a, b in sequence_pairs if abs(a - b) <= 5)

    # Multi-concept integration: bit manipulation + counting
    encoded_state = 0
    for i, flag in enumerate(flags):
        if flag:
            encoded_state |= (1 << i)
    
    popcount = bin(encoded_state).count('1')
    
    # Final metric synthesis - this is where answer comes from
    raw_score = stats['high'] * 10 + pair_proximity * 3 + popcount * 5
    
    # Misleading adjustment (never executed due to logic)
    if baseline_deviation > 100:  # Impossible
        raw_score -= 50
    
    # Correct path
    final_adjustment = 4 if len(sequence_pairs) > 5 else -2
    
    final_diagnostic = raw_score + final_adjustment
    
    return final_diagnostic

# Dead function - never called
def debug_dump_system_state():
    return {"state": "healthy", "code": 200}

# Trigger key computation
final_diagnostic = aggregate_metrics(timing_log, failure_flags)

# Output required result
print(f"Result: {final_diagnostic}")