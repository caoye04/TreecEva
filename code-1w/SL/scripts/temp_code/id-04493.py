def analyze_workload(entries):
    base_load = sum([e[1] for e in entries])
    peak_load = max([e[1] for e in entries])
    avg_load = base_load / len(entries)
    
    # Irrelevant statistics (distractors)
    outlier_count = len([x for x in entries if x[1] > 2 * avg_load])
    normalized_entries = [(idx, val/peak_load) for idx, val in enumerate([e[1] for e in entries])]
    
    return base_load, avg_load, peak_load


def calculate_efficiency(data, factor):
    adjusted = [x * (1 + factor) for x in data]
    squared_residuals = [(x - sum(adjusted)/len(adjusted))**2 for x in adjusted]
    variance = sum(squared_residuals) / len(squared_residuals)
    return int(sum(adjusted) / (variance + 1))

# Simulate system task processing
raw_tasks = [
    ('init', 15), ('parse', 23), ('resolve', 18), ('validate', 31), ('finalize', 11)
]

# Extract relevant timing data
timings = [task[1] for task in raw_tasks]

# Auxiliary transformations (some irrelevant)
indexed_timings = list(enumerate(timings))
shifted_timings = [t << 1 for t in timings]  # Bit-shift distraction
filtered_timings = [t for t in timings if t > 15]

# Overhead simulation (only 'base' and 'avg' are used; others are distractions)
work_stats = analyze_workload(raw_tasks)
base_workload = work_stats[0]
avg_workload = work_stats[1]
peak_workload = work_stats[2]  # Unused downstream

scaling_factor = 0.15
overhead_factor = scaling_factor * (avg_workload / base_workload)

# Core computation path
processed_data = [t * (1.0 + overhead_factor) for i, t in indexed_timings if t < 30]  # Exclude finalize

# Introduce red herring with zip and string manipulation
labels = [t[0].title() for t in raw_tasks]
correlated = list(zip(labels, timings))
diagnostic_str = ''.join([c for s in labels for c in s])  # String distractor
checksum = sum([ord(c) % 5 for c in diagnostic_str])  # Dead-end calculation

# Key statement
efficiency_score = calculate_efficiency(processed_data, overhead_factor)

Result: {efficiency_score}