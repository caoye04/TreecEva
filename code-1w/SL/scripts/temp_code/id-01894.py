import math

def analyze_node_health(node_str):
    # Irrelevant parsing logic (distractor)
    if 'ERR' in node_str:
        return 0
    if len(node_str) % 2 == 0:
        return len(node_str) // 2
    return sum([ord(c) - 96 for c in node_str.lower() if c.isalpha()])

def transform_key(signal):
    # Unused function - red herring
    return ''.join(sorted(signal, reverse=True))

def decode_frequency(freq_code):
    # Decoy computation with no impact
    base = 0
    for ch in freq_code:
        if ch.isdigit():
            base += int(ch)
    return base * 1.5

def compute_phase_shift(data):
    # Misleading but unused transformation
    shifted = []
    for i in range(len(data)):
        shifted.append((data[i] + i) % 7)
    return shifted

def filter_active_nodes(nodes):
    active = []
    for node in nodes:
        if node['status'] == 'ACTIVE' and 'diag' in node:
            active.append(node['diag'])
    return active

def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def build_routing_table(entries):
    # Complex-looking but irrelevant data structure manipulation
    table = {}
    for e in entries:
        key = e[:3]
        val = sum(ord(c) for c in e)
        table[key] = val % 100
    return table

def aggregate_metrics(nodes):
    # Core relevant logic starts here
    diagnostics = []    
    for node in nodes:
        if 'type' in node and node['type'] == 'COMPUTE':
            raw = node.get('diagnostic', '')
            # Real processing: count vowels in diagnostic string
            vowel_count = len([c for c in raw.lower() if c in 'aeiou'])
            # Then multiply by length of id (string)
            id_len = len(node['id'])
            score = vowel_count * id_len
            # Only add if score is odd
            if score % 2 == 1:
                diagnostics.append(score)
    
    # Now process with real dependency
    temp_buffer = []
    for d in diagnostics:
        # Apply non-linear transformation
        if d > 10:
            temp_buffer.append(d // 2)
        else:
            temp_buffer.append(d + 3)
    
    # Final aggregation
    total = sum(temp_buffer)
    adjustment = len(diagnostics)  # number of qualifying nodes
    final_score = total - adjustment
    
    # Additional step: if any node had 'priority' flag, double result
    has_priority = any('priority' in n and n['priority'] for n in nodes)
    if has_priority:
        final_score *= 2
    
    return final_score

# Initialization data - realistic scenario: network node telemetry
node_data = [
    {
        'id': 'N001',
        'type': 'COMPUTE',
        'status': 'ACTIVE',
        'diagnostic': 'STATUS_OK',
        'metrics': [23, 45, 67],
        'timestamp': '2023-05-01T10:00:00Z'
    },
    {
        'id': 'N002',
        'type': 'COMPUTE',
        'status': 'ACTIVE',
        'diagnostic': 'ERR_TIMEOUT',
        'diagnostics': 'retry_failed',
        'version': '2.1.0'
    },
    {
        'id': 'MX03',
        'type': 'COMPUTE',
        'status': 'STANDBY',  # not active, but type matches
        'diagnostic': 'READY',
        'priority': True
    },
    {
        'id': 'N004',
        'type': 'COMPUTE',
        'status': 'ACTIVE',
        'diagnostic': 'OK',
        'meta': {'region': 'us-west'}
    },
    {
        'id': 'N005',
        'type': 'NETWORK',  # wrong type
        'status': 'ACTIVE',
        'diagnostic': 'FLOW_NORMAL'
    }
]

# Dead code path - unreachable
unused_result = compute_phase_shift([1, 2, 3, 4])

# Redundant dictionary operation (distractor)
dummy_map = {'A': 1, 'B': 2}
for k in dummy_map:
    dummy_map[k] += len(k)

# Trigger the actual computation chain
active_list = filter_active_nodes(node_data)
sorted_diagnostics = sorted(active_list)
entropy_value = calculate_entropy([len(s) for s in sorted_diagnostics])

# Critical execution point
final_diagnostic = aggregate_metrics(node_data)

# Print result as required
print(f"Target result: {final_diagnostic}")