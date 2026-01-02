from collections import defaultdict, Counter

# Simulated system telemetry data
def collect_telemetry(nodes):
    metrics = defaultdict(float)
    for node in nodes:
        if node % 3 == 0:
            metrics['power_draw'] += (node * 1.5) % 7
        elif node % 5 == 0:
            metrics['temp_spike'] += (node // 2) ** 0.5
        metrics['heartbeat'] += 1  # Always increment
    return metrics

def evaluate_stability(telemetry, threshold=4.8):
    score = 0
    score += int(telemetry['heartbeat'] * 0.7)
    score -= int(telemetry['temp_spike'])
    # Distractor: irrelevant calculation
    hypothetical_loss = sum([i**2 for i in range(5)]) * 0.1
    adjusted_score = score - hypothetical_loss  # Not used
    return score > threshold

# Auxiliary function with dead logic path
def analyze_node_distribution(node_ids):
    counts = Counter(node_ids)
    distribution_pattern = []
    for k, v in counts.items():
        if v > 1:
            distribution_pattern.append(k * 2)
        else:
            # Dead code branch — never executed due to input structure
            if k > 1000:
                distribution_pattern.append(k // 4)
    # Irrelevant transformation
    encrypted_trace = [((x << 2) ^ 5) & 15 for x in distribution_pattern]
    return len(distribution_pattern)

# Core diagnostic workflow
def compute_resource_efficiency(resources):
    efficiency_map = {}
    total_utilized = 0
    peak_load = 0
    for r_id, usage in resources.items():
        normalized = (usage % 31) / 8.0
        if normalized > 3:
            peak_load += 1
        efficiency_map[r_id] = round(normalized, 3)
        total_utilized += int(normalized)
    # Distractor variable
    avg_fragmentation = len(efficiency_map) / (total_utilized + 1) if total_utilized else 0
    return total_utilized, peak_load

# Main health assessment with mixed logic
def system_health_check(resources, nodes):
    # Step 1: Gather resource stats
    util, peaks = compute_resource_efficiency(resources)
    
    # Step 2: Collect node telemetry
    tel = collect_telemetry(nodes)
    
    # Step 3: Evaluate stability from telemetry
    stable = evaluate_stability(tel)
    
    # Step 4: Analyze node uniqueness (distractor call)
    pattern_size = analyze_node_distribution(nodes)
    
    # Step 5: Compute derived diagnostics
    base_rating = util * 10 + peaks * 5
    if stable:
        base_rating += 12
    
    # Step 6: Apply conditional offset based on pattern (unused)
    if pattern_size > 2:
        offset_correction = -7  # Computed but not used
    
    # Step 7: Incorporate bit manipulation for checksum
    checksum = 0
    for val in resources.values():
        checksum ^= (val & 7) << 1
    
    # Step 8: Final integration
    intermediate = base_rating + (checksum & 15)
    
    # Step 9: Apply logarithmic adjustment (guarded)
    import math
    if intermediate > 0:
        adjusted = int(intermediate + math.log(intermediate))
    else:
        adjusted = intermediate
    
    # Step 10: Final threshold gate
    if adjusted >= 45:
        final_diagnostic = adjusted + 5
    else:
        final_diagnostic = adjusted - 3
    
    return final_diagnostic

# Setup test environment
resource_pool = {f'r_{i}': (i * 17) % 43 for i in range(1, 8)}
active_nodes = [15, 18, 20, 21, 24, 25, 27]

# Trigger point: final_diagnostic assignment
final_diagnostic = system_health_check(resource_pool, active_nodes)
print(f"Result: {final_diagnostic}")