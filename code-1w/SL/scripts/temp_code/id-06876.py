import itertools

# Simulated sensor array data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 22.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 51]
pressure_readings = [1013, 1012, 1015, 1010, 1014, 1016, 1009]

# Irrelevant auxiliary calculations (distractor)
baseline_offset = sum([abs(t - 24) for t in temperature_readings]) / len(temperature_readings)
sample_variance = (lambda x: sum((i - sum(x)/len(x))**2 for i in x)/len(x))(humidity_readings)

# Data alignment using itertools (relevant)
reading_frames = list(itertools.zip_longest(temperature_readings, humidity_readings, pressure_readings, fillvalue=0))

# Noise filtering with misleading intermediate results
filtered_frames = []
noise_threshold = 24.5
spike_count = 0
for frame in reading_frames:
    temp, humid, press = frame
    if temp > noise_threshold:
        spike_count += 1
    # Filter logic only applies to temperature spikes above threshold, but inclusion is conditional
    if temp <= noise_threshold or humid < 47:
        filtered_frames.append((temp, humid, press))

# Secondary irrelevant transformation (dead path)
decoy_aggregate = 0
for i, (t, h, p) in enumerate(filtered_frames):
    if i % 2 == 0 and p > 1012:
        decoy_aggregate += t * (h % 10)

# Core diagnostic scoring logic (relevant)
valid_readings_count = len(filtered_frames)
aggregate_temperature = sum(f[0] for f in filtered_frames)
average_temperature = aggregate_temperature / valid_readings_count if valid_readings_count else 0

# Conditional expression for stability classification (python idiom)
stability_flag = 'STABLE' if average_temperature < 24.0 and spike_count < 3 else 'UNSTABLE'

# Complexity bonus based on pattern density (logical operation with min/max)
pattern_density = len([f for f in filtered_frames if f[1] > 46 and f[2] < 1014])
complexity_bonus = 0.1 if pattern_density >= 3 else 0.05

# Masked adjustment using bitwise distraction (irrelevant)
adjustment_key = 0b101010
mask_applied = adjustment_key & 0b111100 ^ 0b001000  # Dead computation

# Final score calculation chain
base_score = sum(
    1 for t, h, p in filtered_frames 
    if 22.5 <= t <= 24.5 and 45 <= h <= 49 and 1011 <= p <= 1015
)

# Hidden dependency: only frames within nominal ranges contribute
range_compliant = [
    (t, h, p) for t, h, p in filtered_frames 
    if (t > 22.6 and t < 24.3) or (h > 45.5 and p < 1013.5)
]

# Critical logical misdirection: average uses one subset, score another
secondary_metric = len(range_compliant) * 0.75 if range_compliant else 0

# Actual answer-determining computation
aggregate_score = base_score + secondary_metric

# Key execution point: final diagnostic score applied
final_diagnostic = aggregate_score * (1 + complexity_bonus)

# Red herring output
print(f'Debug: Decoy aggregate = {decoy_aggregate}')
print(f'Status: {stability_flag}, Spikes: {spike_count}')

# Required result output
print(f'Result: {final_diagnostic}')