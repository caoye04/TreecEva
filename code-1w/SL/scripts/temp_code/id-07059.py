def analyze_component_health(health_flags, threshold_map):
    cumulative_score = 0
    for flag, weight in threshold_map.items():
        if flag in health_flags and health_flags[flag]:
            cumulative_score += weight * 3
        else:
            cumulative_score -= weight
    return cumulative_score

# Irrelevant diagnostic function (decoy)
def legacy_diagnostic_check(data):
    if len(data) > 5:
        temp_sum = 0
        for x in data:
            temp_sum += x ** 2
        return temp_sum % 7
    return 0

# Unused utility (dead code path)
def compress_telemetry(stream):
    result = 0
    for i, val in enumerate(stream):
        result ^= (val + i) & 0xFF
    return result

# Main processing function with distractors
def process_metrics(entries, state_config):
    raw_counts = {"critical": 0, "warning": 0, "info": 0}
    temporal_weights = []
    
    # Real computation begins
    for entry in entries:
        log_level = entry.get("level", "info")
        timestamp = entry.get("ts", 0)
        if timestamp < 1000:  # Filter condition
            continue
        raw_counts[log_level] += 1
        if log_level == "critical":
            temporal_weights.append(timestamp % 11)
    
    # Distractor: irrelevant transformation
    inverted_weights = [10 - w for w in temporal_weights if w < 8]
    ignored_result = sum(inverted_weights) * 0.5
    
    # Real logic: compute base metric
    base_metric = raw_counts["critical"] * 13 + raw_counts["warning"] * 5
    
    # Conditional red herring
    if len(temporal_weights) > 3:
        adjustment = 0
        for t in temporal_weights:
            adjustment += t ^ 7
        base_metric -= adjustment // 4  # Misleading modification
    
    # Key branching logic with dictionary lookup
    mode_map = {"active": 7, "standby": 3, "maintenance": -5}
    mode_bonus = mode_map.get(state_config.get("mode"), 0)
    
    # Bitwise interference (partially relevant)
    flags = state_config.get("flags", 0)
    if flags & 0x8:  # Check bit 4
        mode_bonus += (flags & 0x3) << 2
    
    # Decoy dictionary update
    state_config['temp_calculated'] = (base_metric ^ mode_bonus) % 100
    
    # Real final calculation
    diagnostic_value = base_metric + mode_bonus
    if diagnostic_value > 0 and raw_counts["info"] % 2 == 0:
        diagnostic_value = (diagnostic_value * 3) // 2
    
    # Secondary red herring: unused loop over system components
    system_components = ["sensor", "actuator", "controller", "bus"]
    component_offset = 0
    for comp in system_components:
        hash_val = 0
        for c in comp:
            hash_val += ord(c) % 5
        component_offset += hash_val & diagnostic_value
    
    # Final assignment (target)
    final_diagnostic = diagnostic_value + len(entries) % 9
    return final_diagnostic

# Setup test data
log_entries = [
    {"level": "critical", "ts": 1024},
    {"level": "warning", "ts": 1100},
    {"level": "critical", "ts": 1050},
    {"level": "info", "ts": 999},      # filtered out by timestamp
    {"level": "warning", "ts": 1200},
    {"level": "critical", "ts": 1300}
]

system_state = {
    "mode": "active",
    "flags": 0xB,  # binary 1011 -> includes bit 4 (0x8), bits 0-1 are 11
    "version": "2.1.0",
    "debug": True
}

# Call the main function
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Result: {final_diagnostic}")