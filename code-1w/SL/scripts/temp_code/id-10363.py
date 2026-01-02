def analyze_component_health(health_log):
    cumulative_score = 0
    for i, entry in enumerate(health_log):
        if i % 2 == 0:
            cumulative_score += entry * 1.5
        else:
            cumulative_score -= entry * 0.5
    return cumulative_score

system_state = {'status': 'active', 'mode': 'diagnostic', 'version': 2.1}

log_entries = [8, 12, 5, 19, 3, 7]

# Irrelevant preprocessing: simulates noise from unused diagnostics
temp_analysis = []
for idx, val in enumerate(log_entries):
    temp_analysis.append(val ** 2 + idx)  # Unused transformation

snapshot_buffer = [x for x in log_entries if x > 10]
device_power_levels = {f'device_{i}': (i+1)*15 for i in range(5)}  # Dead data structure

# Misleading intermediate calculation with decoy function
def compute_stability_index(data):
    return sum(data) / len(data) * 0.1  # Not actually used later

stability_snapshot = compute_stability_index(log_entries)  # Red herring value

# Simulate checksum that looks important but is unused
current_checksum = 0
for byte in b'diag_pass_42':
    current_checksum ^= byte

def extract_signatures(records):
    signatures = []
    for r in records:
        signatures.append(r ^ 7)  # Bit manipulation distraction
    return signatures  # Never called

# Real processing begins here — deeply nested and interwoven with noise
def evaluate_thresholds(entries, config):
    result_set = []
    base_offset = 10
    
    for index, value in enumerate(entries):
        adjusted = value + base_offset
        
        if config['status'] == 'active':
            if adjusted > 15:
                for shift in [1, 2]:
                    shifted_val = adjusted >> shift
                    if shifted_val % 3 == 0:
                        result_set.append(shifted_val)
                        break  # Early exit red herring
            else:
                result_set.append(adjusted * 2)
    
    # Secondary filter that appears significant
    filtered_results = []
    for item in result_set:
        if item in entries:  # Rare condition, mostly false
            filtered_results.append(item)
        else:
            filtered_results.append(item // 2)  # Dominant path
    
    return sum(filtered_results)

# Another decoy: uses zip but irrelevant
def correlate_streams(stream_a, stream_b):
    pairs = list(zip(stream_a, stream_b))
    correlation = 0
    for a, b in pairs:
        if a < b:
            correlation += 1
    return correlation  # Computed but unused

aux_stream_1 = [1, 2, 3]
aux_stream_2 = [2, 1, 4]
unused_correlation = correlate_streams(aux_stream_1, aux_stream_2)

# Core logic buried among distractions
def process_metrics(logs, state):
    base_sum = 0
    for i, val in enumerate(logs):
        if state['mode'] == 'diagnostic':
            transformed = val * (i + 1)
            if transformed % 2 == 0:
                base_sum += transformed // 2
            else:
                base_sum += transformed + 5
    
    # Key branching logic
    if 'version' in state and state['version'] > 2.0:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 1.0
    
    intermediate = evaluate_thresholds(logs, state)
    final_value = base_sum * adjustment_factor - intermediate
    
    # Decoy dictionary mutation
    shadow_copy = state.copy()
    shadow_copy['diagnostic_flag'] = True
    shadow_copy['score'] = final_value  # Looks important, never used
    
    return int(final_value)

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)

# Output required format
print(f"Result: {final_diagnostic}")