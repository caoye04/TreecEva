from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'cpu:90|mem:45|disk:80|net:200',
    'cpu:85|mem:50|disk:75|net:180',
    'cpu:95|mem:40|disk:85|net:220',
    'cpu:88|mem:55|disk:70|net:190'
]

# Irrelevant decoy mapping (distractor)
device_codes = {'A1': 'CPU', 'B2': 'GPU', 'C3': 'TPU', 'D4': 'NPU'}
legacy_mapping = {k: v + '_LEGACY' for k, v in device_codes.items()}

# Parsing function with red herring logic
def parse_telemetry(stream):
    parsed = []
    stats_summary = defaultdict(int)  # Unused aggregation
    for entry in stream:
        components = entry.split('|')
        readings = {}
        for comp in components:
            key, val = comp.split(':')
            readings[key] = int(val)
            stats_summary[key] += int(val)  # Distractor: collected but unused
        parsed.append(readings)
    
    # Dead code path - never invoked (misleading)
    def validate_checksum(data):
        return sum(data.values()) % 17
    
    return parsed

# Auxiliary function that appears important but is partially irrelevant
def calculate_health_index(metrics_list):
    indices = []
    for m in metrics_list:
        cpu_wt = m['cpu'] * 0.6
        mem_wt = m['mem'] * 0.3
        disk_wt = m['disk'] * 0.1
        raw_health = cpu_wt + mem_wt + disk_wt
        adjusted = max(10, min(100, raw_health))  # Clamped result
        indices.append(adjusted)
    
    # Decoy transformation (not used in final result)
    inverse_map = {i: round(100 / i, 2) for i in indices if i != 0}
    
    return indices

# Core processing with embedded distractions
def analyze_patterns(entries):
    pattern_log = []
    for e in entries:
        # Bit manipulation red herring
        encoded_flag = (e['cpu'] << 2) ^ (e['mem'] | 0x0F)
        if encoded_flag > 300:
            pattern_log.append('HIGH_LOAD')
        elif e['disk'] > 75 and e['net'] > 200:
            pattern_log.append('IO_BOTTLENECK')
        else:
            pattern_log.append('NORMAL')
    
    # String-based distraction
    status_text = ''.join([p[0] for p in pattern_log]).lower()
    rotation_key = len(status_text) * 7  # Unused cryptographic-like var
    
    return pattern_log

# Critical function containing the actual answer derivation
def process_metrics(logs, state):
    # Step 1: Extract last entry (most recent)
    latest = logs[-1]
    
    # Step 2: Compute composite stress score
    stress_score = (
        (latest['cpu'] / 100.0) * 0.5 +
        (latest['mem'] / 100.0) * 0.3 +
        (latest['disk'] / 100.0) * 0.2
    ) * 1000
    
    # Step 3: Apply state-based modifier
    modifiers = {'ACTIVE': 1.1, 'STANDBY': 0.9, 'MAINTENANCE': 0.7}
    mod_val = modifiers.get(state, 1.0)
    
    intermediate = stress_score * mod_val
    
    # Step 4: Use Counter to count pattern frequencies (actual relevance)
    freq = Counter(analyze_patterns(logs))
    critical_count = freq['HIGH_LOAD']
    
    # Step 5: Adjust based on frequency of high load
    adjustment_factor = 1 + (critical_count * 0.05)
    
    final_score = intermediate * adjustment_factor
    
    # Step 6: Apply logarithmic compression
    compressed = math.log(final_score + 1) * 10
    
    # Step 7: Round to nearest integer
    final_diagnostic = int(round(compressed))
    
    # Irrelevant formatting distraction
    report_id = f"RPT-{sum(latest.values()):06d}"
    validation_tag = report_id.replace('RPT', 'V').swapcase()
    
    return final_diagnostic

# Global constants (some irrelevant)
SYSTEM_VERSION = 'v2.7.1'
CALIBRATION_OFFSET = 0.041
MAX_BUFFER_SIZE = 512

# Data setup
parsed_data = parse_telemetry(telemetry_stream)
health_scores = calculate_health_index(parsed_data)  # Computed but not used later
patterns_observed = analyze_patterns(parsed_data)

# System state with realistic naming
system_state = 'ACTIVE'

# Key execution point
final_diagnostic = process_metrics(parsed_data, system_state)

# Output result
print(f"Result: {final_diagnostic}")