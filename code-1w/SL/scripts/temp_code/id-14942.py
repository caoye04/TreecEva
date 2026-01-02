import math

def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal processing function (dead end)
    return (amplitude * math.sin(2 * math.pi * frequency + phase)) ** 2

def validate_checksum(data_sequence):
    # Unused validation logic (distractor)
    checksum = 0
    for val in data_sequence:
        checksum ^= val
    return checksum == 0

def transform_coordinates(x, y, z):
    # Geometric transformation with red herring variables
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    norm_x = x / (magnitude + 1e-9)
    norm_y = y / (magnitude + 1e-9)
    norm_z = z / (magnitude + 1e-9)
    return (norm_x, norm_y, norm_z)

def compute_entropy(signal):
    # Complex but irrelevant entropy calculation
    total = sum(signal)
    if total == 0:
        return 0.0
    probabilities = [s / total for s in signal if s > 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 6)

def aggregate_metrics(log_entries, flags):
    base_score = 0
    adjustment_factor = 1.0
    
    # Key logic: filter logs where 'latency' < 50 and 'status' is True
    relevant_entries = [entry for entry in log_entries if entry['latency'] < 50 and entry['status']]
    
    # Extract version numbers from entries (distractor usage)
    versions = [entry['version'] for entry in log_entries]
    unique_versions = list(set(versions))
    
    # Real computation path
    for entry in relevant_entries:
        base_score += entry['ops']
        
    # Bit manipulation decoy
    masked_score = base_score ^ 0xABC
    temp_flag = flags & 0xFFFF
    if temp_flag & 0x10:  # Unlikely condition
        adjustment_factor *= 0.9
    
    # Actual adjustment: only if high_priority flag set (bit 7)
    if flags & 0x80:
        adjustment_factor *= 1.25
    
    # Final score with distractor-influenced logic
    final_value = int(base_score * adjustment_factor)
    
    # Decoy dictionary operations
    stats_summary = {
        'count': len(log_entries),
        'valid_count': len(relevant_entries),
        'score_raw': base_score,
        'score_final': final_value,
        'versions_seen': unique_versions
    }
    
    # Critical result variable
    final_diagnostic = final_value + 50
    return final_diagnostic

# Simulated system telemetry data
timing_log = [
    {'latency': 45, 'ops': 120, 'status': True, 'version': 3, 'priority': 1},
    {'latency': 55, 'ops': 200, 'status': True, 'version': 3, 'priority': 0},  # filtered out (latency >= 50)
    {'latency': 30, 'ops': 85, 'status': True, 'version': 4, 'priority': 1},
    {'latency': 40, 'ops': 150, 'status': False, 'version': 4, 'priority': 1}, # filtered (status False)
    {'latency': 25, 'ops': 175, 'status': True, 'version': 5, 'priority': 0}
]

# System configuration flags (bitfield)
system_flags = 0x80  # Enables the 1.25 multiplier (bit 7 set)

# Unused intermediate computations (red herrings)
signal_data = [12, 45, 67, 89, 34]
entropy_metric = compute_entropy(signal_data)
phase_result = analyze_phase_shift(50.0, 2.5, math.pi / 4)
coord_transform = transform_coordinates(10, 20, 30)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")