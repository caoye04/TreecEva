from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (0.12, 'sensor_A', 'start'),
    (0.35, 'sensor_B', 'start'),
    (0.45, 'sensor_A', 'read'),
    (0.67, 'sensor_B', 'read'),
    (0.72, 'sensor_A', 'end'),
    (0.95, 'sensor_B', 'end')
]

system_flags = {
    'calibration_needed': False,
    'overclock_active': True,
    'legacy_mode': False,
    'power_saving': True
}

# Irrelevant helper: computes signal jitter (not used in final result)
def compute_jitter(log):
    intervals = []
    for i in range(1, len(log)):
        intervals.append(round(log[i][0] - log[i-1][0], 4))
    return sum(intervals) / len(intervals) if intervals else 0.0

# Distractor function: analyzes only sensor_A (misleading path)
analyze_sensor_A = lambda log: [entry for entry in log if entry[1] == 'sensor_A']

# Dead code path — never invoked
def legacy_compatibility_map(flags):
    mapping = {}
    for k, v in flags.items():
        mapping['old_' + k] = not v
    return mapping

# Unused intermediate: simulates power profile
power_profile = []
for i, event in enumerate(timing_log):
    phase = 'high' if i % 2 == 0 else 'low'
    power_profile.append((event[0], phase, round(math.sin(i + 0.5), 3)))

# Misleading metric: counts total events per sensor (not directly used)
event_counter = Counter(entry[1] for entry in timing_log)

# Real processing begins here — nested logic with distractors
status_timeline = defaultdict(list)
for timestamp, sensor, status in timing_log:
    status_timeline[sensor].append((timestamp, status))

processing_weights = {
    'start': 1.0,
    'read': 1.5,
    'end': 0.8
}

# Core transformation: compute weighted duration per sensor
duration_metrics = {}
for sensor, events in status_timeline.items():
    start_time = None
    total_weight = 0.0
    for ts, st in events:
        weight = processing_weights.get(st, 1.0)
        total_weight += weight
        if st == 'start':
            start_time = ts
        elif st == 'end' and start_time is not None:
            duration = ts - start_time
            # Only store duration if read occurred in between
            has_read = any(s == 'read' for _, s in events)
            if has_read:
                duration_metrics[sensor] = round(duration * total_weight, 4)

# Secondary flag-based adjustment
overclock_multiplier = 1.25 if system_flags['overclock_active'] else 1.0
safety_dampener = 0.9 if not system_flags['calibration_needed'] else 0.7

# Dummy list comprehension — looks important but unused
baseline_norm = [round(d * safety_dampener, 3) for d in duration_metrics.values()]

# Critical red herring: partial aggregation that ignores sensor_B
temp_aggregate = 0
for sensor, dur_val in duration_metrics.items():
    if sensor == 'sensor_A':
        temp_aggregate += dur_val * overclock_multiplier

# Actual core logic: combines both sensors with modular weighting
composite_score = 0
for idx, (sensor, value) in enumerate(duration_metrics.items()):
    factor = (idx + 1) * 2.1
    adjusted = value * factor * overclock_multiplier * safety_dampener
    composite_score += adjusted

# Final transformation using slicing and lambda
metric_keys = sorted(duration_metrics.keys())
sliced_reference = metric_keys[:2]  # Redundant but looks intentional
scoring_engine = lambda x: round(x ** 1.1, 4)

# Final diagnostic computed from composite score and flag state
interim_value = composite_score * (1.1 if system_flags['power_saving'] else 1.3)
final_diagnostic = scoring_engine(interim_value)

# Output the target result
print(f"Target result: {final_diagnostic}")