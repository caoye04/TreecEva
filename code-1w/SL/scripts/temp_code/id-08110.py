from itertools import combinations, chain
import math

# Irrelevant utility function (dead code)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading data transformation
temp_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 21.9]
offset = sum(temp_readings) / len(temp_readings) - 20
adjusted_temps = [t - offset for t in temp_readings]
rolling_avg = sum(adjusted_temps[-3:]) / 3

# Real computation begins: system health evaluation
def evaluate_component_stability(logs):
    critical_flags = 0
    for entry in logs:
        if entry['error_count'] > 5 and entry['recovery_time'] > 100:
            critical_flags += 1
    return critical_flags < 2

# Decoy function with plausible name but unused
def calculate_entropy(data):
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    return -sum((f / len(data)) * math.log2(f / len(data)) for f in freq.values())

# Core logic disguised among distractors
raw_metrics = [
    {'id': 'A', 'base': 87, 'adjustment': 13, 'mode': 'active'},
    {'id': 'B', 'base': 92, 'adjustment': -8, 'mode': 'idle'},
    {'id': 'C', 'base': 76, 'adjustment': 24, 'mode': 'active'},
    {'id': 'D', 'base': 81, 'adjustment': 19, 'mode': 'active'}
]

# Irrelevant string processing (distractor)
status_labels = ['OK', 'WARNING', 'CRITICAL']
label_map = {i: s.lower() for i, s in enumerate(status_labels)}
coded_status = ''.join(chain.from_iterable(zip(label_map[0], label_map[1])))

# Fake accumulation with no effect
buffer_cache = 0
for i in range(4):
    buffer_cache += (i + 1) * 17

# Real data preparation
active_bases = [
    m['base'] + m['adjustment'] 
    for m in raw_metrics 
    if m['mode'] == 'active'
]

# Simulated sensor fusion (some steps are red herrings)
sensor_fusion = lambda x, y: (x * 1.05 + y * 0.95) / 2
fused_value = sensor_fusion(active_bases[0], active_bases[1])

# Dummy statistical check (unused)
variance_proxy = (max(active_bases) - min(active_bases)) / 2

# Key intermediate: weighted contribution
contributions = []
for idx, val in enumerate(active_bases):
    weight = 1.1 if val >= 90 else 0.95
    adjusted_val = val * weight
    if adjusted_val > 100:
        adjusted_val = 98.5  # cap
    contributions.append(adjusted_val)

# Secondary adjustment based on composite threshold
baseline = sum(contributions) / len(contributions)
boost_factor = 1.15 if baseline > 94 else (1.05 if baseline > 90 else 0.98)

# Tertiary interference: bitwise decoy
checksum = 0
for c in contributions:
    int_part = int(c)
    checksum ^= (int_part & 255) ^ (int_part >> 8)

# Another irrelevant sequence
permutations = list(combinations([1, 2, 3, 4], 3))
path_count = len(permutations)

# Actual final computation hidden in complex structure
def compute_aggregate(data, fuse, base_val, boost):
    # Multi-step reasoning path
    raw_total = sum(data)
    fused_enhancement = fuse * 0.7
    effective_total = raw_total + fused_enhancement
    applied_boost = effective_total * boost
    
    # Conditional correction
    correction = 0
    if applied_boost > 300 and len(data) >= 3:
        correction = -5.25
    elif any(d > 100 for d in data):
        correction = 2.1
    
    # Final damping factor
    damping = 0.97 if effective_total > 280 else 1.0
    
    result = (applied_boost + correction) * damping
    
    # Dead branch: never reached due to logic
    if result < 0:
        result = abs(result) * 0.5
        
    return result

# Execution point of interest
final_score = compute_aggregate(contributions, fused_value, baseline, boost_factor)

# Output required format
print(f"Target result: {final_score}")