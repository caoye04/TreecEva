from collections import defaultdict
from itertools import combinations

# System health monitoring simulation with diagnostic interference

def simulate_sensor_noise(baseline, factor):
    return [x * factor + 1.7 for x in baseline]

# Irrelevant helper function (dead code path)
def legacy_checksum(data):
    return sum(data) % 256

# Misleading intermediate computation
temp_offset = 4.5
sample_window = [0.8, 1.2, 0.9, 1.3, 1.1]
adjusted_samples = [x + temp_offset for x in sample_window]  # Red herring

# Core system metrics
base_metrics = [3, 7, 2, 8, 5]

# Distractor: unused transformation
transformed = list(map(lambda x: x ** 2 - x, base_metrics))

# Real signal processing
def generate_signature(metrics):
    sig = 0
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            sig += val * 3
        else:
            sig -= val * 2
    return sig

health_signature = generate_signature(base_metrics)  # = (3*3) + (2*3) + (5*3) - (7*2) - (8*2) = 9+6+15-14-16 = 0

# Complex system load calculation with decoy logic
system_load = defaultdict(int)
for i in range(5):
    system_load[f'node_{i}'] = (i + 1) * 10
    if i % 2:
        system_load[f'node_{i}'] += 5

# Decoy aggregation
unused_aggregate = sum(v for k, v in system_load.items() if 'node_' in k and int(k[5:]) < 3)

# Real load metric extraction
active_nodes = [v for k, v in system_load.items() if int(k.split('_')[1]) in [1, 3]]  # nodes 1 and 3: values 15, 35
raw_load_score = sum(active_nodes) // 10  # (15 + 35) // 10 = 5

# Diagnostic engine with red herrings
status_flags = [True, False, True]
current_mode = "STANDBY" if any(status_flags) else "IDLE"  # STANDBY (misleading context)

# Actual analysis function
def analyze_metrics(signature, load):
    # Nested conditional logic with distractions
    diagnostics = []
    
    for i in range(2):
        for j in range(2):
            diagnostics.append((signature + i) * (load + j) - 7)
    
    # Filter out impossible conditions (simulated)
    valid_diagnostics = [d for d in diagnostics if d > -100]
    
    # Use itertools to create diversions
    pairs = list(combinations(valid_diagnostics, 2))
    pair_sum = sum(abs(a - b) for a, b in pairs) if len(pairs) > 1 else 0
    
    # Critical distraction: irrelevant string processing
    log_entry = "ERR_404"
    error_level = len(log_entry) * 2 if "ERR" in log_entry else 0  # 14, never used
    
    # Final computation chain
    intermediate = valid_diagnostics[0]  # First element: (0+0)*(5+0)-7 = -7
    correction = len(pairs)  # number of pairs from 4 elements = 6
    final_value = intermediate + correction * 3  # -7 + 6*3 = 11
    
    # Dead code branch
    if final_value < 0:
        fallback = 999
        return fallback
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_metrics(health_signature, raw_load_score)
print(f"Result: {final_diagnostic}")