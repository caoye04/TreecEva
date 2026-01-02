import itertools

# Simulated sensor readings and system diagnostics
sensor_raw = [127, 255, 184, 96, 203]
system_flags = [True, False, True, False]
baseline_offset = 42
temp_buffer = [x ^ baseline_offset for x in sensor_raw]

# Irrelevant pre-processing: noise calibration (unused later)
noise_profile = []
for i in range(len(sensor_raw)):
    if sensor_raw[i] > 128:
        noise_profile.append((i, sensor_raw[i] % 17))

# Decoy function: looks important but never called
def analyze_anomaly_pattern(data):
    return sum(d ** 2 for d in data if d & 1) // len(data)

# Misleading intermediate transformation
shifted = list(map(lambda x: (x << 2) & 255, temp_buffer))
filtered = [x for x in shifted if x % 3 == 0]
fake_aggregate = sum(filtered) / len(filtered) if filtered else 0

# Real data path begins here
sensor_data = {f'sensor_{i}': val for i, val in enumerate(sensor_raw)}
system_state = {
    'active': True,
    'mode': 'diagnostic',
    'checksum': 255,
    'version': 0x1A
}

# Conditional override that appears significant but is bypassed
current_mode = system_state['mode']
if current_mode == 'operational':
    baseline_offset *= 2
else:
    baseline_offset = 37  # This runs, but only matters indirectly

# Bit manipulation red herring
flag_mask = 0
for flag in system_flags:
    flag_mask <<= 1
    flag_mask |= int(flag)
flag_mask ^= 255  # Unused obfuscation

# Core logic disguised among distractions
def compute_health_index(data_dict, offset):
    values = list(data_dict.values())
    adjusted = [v - offset for v in values]
    squared_diffs = [(a - 50) ** 2 for a in adjusted]
    return sum(squared_diffs) // len(squared_diffs)

# Another decoy: complex but unused data structure
audit_trail = list(itertools.accumulate([len(str(x)) for x in sensor_raw]))
summary_stats = {k: v for k, v in zip(['stat_' + str(i) for i in range(5)], audit_trail)}

# Conditional expression with misleading branches
diagnostic_hint = (
    'severe' if fake_aggregate > 100 else
    'moderate' if sum(temp_buffer) < 500 else
    'normal'
)

# Unused bitwise diagnostic
consistency_check = 0
for k, v in sensor_data.items():
    consistency_check ^= v ^ ord(k[-1])

# Real aggregation function buried in code
def aggregate_metrics(data_map, state):
    vals = list(data_map.values())
    base = state.get('checksum')
    mode_flag = 1 if state.get('active') else -1
    
    # Critical calculation hidden among less relevant ops
    primary_sum = sum(v & base for v in vals)
    secondary_sum = sum(v | (base >> 2) for v in vals)
    ratio_metric = primary_sum / secondary_sum
    
    # Final transformation using modular arithmetic and conditional logic
    if mode_flag > 0:
        result = (ratio_metric * 1000) % 973 + baseline_offset
    else:
        result = (ratio_metric * 500) % 487
    
    # One final adjustment
    result = int(result) + (1 if diagnostic_hint == 'normal' else 0)
    return result

# Key execution point
final_diagnostic = aggregate_metrics(sensor_data, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")