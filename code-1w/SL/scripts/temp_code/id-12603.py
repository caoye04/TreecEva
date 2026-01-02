import itertools

# System health monitoring with mixed computational paradigms
def analyze_node_stability(readings):
    if not readings:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    stability_score = 100 - (variance * 2.5)
    return max(stability_score, 0)

# Irrelevant helper - distractor function
def encrypt_log(data):
    encrypted = ''.join(chr((ord(c) + 3) % 127) for c in data)
    return encrypted[::-1]

# Decoy transformation - never actually used in final calculation
def transform_coordinates(x, y, z):
    transformed = (x ^ 255, y ^ 255, z ^ 255)
    magnitude = (transformed[0] ** 2 + transformed[1] ** 2 + transformed[2] ** 2) ** 0.5
    return round(magnitude, 3)

# Simulate false dependency chain
def compute_ghost_factor(seq):
    accumulated = 0
    for i in range(len(seq)):
        if i % 3 == 0:
            accumulated += seq[i] * 1.5
        elif i % 3 == 1:
            accumulated -= seq[i] // 4
    return accumulated  # Dead-end value

# Core diagnostic logic
def evaluate_integrity(nodes):
    integrity_list = []
    for node in nodes:
        raw_data = node['telemetry']
        # Extract only even-indexed values for processing
        filtered = [v for i, v in enumerate(raw_data) if i % 2 == 0]
        base_score = sum(filtered)
        # Apply conditional multiplier based on node class
        if node['class'] == 'A':
            base_score *= 1.2
        elif node['class'] == 'B':
            base_score *= 0.85
        else:
            base_score *= 1.0
        integrity_list.append(base_score)
    return integrity_list

# Auxiliary function - looks important but partially irrelevant
def generate_report_keys(entity_id, timestamp):
    key_base = f'{entity_id}_{timestamp}'
    segments = [key_base[i:i+4] for i in range(0, len(key_base), 4)]
    rotated = [s[-1] + s[:-1] for s in segments]
    return '|'.join(rotated)

# Real computation path buried under distractions
def aggregate_metrics(node_map, load_profile):
    # Step 1: Unpack nested structure
    active_nodes = [node_map[k] for k in sorted(node_map.keys()) if node_map[k]['active']]
    
    # Step 2: Evaluate each node's integrity score
    scores = evaluate_integrity(active_nodes)
    
    # Step 3: Apply load-based weighting
    weighted = []
    for i, score in enumerate(scores):
        weight = load_profile[i % len(load_profile)]
        adjusted = score * (weight / 100.0)
        weighted.append(adjusted)
    
    # Step 4: Accumulate and normalize
    total = sum(weighted)
    normalization_factor = len(active_nodes) or 1
    normalized_total = total / normalization_factor
    
    # Step 5: Add bonus for high-stability nodes
    bonus = 0
    for node in active_nodes:
        stability_readings = node['telemetry'][1::3]  # Every third reading starting at index 1
        stability_metric = analyze_node_stability(stability_readings)
        if stability_metric > 90:
            bonus += 15
    
    # Step 6: Final adjustment using modular arithmetic
    final_value = (int(normalized_total) + bonus) % 9731
    
    # Misleading side calculation - distracts from real path
    phantom_chain = list(itertools.accumulate([final_value % 100], lambda a, x: (a * 1.05) % 4000))
    for _ in range(5):
        phantom_chain.append((phantom_chain[-1] * 1.05) % 4000)
    
    # Final result
    return final_value

# --- Data setup ---
network_nodes = {
    'node_001': {
        'class': 'A',
        'active': True,
        'telemetry': [88, 92, 76, 85, 94, 87, 73, 91, 89, 77, 95, 82]
    },
    'node_002': {
        'class': 'B',
        'active': True,
        'telemetry': [75, 80, 78, 83, 77, 85, 79, 81, 84, 80, 76, 82]
    },
    'node_003': {
        'class': 'C',
        'active': False,  # Inactive - should be skipped
        'telemetry': [90, 94, 88, 92, 96, 89, 93, 91, 95, 90, 92, 94]
    },
    'node_004': {
        'class': 'A',
        'active': True,
        'telemetry': [86, 89, 83, 90, 87, 91, 85, 88, 92, 86, 84, 90]
    }
}

system_load = [95, 88, 102, 91, 87]  # Percentages over time window

# --- Execution ---

# Irrelevant initialization block
timestamp = 1718923405
entity_code = "SYS_DIAG_2024"
log_data = f"{entity_code}|{timestamp}|INIT"
encrypted_log = encrypt_log(log_data)
report_key = generate_report_keys(4201, timestamp)

# Another red herring: coordinate transformation
coords = transform_coordinates(127, 255, 64)

# Ghost factor computation - looks related but isn't
sequence_probe = [3, 7, 15, 31, 63]
ghost_result = compute_ghost_factor(sequence_probe)

# Actual target execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Output the result as required
print(f"Target result: {final_diagnostic}")