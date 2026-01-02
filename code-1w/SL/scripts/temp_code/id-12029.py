def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    return [abs(val) ** 0.5 * (1 + i) for i, val in enumerate(filtered)]


def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) & i
    return checksum

# Irrelevant helper: simulates network latency probing (unused later)
def probe_latency(nodes):
    delays = []
    for node in nodes:
        delay = sum(ord(c) for c in node) % 7
        delays.append(delay if delay != 3 else 0)
    return delays

# Decoy function: looks important but unused
def compute_entropy(data):
    from math import log
    freqs = {}
    for item in data:
        freqs[item] = freqs.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Real processing chain
log_data = [1.2, -2.4, 3.6, -0.3, 4.8, 1.1, -5.0, 0.9]

scaling_factors = [1.1, 0.9, 1.05, 0.95, 1.2]
decay_weights = [0.1 * (i+1) for i in range(5)]

threshold_map = {
    'low': 1.0,
    'medium': 2.0,
    'high': 3.5
}

auxiliary_indices = []
for key, thresh in threshold_map.items():
    idx = sum(1 for x in log_data if x > thresh)
    auxiliary_indices.append(idx)

# Simulated sensor flags (distractor)
sensor_flags = {f's{i}': (i % 3 == 0) for i in range(1, 6)}

# Unused transformation path
temp_log = []
for x in log_data:
    if x > 0:
        temp_log.append(x * scaling_factors[0])
    else:
        temp_log.append(x / scaling_factors[1])

# Actual relevant processing begins here
def process_entry(val, index, config):
    base = abs(val) * (index + 1)
    if val < 0:
        base = base ** 0.5
    level = 'low'
    if base > config['high']:
        level = 'high'
    elif base > config['medium']:
        level = 'medium'
    
    # Dummy bit manipulation (looks complex but partially irrelevant)
    magic = int(base) ^ 255
    magic = (magic << 2) & 1023
    
    return {'value': base, 'level': level, 'flag': magic}

def process_metrics(data, thresholds):
    results = []
    for i, entry in enumerate(data):
        outcome = process_entry(entry, i, thresholds)
        results.append(outcome)
    
    # Key aggregation
    high_count = sum(1 for r in results if r['level'] == 'high')
    medium_count = sum(1 for r in results if r['level'] == 'medium')
    score = high_count * 100 + medium_count * 10
    
    # Secondary metric: sum of transformed values above threshold
    transformed = [r['value'] for r in results if r['value'] > thresholds['medium']]
    bonus = sum(transformed) // 1 if transformed else 0
    
    # Distractor: zip with unrelated list
    weights = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    weighted_vals = []
    for val, wt in zip([r['value'] for r in results], weights):
        weighted_vals.append(val * wt)
    
    # Final computation (depends only on score and bonus)
    final_score = score + int(bonus % 89)
    
    # Dead code branch (never executed due to logic)
    if False and final_score > 1000:
        final_score -= 255
    
    # Critical red herring: checksum that looks important
    fake_hash = generate_checksum(weighted_vals)
    
    # Actual answer derivation
    adjustment = 0
    for k, v in thresholds.items():
        adjustment += int(v)
    
    final_diagnostic = final_score - adjustment + auxiliary_indices[0]
    
    # This print is required
    return final_diagnostic

# Execution flow
interim = analyze_signal(log_data)

# Unused enumeration example (distractor)
indexed_weights = []
for idx, w in enumerate(zip(scaling_factors, decay_weights)):
    sf, dw = w
    indexed_weights.append((idx, sf * (1 - dw)))

# Main call
final_diagnostic = process_metrics(log_data, threshold_map)
print(f"Target result: {final_diagnostic}")