from collections import defaultdict, Counter

# Simulated sensor data aggregation for a distributed system health monitor
def collect_telemetry(nodes):
    raw_readings = []
    for node in nodes:
        base = hash(node) % 100
        readings = [base + i * 3 for i in range(5)]
        raw_readings.extend(readings)
    return raw_readings

# Irrelevant auxiliary function: processes network latency (not used in final result)
def analyze_latency(peers):
    stats = defaultdict(float)
    for p in peers:
        val = (hash(p) // 100) % 50
        stats[p] = round(val * 0.75, 2)
    return dict(stats)

# Core transformation: derive health signature from entropy and parity patterns
def generate_signature(data_stream):
    window_size = 4
    entropy_pool = []
    
    for i in range(0, len(data_stream) - window_size + 1, 2):
        window = data_stream[i:i+window_size]
        even_count = sum(1 for x in window if x % 2 == 0)
        window_entropy = even_count ^ len(window)  # XOR-based entropy proxy
        entropy_pool.append(window_entropy)
    
    # Slicing to take only stable phase readings
    valid_entropy = entropy_pool[1:-1] if len(entropy_pool) > 3 else entropy_pool
    
    # Compute signature using bit manipulation and modular arithmetic
    signature = 0
    for idx, ent in enumerate(valid_entropy):
        rotated = ((ent << 3) & 0xFF) | (ent >> 5)  # 8-bit rotate left by 3
        signature ^= rotated
        signature = (signature + idx) % 256
    
    return signature

# Secondary metric calculation with decoy logic paths
def evaluate_stress(load_profile):
    stress_flags = 0
    threshold = 65
    hysteresis = defaultdict(int)
    
    for idx, load in enumerate(load_profile):
        # Real path: count high-load instances
        if load > threshold:
            stress_flags += 1
            hysteresis['over'] += 1
        elif load < 30:
            hysteresis['under'] += 1  # Red herring: not used later
        
        # Dead code path: never reached due to logic above
        if load == 50:
            temp_buffer = [load * 2 for _ in range(5)]  # Unused list
            stress_flags -= 1  # Never executed
    
    # Decoy transformation
    dummy_metric = stress_flags * 1.5
    adjusted = stress_flags ** 2 % 100
    
    return adjusted  # Only this matters

# Main processing pipeline with multiple abstraction layers
def process_metrics(sig, load):
    # Complex conditional expression with boolean logic
    level_1 = (sig > 100) or (sig < 50 and (load > 80 or load < 20))
    level_2 = (sig > 150) and (load > 90)
    level_3 = not (sig % 7 == 0) and (load % 11 == 0)
    
    # Multi-concept integration: bitwise, comparison, arithmetic
    risk_score = (sig << 1) ^ load
    risk_score = (risk_score + (risk_score & 0x0F)) % 1000
    
    # Conditional override chain with red herring
    if level_3:
        risk_score = 404  # Misleading error code
    elif level_2:
        risk_score = 999
    elif level_1:
        risk_score += 100
    else:
        risk_score += 50
    
    # Final adjustment using string method distraction
    tag = f"health_{sig}_{load}"
    extra_weight = len(tag.split('_'))  # Always 3, but looks dynamic
    final_risk = risk_score + extra_weight * 2
    
    # Critical execution point
    final_diagnostic = final_risk * 3  # Key assignment
    
    # Post-processing dead code (distractor)
    debug_log = Counter({'processed': 1, 'errors': 0})
    if final_diagnostic < 0:
        debug_log['errors'] += 1  # Never triggered
    
    return final_diagnostic

# Orchestration script with irrelevant operations
if __name__ == "__main__":
    node_cluster = [f"node-{i}{chr(65+i%26)}" for i in range(8)]
    peer_list = [f"peer-{j}" for j in range(5)]
    
    # Collect real data stream
    telemetry_data = collect_telemetry(node_cluster)
    
    # Generate core diagnostic components
    health_signature = generate_signature(telemetry_data)
    system_load = evaluate_stress(telemetry_data)
    
    # Perform latency analysis (completely unused)
    _ = analyze_latency(peer_list)
    
    # Execute key statement
    final_diagnostic = process_metrics(health_signature, system_load)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")