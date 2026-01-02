from collections import defaultdict, Counter
import math

# Simulated telemetry data from distributed system nodes
telemetry_streams = {
    'node_7': [14, 17, 23, 14, 19, 23, 14],
    'node_12': [88, 92, 88, 95, 92, 88],
    'node_21': [61, 63, 61, 60, 63, 61, 63, 61]
}

# Irrelevant cache warm-up routine (distractor)
warm_cache = [math.sqrt(i) for i in range(100) if i % 17 == 0]

# System health thresholds (mixed relevance)
thresholds = defaultdict(lambda: 50)
thresholds.update({'cpu': 90, 'memory': 85, 'latency': 200, 'retry_count': 5})

# Misleading aggregation function that is never called
def analyze_staleness(records):
    return sum(1 for r in records if r > 75) / len(records) if records else 0

# Auxiliary transformation with partial relevance
def extract_patterns(sequence):
    freq = Counter(sequence)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    return sorted(modes)

# Decoy state tracker (unused but plausible)
current_lock_state = {'active': True, 'priority': 7, 'timeout': None}

# Simulated log metadata with red herring fields
log_metadata = {
    'version': '3.7.1',
    'compression': 'lz4',
    'batch_size': 1024,
    'checksum_valid': True,
    'replica_count': 3
}

# Core processing pipeline
system_state = {
    'nodes_active': 27,
    'quorum_reached': True,
    'leader_epoch': 14,
    'failure_mask': 0b1010101010101010
}

log_data = []
for node_id, readings in telemetry_streams.items():
    # Extract most frequent reading per node
    pattern = extract_patterns(readings)
    primary_mode = pattern[0] if pattern else 0
    
    # Apply artificial distortion (bit manipulation red herring)
    distorted = primary_mode ^ int(node_id.split('_')[1])
    adjusted = distorted + (distorted >> 2)
    
    # Only this line contributes to final result
    normalized = abs(primary_mode - 10)  # Key contribution
    
    # Dead code path (conditional never taken due to design)
    if len(readings) < 5 and 'test' in node_id:
        normalized *= 2
        
    log_data.append(normalized)

# Secondary decoy calculation with plausible metrics
event_risk_score = 0
for val in [12, 15, 18, 21]:
    event_risk_score += (val % 7) * 3

# Unused anomaly detector
anomaly_registry = set()
for k, v in telemetry_streams.items():
    if len(v) % 2 == 1:
        anomaly_registry.add(k)

# Critical processing function with mixed logic
def process_metrics(metrics, state):
    # Irrelevant initialization block
    baseline = 0
    accumulator = defaultdict(int)
    for i in range(3):
        baseline += math.floor(10 * (i + 1) ** 0.5)
    
    # Process actual signal
    signal_sum = sum(metrics)  # Depends on normalized values from log_data
    
    # Complex but irrelevant branching
    modifier = 1
    if state['quorum_reached']:
        if state['leader_epoch'] > 10:
            temp_mask = state['failure_mask']
            ones = bin(temp_mask).count('1')
            zeros = bin(temp_mask).count('0') - 1  # ignore '0b' prefix
            parity = ones ^ zeros
            if parity % 3 == 0:
                modifier = 2
    
    # Red herring: unused transformation
    shadow_copy = [x * modifier for x in metrics]
    
    # Early termination check (never triggers in this input)
    if not state.get('initialized', False):
        return -999
    
    # Actual computation path
    intermediate = signal_sum * 17
    
    # Final adjustment using bit arithmetic distraction
    final_shift = (intermediate << 1) - (intermediate >> 1)
    
    # The true answer derivation
    result = final_shift // 100  # Integer division to stabilize
    
    # Distractor: floating point conversion that isn't used
    float_div = round(final_shift / 97.841, 4)
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)

# Output required format
print(f"Target result: {final_diagnostic}")