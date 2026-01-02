import math

# Simulated system telemetry data with diagnostic flags
def collect_telemetry():
    raw_signals = [0.88, 0.76, 0.91, 0.83, 0.79]
    noise_floor = 0.12
    filtered = [x - noise_floor for x in raw_signals if x > 0.75]
    return {"readings": filtered, "version": "v2.1", "calibrated": True}

# Auxiliary function - appears important but used only once
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# Decoy function: looks relevant but never called
def compute_health_score(readings):
    total = 0
    for r in readings:
        total += math.pow(r, 2.5)
    return int(total * 10) // len(readings)

# Another decoy: complex logic but unused
def analyze_pattern(seq):
    if len(seq) < 3:
        return False
    trend = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
    oscillation = sum(1 for i in range(1, len(seq)) if abs(seq[i]-seq[i-1])>0.05)
    return {'trend': trend, 'jitter': oscillation}

# Critical processing pipeline
def process_metrics(data, state):
    # Irrelevant transformation (dead-end)
    temp_log = []
    for k, v in state.items():
        if isinstance(v, bool):
            temp_log.append(f"{k}_ok" if v else f"{k}_fail")
    
    # Real computation begins
    values = data["readings"]
    base_score = sum(math.sin(x * math.pi) for x in values)
    
    # Distractor: complex-looking normalization
    adjusted = [normalize(v, 0.5, 1.0) for v in values]
    dummy_weight = sum(adjusted) / len(adjusted)
    
    # Actual key calculation
    if state.get("active", False) and state.get("calibrated"):
        multiplier = 3
        if len(values) >= 4:
            # Secondary condition modifies multiplier
            avg = sum(values) / len(values)
            if avg > 0.8:
                multiplier += 1
            # Nested conditional with slicing distraction
            recent = values[-3:]
            if all(r > 0.78 for r in recent):
                multiplier += 2
        else:
            multiplier = 1
        
        # Core formula: answer depends on this
        base_score *= multiplier
    else:
        base_score = 0
    
    # Red herring: dictionary mutation not affecting output
    diagnostics = {"raw_count": len(values), "base": base_score, "temp": dummy_weight}
    diagnostics["flags"] = temp_log
    diagnostics["status"] = "nominal"
    
    # Final result derived from controlled path
    final_value = int(base_score * 1000) + 117
    
    # Unused branching - misleading control flow
    if diagnostics["raw_count"] == 0:
        final_value = -999
    elif diagnostics.get("temp") > 0.5:
        final_value += 50  # This would mislead if dummy_weight were higher

    return final_value

# Simulate system state with plausible structure
system_state = {
    "active": True,
    "calibrated": True,
    "mode": "diagnostic",
    "timestamp": 1718934567,
    "debug": False,
    "redundancy_check": [True, True, False],
    "version_hash": "abc123"
}

# Data snapshot with meaningful content
snapshot = collect_telemetry()

# Add irrelevant list comprehension
buffer_dump = [chr(int(65 + i)) for i in range(10) if i % 3 == 0]

# Unused bitwise operation - looks cryptic but irrelevant
checksum = 0
for item in buffer_dump:
    checksum ^= ord(item)
    checksum &= 0xFF
    checksum = (checksum << 1) | (checksum >> 7)

# Key assignment statement
final_diagnostic = process_metrics(snapshot, system_state)

# Output result as required
print(f"Result: {final_diagnostic}")