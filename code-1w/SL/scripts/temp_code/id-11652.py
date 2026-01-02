from collections import defaultdict, Counter
import math

# Simulated sensor data and diagnostic pipeline
sensor_readings = [144, 25, 36, 49, 121, 81, 169, 64]
threshold_map = defaultdict(lambda: 50)
critical_flags = [False] * 10
diagnostic_cache = {}

# Irrelevant helper (dead code path)
def legacy_calibrate(x):
    return (x + 10) * 0.95

# Unused statistical summary
data_stats = {
    'mean': sum(sensor_readings) / len(sensor_readings),
    'max_val': max(sensor_readings),
    'min_val': min(sensor_readings),
    'range': max(sensor_readings) - min(sensor_readings)
}

# Bit manipulation red herring
def obfuscate(n):
    return ((n << 3) & 255) ^ 17

obfuscated_sequence = [obfuscate(x) for x in sensor_readings]

# Real processing begins here
health_trace = []
system_log = []

for reading in sensor_readings:
    root_val = int(math.sqrt(reading))
    is_perfect_square = (root_val * root_val == reading)
    
    # Conditional nesting with mixed logic
    if reading > threshold_map['critical']:
        if is_perfect_square:
            health_trace.append(root_val)
            if root_val % 2 == 0:
                system_log.append('STABLE_EVEN')
            else:
                system_log.append('STABLE_ODD')
        else:
            # Distractor branch with no real impact
            temp_flag = True
            for i in range(3):
                temp_flag = not temp_flag
            critical_flags[reading % 10] = True
    elif reading == threshold_map['warning']:
        system_log.append('CAUTION')
    else:
        continue

# Another irrelevant transformation
def useless_transform(seq):
    return [x for x in seq if x > 30]

filtered_diagnostics = useless_transform(obfuscated_sequence)

# Key data aggregation with lambda and Counter
frequency_count = Counter(health_trace)
penalty_func = lambda x: x ** 2 if x > 4 else x * 1.5

correction_factor = 0
for val, count in frequency_count.items():
    if count > 1:
        correction_factor += penalty_func(val)

# Simulate log analysis
alert_level = 0
for entry in system_log:
    if 'EVEN' in entry:
        alert_level += 1
    elif 'ODD' in entry:
        alert_level -= 1

# Final computation chain
intermediate_score = sum(health_trace) * correction_factor
if alert_level >= 0:
    intermediate_score = math.ceil(intermediate_score)
else:
    intermediate_score = math.floor(intermediate_score)

baseline_offset = len(system_log) * 3.5

# Critical statement
final_diagnostic = process_metrics(health_trace, system_log)

# Actual implementation of process_metrics (defined after usage to mislead)
def process_metrics(trace, log):
    base = sum(trace)
    adjustment = len(log) * 0.5
    noise_floor = 0
    
    # Simulated signal refinement
    for t in trace:
        if t in [5, 7, 11]:
            noise_floor += 0.1
    
    # Final formula
    result = (base + adjustment) - noise_floor
    return int(result * 10)  # Amplify for precision simulation

# Recompute final value correctly at end
final_diagnostic = process_metrics(health_trace, system_log)
print(f"Result: {final_diagnostic}")