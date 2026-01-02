from collections import defaultdict
from itertools import cycle

# System diagnostics for thermal regulation unit
base_rating = 87
override_sequence = [3, 1, 4, 1, 5]
checksum = sum(x ** 2 for x in override_sequence)  # Irrelevant diagnostic metric

event_log = defaultdict(lambda: 'unknown')
event_log['startup'] = 'normal'
event_log['calibration'] = 'passed'

# Simulate sensor fluctuation (not affecting final result)
sensor_drift = 0
for i in range(5):
    sensor_drift += (i * 0.1) if i % 2 else -(i * 0.1)

# Primary control flags
critical_failure = False
degraded_mode = len(override_sequence) > 10  # Evaluates to False

# Efficiency calibration using cyclic pattern
efficiency_cycle = cycle([0.9, 0.95, 1.0])
efficiency_samples = []
for i in range(7):
    efficiency_samples.append(next(efficiency_cycle))

efficiency_factor = efficiency_samples[2] * efficiency_samples[5]  # 1.0 * 0.95 = 0.95

# Redundant state tracker (distractor)
system_states = set()
system_states.add('active')
system_states.add('monitoring')
status_history = list(system_states)  # Unused

# Bitwise integrity check (misleading but not used)
integrity_key = 0b1101
validation_mask = 0b1011
sanity_check = integrity_key & validation_mask  # 9

# Final capacity calculation (critical point)
thermal_capacity = base_rating * efficiency_factor

# Logging irrelevant summary
summary_code = ''.join(str(len(item)) for item in event_log.values())  # '6,6'

print(f"Result: {thermal_capacity}")