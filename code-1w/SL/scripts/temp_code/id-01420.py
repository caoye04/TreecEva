from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def calculate_network_latency(nodes):
    return sum([len(n) for n in nodes]) * 0.05

# Misleading performance metric (distractor)
class PerformanceTracker:
    def __init__(self):
        self.metrics = defaultdict(float)
        self.audit_log = []

    def update(self, k, v):
        self.metrics[k] += v
        self.audit_log.append(f'Updated {k}: {v}')

    def get_summary(self):
        return dict(self.metrics)

# Core logic disguised among distractions
def analyze_signal_strength(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    if not filtered:
        return 0.0
    avg = sum(filtered) / len(filtered)
    variance = sum([(x - avg) ** 2 for x in filtered]) / len(filtered)
    return round(math.sqrt(variance), 4)

# Unused but plausible function (red herring)
def decode_transmission(signal):
    try:
        return ''.join([chr(int(s)) for s in signal if s.isdigit()])
    except:
        return "ERROR"

# Key recursive transformation function
def transform_sequence(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return [s * 2 for s in seq]
    processed = []
    for item in seq:
        if item % 3 == 0:
            processed.append(item // 3)
        elif item % 2 == 0:
            processed.extend(transform_sequence([item - 1], depth + 1))
        else:
            processed.append(item + 1)
    return transform_sequence(processed, depth + 1)

# Main evaluation logic with embedded distractors
def evaluate_performance(data):
    temp_results = []
    aux_counter = Counter()
    
    # Distractor loop - accumulates but isn't used in final result
    for entry in data:
        if 'aux' in entry:
            aux_counter[entry['type']] += 1
    
    # Real processing chain
    base_values = [d['value'] for d in data if d['active']]
    shifted = [x - 5 for x in base_values]
    
    # Apply recursive transformation
    transformed = transform_sequence(shifted)
    
    # Signal analysis on derived values (misleading relevance)
    _ = analyze_signal_strength(transformed)  # Result ignored
    
    # Critical calculation hidden among noise
    magnitude = sum(abs(t) for t in transformed)
    penalty = len([t for t in transformed if t < 0]) * 3
    raw_score = magnitude - penalty
    
    # Normalize using bitwise manipulation (obscure but valid)
    normalized = (raw_score & 0xFFFF) ^ 0xAAAA
    if normalized > 32767:
        normalized -= 65536
    
    # Final adjustment based on conditional expression
    final_score = normalized if raw_score != 0 else -999
    
    # Dead assignment (distractor)
    final_score = final_score + 0  # No-op
    
    return final_score

# Simulated input data with meaningful structure
metric_data = [
    {'value': 17, 'active': True, 'type': 'primary', 'aux': False},
    {'value': 22, 'active': True, 'type': 'primary', 'aux': True},
    {'value': 8,  'active': True, 'type': 'backup',  'aux': False},
    {'value': 0,  'active': False,'type': 'test',    'aux': True},  # Inactive
    {'value': 14, 'active': True, 'type': 'primary', 'aux': False}
]

# Execution point of interest
final_score = evaluate_performance(metric_data)
print(f'Result: {final_score}')