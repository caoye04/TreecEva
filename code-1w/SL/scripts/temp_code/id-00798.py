import itertools

# System diagnostics simulation with red herrings and complex data flow
def analyze_node_sequence(node_ids):
    # Irrelevant transformation: generates unused node hashes
    hashed = [hash(n * 17 + 256) % 1000 for n in node_ids]
    filtered = [n for n in node_ids if n % 3 == 0]
    return sum(filtered) * len(hashed)

def validate_chain_consistency(chain):
    # Decoy function - looks important but unused in critical path
    if not chain:
        return False
    diffs = [chain[i+1] - chain[i] for i in range(len(chain)-1)]
    return all(d > 0 for d in diffs)

def generate_audit_trail(records):
    # Distractor: builds a complex structure not used in final result
    timestamps = [r[1] for r in records]
    anomalies = [(i, t) for i, t in enumerate(timestamps) if t % 7 == 0]
    summary = {'count': len(records), 'anomalies': len(anomalies)}
    return summary

def extract_signatures(payload):
    # Dead-end computation with bit manipulation red herring
    sigs = []
    for p in payload:
        transformed = (p << 2) ^ 0xFF
        normalized = (transformed & 0xFFFF) >> 1
        sigs.append(normalized)
    return sigs

def compute_integrity_score(log_entries):
    # Core logic buried in noise
    base_values = [entry[0] for entry in log_entries]
    
    # Red herring: complex tuple unpacking with irrelevant fields
    extended_info = [entry[2:] for entry in log_entries if len(entry) > 2]
    temp_flags = list(itertools.chain.from_iterable(extended_info))
    
    # Misleading intermediate: looks like scoring but isn't final
    pseudo_score = sum(b ** 2 for b in base_values if b < 50) - len(temp_flags)
    
    # Actual relevant computation (well-hidden)
    valid_entries = [b for b in base_values if b % 4 == 2]
    adjustment_factor = len([v for v in valid_entries if v > 10])
    
    # Key calculation
    raw_total = sum(valid_entries)
    final_score = raw_total - adjustment_factor * 3
    
    # Multiple distractor operations
    decoy_shift = (raw_total << 3) & 0xFF
    dummy_check = any(decoy_shift == v for v in valid_entries)
    
    return final_score

# Simulated system state log (mixed data)
network_state_log = [
    (12, 1500, 'A', 'X'),
    (18, 1505, 'B'),
    (22, 1510, 'C', 'Y', 'Z'),
    (26, 1515, 'D'),
    (34, 1520, 'E', 'W'),
    (42, 1525, 'F'),
    (58, 1530, 'G', 'V')
]

# Unused variables - red herrings
current_epoch = 1527
system_capacity = 9876
temporal_weights = tuple(i * 0.5 for i in range(8))
node_hierarchy = {i: chr(65+i) for i in range(7)}

# Complex initialization with distraction
audit_results = generate_audit_trail(network_state_log)
node_analysis = analyze_node_sequence([entry[0] for entry in network_state_log])
signatures = extract_signatures([entry[1] for entry in network_state_log])

# Critical execution point buried in noise
intermediate_cycle = list(itertools.product([2], range(3)))
baseline_reference = node_analysis // 100

# Key statement
final_diagnostic = compute_integrity_score(network_state_log)

# Print required output
print(f"Result: {final_diagnostic}")