import itertools

def analyze_node_health(node_data, threshold=0.75):
    # Irrelevant health computation (distractor)
    return sum([v['load'] / v['capacity'] for v in node_data.values()]) / len(node_data)

def compute_fallback_route(nodes):
    # Dead code path — never called
    route = []
    for i in range(len(nodes)):
        if nodes[i]['active']:
            route.append(i)
    return list(itertools.accumulate(route))

def encrypt_signal(data, key=3):
    # Distractor function: string manipulation with no impact on result
    encrypted = ''.join(chr((ord(c) + key) % 97 + 32) for c in data.lower() if c.isalpha())
    return encrypted[::-1]

def decode_frequency_sequence(seq):
    # Unused recursive frequency decoder (red herring)
    if not seq:
        return 0
    return seq[0] + decode_frequency_sequence(seq[1:]) * 0.1

def apply_phase_shift(buffer, shift_by=2):
    # Bit manipulation distractor
    shifted = [(x << shift_by) ^ 0xAA & 0xFF for x in buffer]
    return [b for b in shifted if b > 50]

# Simulated network node diagnostics
network_nodes = {
    'node_01': {'status': 'critical', 'load': 95, 'capacity': 100, 'active': False, 'flags': 0b1010},
    'node_02': {'status': 'warning', 'load': 78, 'capacity': 90, 'active': True, 'flags': 0b0110},
    'node_03': {'status': 'normal', 'load': 45, 'capacity': 80, 'active': True, 'flags': 0b0001},
    'node_04': {'status': 'critical', 'load': 92, 'capacity': 100, 'active': False, 'flags': 0b1100},
    'node_05': {'status': 'normal', 'load': 33, 'capacity': 75, 'active': True, 'flags': 0b0011}
}

# Irrelevant signal trace (distractor data)
signal_trace = [0x1A, 0x2C, 0x0F, 0x3D, 0x22]
processed_buffer = apply_phase_shift(signal_trace, 1)

class DiagnosticLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, msg):
        self.logs.append(msg)

logger = DiagnosticLogger()
logger.log("System diagnostic initiated")

# Decoy dictionary for configuration (misleading intermediate state)
current_config = {
    'threshold': 0.8,
    'debug_mode': True,
    'encryption_enabled': False,
    'retry_limit': 3,
    'timeout_ms': 500
}

# Auxiliary function to calculate node efficiency score (unused)
def calculate_efficiency(n):
    return (n['load'] * 0.6) + (n['capacity'] * 0.4)

# Real logic starts here: extract active nodes
active_node_ids = [k for k, v in network_nodes.items() if v['active']]

# Compute cumulative load on active nodes
cumulative_load = sum(network_nodes[k]['load'] for k in active_node_ids)

# Count how many have warning or critical status (irrelevant count)
issue_count = sum(1 for k in network_nodes if network_nodes[k]['status'] in ['warning', 'critical'])

# Tuple unpacking distraction
primary_node, backup_node = 'node_01', 'node_02'
status_codes = {'critical': 2, 'warning': 1, 'normal': 0}

# Dictionary-based state mapping (partially relevant)
node_risk_levels = {}
for nid, data in network_nodes.items():
    risk_score = status_codes[data['status']] + (1 if data['load'] > 75 else 0)
    node_risk_levels[nid] = risk_score

# Complex nested computation with filtering and transformation
high_risk_active = [
    nid for nid in active_node_ids 
    if node_risk_levels[nid] >= 2 or (node_risk_levels[nid] == 1 and '0' in nid)
]

# Real key computation: XOR of flags from high-risk active nodes
flag_accumulator = 0
for nid in high_risk_active:
    flag_accumulator ^= network_nodes[nid]['flags']

# Additional distraction: string processing on node IDs
node_names_concat = ''.join(sorted(active_node_ids))
encoded_name_fragment = encrypt_signal(node_names_concat, key=2)

# Real dependency: transform using itertools
grouped_indices = [len(list(group)) for _, group in itertools.groupby(node_names_concat, key=str.isdigit)]
adjusted_factor = sum(grouped_indices) * 10

# Final diagnostic depends only on flag_accumulator and adjusted_factor
final_diagnostic = (flag_accumulator * 100) + adjusted_factor

Result: {final_diagnostic}