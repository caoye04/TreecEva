from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
raw_readings = [3, 5, 7, 11, 13, 17, 19, 23]

# Irrelevant initialization - red herring variables
temp_cache = {'a': [], 'b': {}, 'c': set()}
dummy_matrix = [[0] * 4 for _ in range(4)]
scalar_offset = sum([x % 3 for x in range(100)]) // 97  # Misleading computation

# Real data transformation path
processed = [x ** 2 - x for x in raw_readings]
filtered = [x for x in processed if x > 50]

# Bit manipulation decoy - unused but plausible
bit_analysis = 0
for x in raw_readings:
    bit_analysis ^= (x << 2) | (x >> 1)

# Unused helper function - dead code path
def legacy_calibrate(data):
    return [d + 2 * i for i, d in enumerate(data)]

# Another distractor: complex combinatorics with no impact
total_pairs = 0
for i in range(len(raw_readings)):
    for j in range(i + 1, len(raw_readings)):
        if (raw_readings[i] + raw_readings[j]) % 5 == 0:
            total_pairs += 1

# Actual signal extraction via frequency counting
element_freq = Counter(filtered)
unique_signals = list(element_freq.keys())

# Decoy dictionary aggregation
aggregated_diagnostics = defaultdict(list)
for val in filtered:
    aggregated_diagnostics['group_1'].append(val % 7)
    aggregated_diagnostics['group_2'].append(val % 9)

# Control flow distraction with short-circuiting
trigger = len(filtered) > 5 and (not False or True) and scalar_offset == 3
override_flag = False
if trigger and not override_flag:
    dummy_correction = [x * 1.5 for x in filtered if x % 2 == 0]
else:
    dummy_correction = []

# Core configuration - relevant
config = {
    'threshold': 120,
    'mode': 'strict',
    'factors': [2, 3]
}

# Transformation that matters
transformed_data = []
for x in unique_signals:
    temp_val = x
    if x > config['threshold']:
        temp_val = (temp_val // config['factors'][0]) + config['factors'][1]
    transformed_data.append(temp_val)

# Conditional expression distraction
status_flag = 'active' if sum(transformed_data) > 300 else 'standby'
system_state = 1 if status_flag == 'active' else 0

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Critical function: pattern analysis with interleaved logic
def analyze_pattern(data, cfg):
    base_score = 0
    penalty = 0
    
    for i, val in enumerate(data):
        # Relevant arithmetic and control flow
        if cfg['mode'] == 'strict':
            if val % cfg['factors'][0] == 0:
                base_score += int(math.log(val + 1, cfg['factors'][0]))
            else:
                penalty += 1
        
        # Distracting bitwise operation inside loop (no real effect)
        mask = (val ^ (val & (val >> 1))) & 0xF
        _ = mask << 2  # Unused
    
    # Final computation - only base_score and penalty matter
    adjustment = len(data) // cfg['factors'][1]
    return base_score - penalty + adjustment

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, config)

# Print required output
print(f"Result: {final_diagnostic}")