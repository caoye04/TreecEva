import math

# Irrelevant helper function (dead code path)
def unused_utility(x):
    return sum(i ** 2 for i in range(x))

# Misleading transformation chain
def transform_readings(readings):
    normalized = [r * 0.95 + 2.1 for r in readings if r > 0]
    filtered = [n for n in normalized if n < 100]
    stats = {
        'max_val': max(filtered),
        'min_val': min(filtered),
        'range': max(filtered) - min(filtered)
    }
    # Decoy statistic - not used later
    avg_sq = sum(x**2 for x in filtered) / len(filtered)
    return filtered, stats

# Another red herring: complex but unused data structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.index = 0

    def add(self, val):
        self.buffer[self.index] = val % 100
        self.index = (self.index + 1) % self.size

    def get_average(self):
        return sum(self.buffer) / len(self.buffer)

# Core computation buried in distractions
def analyze_sensor_data(data_packet):
    # Extract relevant payload (simulated packet structure)
    header = data_packet.get('header', {})
    payload = data_packet.get('payload', [])
    
    # Irrelevant metadata parsing
    version = header.get('version', 'N/A')
    timestamp = header.get('ts', 0)
    sensor_id = header.get('sid', -1)
    
    # Real processing begins here
    processed = []
    for item in payload:
        if isinstance(item, dict) and 'value' in item:
            raw = item['value']
            if raw < 0:
                continue
            adjusted = math.log(raw + 1) * 1.75
            processed.append(adjusted)
    
    # Secondary filtering
    valid_entries = [p for p in processed if p > 1.0]
    
    # Compute derived metrics (some irrelevant)
    count = len(valid_entries)
    total = sum(valid_entries)
    mean_val = total / count if count > 0 else 0
    
    # Red herring: bit manipulation on meaningless id
    sid_bits = sensor_id ^ 0xFF
    checksum = (sid_bits + timestamp) % 1000
    
    # Distractor: unused statistical moment
    if count > 0:
        variance_proxy = sum((x - mean_val)**2 for x in valid_entries) / count
        skew_hint = sum((x - mean_val)**3 for x in valid_entries) / count
    
    # Actual critical intermediate result
    base_score = mean_val * count * 0.85
    
    return {
        'base_score': base_score,
        'count': count,
        'mean': mean_val,
        'checksum': checksum,  # unused downstream
        'decoy_metric': variance_proxy if count > 0 else 0  # misleading
    }

# Higher-level fusion logic
def compute_aggregate(packets):
    results = []
    total_payload_size = 0
    
    for pkt in packets:
        payload_len = len(pkt.get('payload', []))
        total_payload_size += payload_len
        analysis = analyze_sensor_data(pkt)
        results.append(analysis)
    
    # Irrelevant scaling factor
    scale_factor = math.sqrt(total_payload_size) if total_payload_size > 0 else 1
    
    # Focus on base_score from each result
    scores = [res['base_score'] for res in results]
    
    # More distractions: attempt to fit line (unused)
    if len(scores) > 1:
        n = len(scores)
        slope_guess = (scores[-1] - scores[0]) / (n - 1) if n > 1 else 0
        intercept_guess = scores[0] - slope_guess * 0
    
    # Real aggregation
    raw_sum = sum(scores)
    penalty = len([s for s in scores if s < 10]) * 2.5  # small penalty
    adjusted_sum = raw_sum - penalty
    
    # Final nonlinear boost
    if adjusted_sum > 0:
        final_boost = math.tanh(adjusted_sum / 100) * 20
    else:
        final_boost = 0
    
    aggregate = adjusted_sum + final_boost
    
    # Key output variable
    final_score = int(round(aggregate * scale_factor))  # scale_factor == 1 in this case
    
    # Dead code: never executed due to structure
    if False:
        buffer = DataBuffer(10)
        for _ in range(15):
            buffer.add(unused_utility(5))
    
    return final_score

# Generate test input (deterministic)
packets = [
    {
        'header': {'version': 2, 'ts': 1678886400, 'sid': 101},
        'payload': [
            {'value': 50}, {'value': 20}, {'value': 0}, {'value': 150},
            {'value': -5}, {'value': 75}
        ]
    },
    {
        'header': {'version': 2, 'ts': 1678886401, 'sid': 102},
        'payload': [
            {'value': 30}, {'value': 80}, {'value': 10}, {'value': 200}
        ]
    },
    {
        'header': {'version': 2, 'ts': 1678886402, 'sid': 103},
        'payload': [
            {'value': 40}, {'value': 60}, {'value': 5}
        ]
    }
]

# Execute main computation
result = compute_aggregate(packets)
print(f"Result: {result}")