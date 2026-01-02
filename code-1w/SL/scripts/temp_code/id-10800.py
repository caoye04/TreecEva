import itertools

# Simulated sensor data stream with noise
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
noise_floor = 2
threshold = 4
smoothing_factor = 0.1

# Step 1: Filter out values below noise floor
cleaned_data = [x for x in data_stream if x > noise_floor]

# Misleading transformation - not used in final computation
transformed_data = list(map(lambda x: x ** 2 - smoothing_factor * x, cleaned_data))
dummy_stat = sum(transformed_data) / len(transformed_data) if transformed_data else 0

# Step 2: Group consecutive values above threshold using itertools
runs = []
current_run = 0
for k, g in itertools.groupby(cleaned_data, key=lambda x: x >= threshold):
    group = list(g)
    if k:
        runs.append(sum(group))
    current_run += len(group)  # distractor counter

dummy_run_count = len(runs) + (1 if dummy_stat > 20 else 0)  # semi-relevant but unused

# Step 3: Apply weighted accumulation with decay on runs
accumulated_power = 0
for i, run_sum in enumerate(runs):
    weight = 0.9 ** i
    accumulated_power += run_sum * weight

# Step 4: Normalize by number of original high-signal segments
normalization_base = len([x for x in data_stream if x >= threshold])
normalized_power = accumulated_power / normalization_base if normalization_base else 0

# Step 5: Process signals based on dynamic criteria
def process_signals(data, thresh):
    if not data:
        return 0
    # Real logic: count how many times value alternates above/below adjusted threshold
    adjusted_values = [x for x in data if x != thresh]  # minor filtering
    cross_count = 0
    for i in range(1, len(adjusted_values)):
        if (adjusted_values[i-1] > thresh) != (adjusted_values[i] > thresh):
            cross_count += 1
    # Final transformation combining cross count and normalized power
    local_metric = cross_count * 1.5 + normalized_power
    return int(local_metric) if local_metric >= 5 else round(local_metric, 3)

# Distractor function - never called
def auxiliary_diagnostic(x):
    return [i for i in range(len(x)) if x[i] == max(x)]

# Unused state tracking
state_log = {'init': True, 'phase': 'idle', 'value': dummy_stat}

# Key execution point
final_output = process_signals(filtered_data=[x for x in cleaned_data if x % 2 == 1], threshold=threshold)

print(f"Result: {final_output}")