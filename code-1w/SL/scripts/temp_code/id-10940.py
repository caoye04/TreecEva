import math

# Irrelevant helper function (dead code path)
def unused_network_simulator(nodes):
    return sum([len(node) for node in nodes])

# Misleading preprocessing with decoy transformations
def preprocess_metrics(raw):
    temp_result = {}
    for k, v in raw.items():
        if 'temp' in k:
            temp_result[k] = v * 1.8 + 32
        elif 'count' in k:
            temp_result[k] = v + 10  # Red herring adjustment
    return temp_result  # Never used

# Distractor: Complex but unused data structure transformation
class MetricBuffer:
    def __init__(self):
        self.buffer = []
        self.index_map = {}
    
    def add(self, val):
        self.buffer.append(val)
        self.index_map[len(self.buffer)-1] = val ** 2

# Unused recursive checksum (decoy logic)
def recursive_checksum(data, index=0):
    if index >= len(data):
        return 0
    return (data[index] % 7) + recursive_checksum(data, index + 1)

# Real logic begins here — subtle and buried among noise
def analyze_streak(values):
    max_streak = 0
    current = 0
    for v in values:
        if v > 0:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 0
    return max_streak

# Bit manipulation red herring
def bit_scramble(n):
    n = ((n << 3) & 0xFF) | (n >> 5)
    n ^= 0b10101010
    return n % 100  # Used nowhere

# Core evaluation logic — non-obvious due to surrounding noise
def compute_efficiency(x, y):
    if y == 0:
        return 0
    return round((x * 100) / (y + x), 3)

# Main scoring logic disguised as one among many functions
def evaluate_performance(metrics):
    # Extract relevant data from dictionary
    attempts = metrics.get('task_attempts', 0)
    successes = metrics.get('success_count', 0)
    latency_data = metrics.get('latency_samples', [])
    
    # Real computation chain starts here
    base_score = compute_efficiency(successes, attempts - successes) if attempts > successes else 0
    
    # Use dictionary operations meaningfully
    stats_summary = {
        'peak': max(latency_data) if latency_data else 0,
        'trough': min(latency_data) if latency_data else 0,
        'range': 0
    }
    stats_summary['range'] = stats_summary['peak'] - stats_summary['trough']
    
    # Normalize range via modular arithmetic
    normalized_spread = stats_summary['range'] % 97  # Prime modulus for illusion of complexity
    
    # Real dependency: streak analysis on derived signal
    signal = [1 if x < 50 else -1 for x in latency_data]  # Threshold-based signal
    longest_positive_streak = analyze_streak(signal)
    
    # Final composite score calculation (only this matters)
    final_component = base_score * 10
    adjustment = longest_positive_streak * 7
    bonus = 25 if normalized_spread > 50 else 10
    
    # Critical answer-determining line
    final_score = int(final_component + adjustment + bonus)
    
    return final_score

# --- Setup and Execution ---

# Large dictionary with mixed relevant/irrelevant keys
metric_data = {
    'task_attempts': 45,
    'success_count': 30,
    'temp_readings': [22.1, 23.5, 21.8],
    'latency_samples': [65, 44, 48, 39, 52, 41, 43, 47, 38, 61],
    'debug_mode': True,
    'version': '2.1.0',
    'checksum': 5643,
    'user_id': 'usr-8893',
    'metadata_flag': 0b1101
}

# Call irrelevant preprocessing (distractor)
preprocessed = preprocess_metrics(metric_data)

# Instantiate unused class (red herring)
buffer = MetricBuffer()
for val in metric_data['latency_samples']:
    buffer.add(val)

# Compute recursive checksum on unrelated data (misleading)
ids = [ord(c) for c in metric_data['user_id'] if c.isdigit()]
fake_check = recursive_checksum(ids)

# Real execution point
final_score = evaluate_performance(metric_data)

# Output result as required
print(f"Target result: {final_score}")