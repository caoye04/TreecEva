import math

# Simulated sensor data with noise and metadata
timestamps = list(range(100, 200))
raw_signal = [math.sin(i * 0.1) + 0.5 * math.cos(i * 0.3) for i in range(100)]
noise_floor = [0.1 * abs((i % 7) - 3) for i in range(100)]
decoy_signal = [(i ** 0.5) % 2.5 for i in range(100)]

# Irrelevant auxiliary data (distractor)
system_logs = [{'id': i, 'status': 'OK'} for i in range(50)]
historical_cache = {i: (i * 0.95) for i in range(80)}

# Data fusion with red herring operations
combined_metrics = []
for i in range(len(raw_signal)):
    metric = raw_signal[i] * 1.2 + noise_floor[i] * 0.8
    if i % 5 == 0:
        metric += 0.05
    # Unused transformation path (dead code)
    if i > 150:  # Never true
        metric = math.log(metric + 1)
    combined_metrics.append(round(metric, 4))

# Filtering logic obscured by irrelevant conditions
effective_threshold = 0.75
filtered_data = []
for val in combined_metrics:
    if val > effective_threshold:
        filtered_data.append(val)
    elif val < 0.2:
        # Rarely triggered, misleading branch
        filtered_data.append(val * 1.1)

# Decoy processing function (never called)
def analyze_pattern(seq):
    return sum(x ** 2 for x in seq if x > 1.0)

# Real processing chain
scaling_factor = 1.7
amplified = [x * scaling_factor for x in filtered_data]

# Conditional manipulation based on length (key dependency)
if len(amplified) % 2 == 0:
    processed = [x + 0.05 for x in amplified]
else:
    processed = [x - 0.02 for x in amplified]

# Aggregation with distraction
sum_snapshot = sum(processed[:10])
mean_shift = sum_snapshot / 10 if len(processed) > 0 else 0

# Core transformation
def transform_entry(x):
    if x > 1.0:
        return x * math.sqrt(2)
    else:
        return x * 1.414

transformed = [transform_entry(x) for x in processed]

# Secondary filter
valid_entries = [x for x in transformed if x < 3.0]

# Final computation obscured by decoy variables
temp_result = sum(valid_entries) * 0.9

# Misleading intermediate (looks important)
consistency_score = len(valid_entries) / (len(combined_metrics) + 1)

# Critical statement
final_output = int(temp_result * 100) / 100.0

print(f"Result: {final_output}")