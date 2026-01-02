from collections import defaultdict, Counter
import math

# Simulated sensor input data (irrelevant to final result but looks important)
sensor_readings = [0.87, 0.91, 0.76, 0.88, 0.95, 0.67, 0.74, 0.83]
baseline_adjustment = sum(sensor_readings) / len(sensor_readings)
normalized_scores = [round((x - baseline_adjustment) * 100) for x in sensor_readings]

def analyze_trend(data):
    # Distractor function: never called in execution path
    return sum(x > 0 for x in data) > len(data) // 2

def compute_entropy(sequence):
    # Another decoy function with plausible scientific use
    freqs = Counter(sequence)
    total = len(sequence)
    return -sum((count / total) * math.log2(count / total) for count in freqs.values())

def validate_checksum(structure):
    # Misleading validation logic that seems critical but is unused
    checksum = 0
    for i, val in enumerate(structure):
        checksum ^= (val * (i + 1)) % 256
    return checksum == 0x7F

# System configuration profiles (partially relevant)
config_profiles = {
    'high_throughput': {'latency_weight': 0.3, 'bandwidth_cap': 850},
    'low_latency': {'latency_weight': 0.7, 'bandwidth_cap': 600},
    'balanced': {'latency_weight': 0.5, 'bandwidth_cap': 720}
}

# Legacy diagnostic thresholds (red herring)
thresh_map = defaultdict(lambda: 0.75)
thresh_map.update({'critical': 0.9, 'warning': 0.6})

# Core state variables
system_load = [45, 62, 53, 77, 68, 59, 81, 73, 64, 70]
active_modules = ['A', 'B', 'C', 'D', 'E', 'F']
module_cycles = {'A': 1200, 'B': 950, 'C': 1340, 'D': 890, 'E': 1120, 'F': 980}

# Bitmask simulation for hardware flags (distractor)
hw_status_flag = 0b101101
is_overclocked = bool(hw_status_flag & 0b1000)
has_fan_alert = bool(hw_status_flag & 0b10)
fan_rpm = 2400 if not has_fan_alert else 3200

# Intermediate transformation chain with red herrings
temp_buckets = defaultdict(int)
for load in system_load:
    bucket = (load // 10) * 10
    temp_buckets[bucket] += 1

# Unused statistical summary
dist_summary = {k: round(v / len(system_load), 2) for k, v in temp_buckets.items()}

# Critical path begins here -- actual computation branch
health_signature = []
for i, val in enumerate(system_load):
    shifted = (val ^ (i << 2)) + 5
    if shifted % 3 == 0:
        shifted = shifted // 3
    elif shifted % 2 == 0:
        shifted = shifted // 2
    health_signature.append(shifted)

# Complex processing involving multiple concepts
def process_metrics(signature, load_profile):
    # Step 1: frequency analysis of transformed values
    freq_analysis = Counter(signature)
    
    # Step 2: weighted decay based on position
    decayed_sum = 0
    for idx, val in enumerate(reversed(signature)):
        weight = 0.95 ** idx
        decayed_sum += val * weight
    
    # Step 3: bitwise reduction
    accumulated = 0
    for x in signature:
        accumulated ^= (x * 3) & 0xFFFF
    
    # Step 4: combine with aggregate load statistics
    avg_load = sum(load_profile) / len(load_profile)
    peak_load = max(load_profile)
    load_ratio = avg_load / peak_load if peak_load else 0
    
    # Step 5: compose final metric
    raw_metric = (decayed_sum * 0.6) + (accumulated * 0.001) + (load_ratio * 100)
    
    # Step 6: apply nonlinear compression
    compressed = math.log(1 + abs(raw_metric)) * 10
    
    # Step 7: inject fake dependency on unused module data
    cycle_total = sum(module_cycles[m] for m in ['A', 'C', 'E'])  # only uses subset
    adjustment_factor = (cycle_total % 100) / 100.0
    
    # Final adjustment (only this line matters for answer)
    final_value = compressed - adjustment_factor
    
    return round(final_value, 4)

# Dead code path -- looks like initialization but unused
if __name__ == "__main__":
    debug_mode = False
    if debug_mode:
        print("Debug: Initializing diagnostics")

# Execution point of interest
final_diagnostic = process_metrics(health_signature, system_load)
print(f"Target result: {final_diagnostic}")