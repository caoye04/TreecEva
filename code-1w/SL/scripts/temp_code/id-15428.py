def calculate_efficiency(data):
    base_efficiency = sum([x[0] * x[1] for x in data])
    penalty = 0
    for entry in data:
        duration, throughput, priority = entry
        if priority > 2:
            penalty += duration // (throughput + 1)
    return base_efficiency - penalty

# Simulated system performance logs
task_log = [
    (10, 5, 3),  # duration, throughput, priority
    (7, 8, 1),
    (12, 4, 4),
    (5, 10, 2)
]

# Irrelevant preprocessing: buffer analysis (distractor)
buffer_load = [t[0] // (t[1] + 1) for t in task_log]
peak_load = max(buffer_load) if buffer_load else 0
adjustment_factor = 0.9 if peak_load > 6 else 1.0

# Data transformation with red herring variables
transformed = []
for t in task_log:
    normalized_duration = round(t[0] / 2.5, 2)
    inverted_priority = 5 - t[2]  # unused distraction
    transformed.append((t[0], t[1], t[2]))  # effectively just copying

# Secondary metric (dead computation - not used)
weighted_priority = sum(t[2] * (t[0] / 10) for t in task_log)

# Actual processing pipeline
filtered_data = [t for t in transformed if t[1] >= 4]  # filter by throughput
processed_data = [(t[0] // 2 + t[1], t[1], t[2]) for t in filtered_data]

# Core efficiency calculation point
intermediate_debug = [p[0] - p[1] for p in processed_data]  # logged but unused

# Key statement
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")