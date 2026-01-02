from itertools import groupby

# Simulated sensor readings over time (timestamp, temperature, active)
data_stream = [
    (1001, 23.5, True), (1002, 23.6, True), (1003, 24.1, False),
    (1004, 24.2, True), (1005, 24.5, True), (1006, 25.0, True),
    (1007, 25.1, False), (1008, 25.3, True), (1009, 25.6, True)
]

# Filter valid active periods
active_segments = []
temp_buffer = []
prev_active = False

for ts, temp, active in data_stream:
    if active:
        temp_buffer.append(temp)
        if not prev_active:
            # New segment start
            active_segments.append([])
        active_segments[-1].append(temp)
    prev_active = active

# Misleading computation: average of all temperatures (not used later)
all_temps = [temp for _, temp, _ in data_stream]
overall_avg = sum(all_temps) / len(all_temps) if all_temps else 0

# Another red herring: count transitions
transition_count = 0
last_state = False
for _, _, active in data_stream:
    if active != last_state:
        transition_count += 1
    last_state = active

# Process segments: compute variance in each active block
def compute_variance(vals):
    if len(vals) < 2:
        return 0.0
    mean = sum(vals) / len(vals)
    return sum((x - mean) ** 2 for x in vals) / len(vals)

segment_variances = [compute_variance(seg) for seg in active_segments]

# Compute total duration of active states (using timestamps)
active_durations = []
start_time = None
for ts, _, active in data_stream:
    if active and start_time is None:
        start_time = ts
    elif not active and start_time is not None:
        active_durations.append(ts - start_time)
        start_time = None
if start_time is not None:
    active_durations.append(data_stream[-1][0] - start_time)

total_active_time = sum(active_durations)

# Simulated calibration offset (unused but looks relevant)
calibration_factor = 1.05
adjusted_variances = [v * calibration_factor for v in segment_variances]  # unused

# Group data by rounded temperature for frequency analysis (semi-relevant)
sorted_by_temp = sorted([(temp, active) for _, temp, active in data_stream if active], key=lambda x: round(x[0]))
grouped_temps = {k: list(v) for k, v in groupby(sorted_by_temp, key=lambda x: round(x[0]))}
temp_frequency_score = len(grouped_temps)  # counts distinct rounded temps during active phases

# Main processing pipeline
processed_data = {
    'variance_level': sum(segment_variances),
    'duration_metric': total_active_time,
    'complexity_index': len(active_segments),
    'stability_hint': overall_avg,  # included but down-weighted
    'frequency_feature': temp_frequency_score
}

# Efficiency model (deterministic formula)
def calculate_efficiency(data):
    base = data['duration_metric'] * 10
    penalty = data['variance_level'] * 5
    bonus = data['frequency_feature'] * 2
    adjustment = data['complexity_index']  # small linear factor
    return int(base - penalty + bonus + adjustment)

# Critical execution point
efficiency_score = calculate_efficiency(processed_data)

# Print result as required
print(f"Result: {efficiency_score}")