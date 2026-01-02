from collections import defaultdict

# System configuration parameters
default_response_time = 120
event_log = ['startup', 'calibration', 'idle']

# Define active filter modes and current system operations
filter_profiles = {1: 'high_throughput', 2: 'low_latency', 3: 'energy_saving', 4: 'diagnostic'}
efficient_filters = {2, 3, 4}
operational_modes = {1, 3, 4, 5}

# Performance tracking setup
task_counter = defaultdict(int)
task_counter['initialization'] += 1

# Determine overlap between efficient filters and current operations
filtration_score = len(efficient_filters & operational_modes)

# Log final result
task_counter['evaluation'] += 1
print(f"Result: {filtration_score}")