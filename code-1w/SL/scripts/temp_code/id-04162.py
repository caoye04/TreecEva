from collections import defaultdict, Counter
import math

# Simulated telemetry data from distributed nodes
telemetry_streams = {
    'node_A': [14, 17, 14, 21, 17, 23, 14],
    'node_B': [9, 12, 9, 15, 12, 18, 9],
    'node_C': [5, 8, 5, 11, 8, 14, 5]
}

# Irrelevant historical stats (distractor)
historical_avgs = defaultdict(float)
for node, readings in telemetry_streams.items():
    historical_avgs[node] = sum(readings) / len(readings)

# System health thresholds (unused red herring)
thresholds = {'critical': 20, 'warning': 15, 'normal': 10}

# Simulate packet loss simulation (dead code path)
def simulate_packet_loss(rate, samples):
    import random
    return [random.random() > rate for _ in range(samples)]

# Unused helper (decoy function)
def analyze_bandwidth_usage(data):
    total = sum(len(str(x)) for x in data)
    return total * 0.75

# Core diagnostic engine
log_snapshot = []
for key, values in telemetry_streams.items():
    freq = Counter(values)
    mode_val = freq.most_common(1)[0][0]
    log_snapshot.append(mode_val)

# Misleading transformation chain
shadow_copy = [x + 2 for x in log_snapshot]
shadow_copy = [x * 1.5 for x in shadow_copy if x > 10]
baseline_offset = sum(shadow_copy) / len(shadow_copy) if shadow_copy else 0

# Real processing begins here
system_state = {}
system_state['active_nodes'] = len(telemetry_streams)
system_state['peak_sync'] = max(log_snapshot)
system_state['consensus'] = all(x == log_snapshot[0] for x in log_snapshot)

# Spurious noise injection (irrelevant)
noise_floor = 0
for i in range(3):
    for j in range(4):
        noise_floor += (i * j) % 3

# Actual metric processor
def extract_entropy(seq):
    counts = Counter(seq)
    entropy = 0.0
    total = sum(counts.values())
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def process_metrics(modes, state):
    # Step 1: Base score from entropy
    base_score = extract_entropy(modes) * 100
    
    # Step 2: Adjust by node count
    node_factor = state['active_nodes'] * 5
    
    # Step 3: Check consensus bonus
    consensus_bonus = 25 if state['consensus'] else 0
    
    # Step 4: Peak synchronization penalty
    peak_penalty = 0
    if state['peak_sync'] < 15:
        peak_penalty = 10
    
    # Step 5: Apply transformations
    intermediate = base_score + node_factor + consensus_bonus - peak_penalty
    
    # Step 6: Normalize through sigmoid-like curve
    normalized = int(intermediate / (1 + intermediate * 0.01))
    
    # Step 7: Mask with bit operation (XOR with fixed pattern)
    masked = normalized ^ 0b110101
    
    # Step 8: Final adjustment using unused baseline_offset (red herring usage but harmless)
    final_value = masked + int(baseline_offset * 0)  # Neutralized distractor
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(log_snapshot, system_state)
print(f"Target result: {final_diagnostic}")