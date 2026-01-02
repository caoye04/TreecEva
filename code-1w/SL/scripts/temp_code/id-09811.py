def analyze_log_sequence(entries):
    frequency_map = {}
    for entry in entries:
        tag = entry.split('_')[0]
        frequency_map[tag] = frequency_map.get(tag, 0) + 1
    
    # Distractor: Unused transformation
    transformed = list(map(lambda x: x.upper(), entries))
    
    return frequency_map


def compute_health_score(data, threshold=5):
    score = 0
    anomalies = 0
    
    for key, count in data.items():
        if count > threshold:
            anomalies += 1
            score -= count * 1.5
        else:
            score += len(key)
    
    # Distractor: Irrelevant intermediate calculation
    adjustment_factor = sum([len(k) for k in data.keys()]) % 7 if data else 0
    score += adjustment_factor * 0.3
    
    return int(score)


def generate_checksum_registry(keys):
    checksums = {}
    for key in keys:
        chk = 0
        for char in key:
            chk ^= ord(char)  # XOR-based checksum
        checksums[key] = chk % 100
    return checksums

# Simulate system log parsing
raw_logs = [
    'ERR_network_timeout',
    'INFO_cache_hit',
    'WARN_disk_usage_high',
    'ERR_network_timeout',
    'INFO_cache_miss',
    'WARN_disk_usage_high',
    'WARN_cpu_spike',
    'INFO_cache_hit',
    'ERR_network_timeout',
    'WARN_cpu_spike'
]

# Step 1: Extract frequency counts
freq_analysis = analyze_log_sequence(raw_logs)

# Distractor: Secondary unused analysis path
sorted_tags = sorted(freq_analysis.keys(), key=lambda x: freq_analysis[x], reverse=True)

# Step 2: Compute health metric (partially relevant)
health_diagnostic = compute_health_score(freq_analysis, threshold=3)

# Step 3: Build checksum map from unique tags
checksum_registry = generate_checksum_registry(freq_analysis.keys())

# Step 4: Simulate integrity verification with mixed logic
running_hash = 0
for log in raw_logs:
    tag = log.split('_')[0]
    if tag in checksum_registry:
        running_hash += checksum_registry[tag]

# Final diagnostic computation using combined state
intermediate_state = (health_diagnostic + running_hash) % 1000

# Key function combining multiple concepts
verify_system_integrity = lambda logs, chksums: sum(
    chksums[log.split('_')[0]] for log in logs if log.startswith('ERR')
) + (intermediate_state // 10)

# Execute final statement
final_diagnostic = verify_system_integrity(raw_logs, checksum_registry)

print(f"Result: {final_diagnostic}")