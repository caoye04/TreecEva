from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
data_stream = [
    ('temp', 23.5), ('humidity', 45), ('temp', 24.1), ('pressure', 1013),
    ('humidity', 47), ('temp', 23.9), ('temp', 24.0), ('pressure', 1012),
    ('humidity', 46), ('temp', 24.2), ('temp', 23.8), ('pressure', 1014),
    ('humidity', 48), ('temp', 24.0)
]

# Misleading variable - not used in final calculation
redundant_aggregates = {}
for key, value in data_stream:
    if key not in redundant_aggregates:
        redundant_aggregates[key] = []
    redundant_aggregates[key].append(value)

# Extract only temperature values for processing
temperatures = [value for key, value in data_stream if key == 'temp']

# Distractor: unused statistical computation
mean_temp = sum(temperatures) / len(temperatures)
variance_proxy = sum((x - mean_temp) ** 2 for x in temperatures)
fluctuation_index = variance_proxy / len(temperatures) if temperatures else 0

# State tracking with defaultdict (relevant)
reading_counts = defaultdict(int)
for key, _ in data_stream:
    reading_counts[key] += 1

# Use Counter to analyze frequency distribution (relevant for weighting)
frequency_stats = Counter(dict(reading_counts))
total_readings = sum(frequency_stats.values())
weight_map = {k: v / total_readings for k, v in frequency_stats.items()}

# Process temperature data: apply moving average filter (window size = 3)
smoothed_temps = []
for i in range(len(temperatures)):
    window = temperatures[max(0, i-1):min(len(temperatures), i+2)]
    smoothed_temps.append(sum(window) / len(window))

# Compute baseline stability metric (lower = more stable)
stability_metric = sum(abs(smoothed_temps[i] - smoothed_temps[i-1]) for i in range(1, len(smoothed_temps)))

# Normalize temperatures to z-score like scale using hardcoded reference
reference_mean = 24.0
reference_std = 0.5
normalized_deviations = [(t - reference_mean) / reference_std for t in smoothed_temps]

# Compute outlier-adjusted average (trim top and bottom 10%)
sorted_devs = sorted(normalized_deviations)
trim_count = max(1, len(sorted_devs) // 10)
trimmed_devs = sorted_devs[trim_count:-trim_count] if trim_count*2 < len(sorted_devs) else [0]
adjusted_avg_dev = sum(trimmed_devs) / len(trimmed_devs)

# Simulate auxiliary system status (distractor)
current_status = 'nominal'
if fluctuation_index > 0.1:
    current_status = 'caution'
status_code = hash(current_status) % 100  # Unused

# Prepare processed data structure for scoring
processed_data = {
    'readings': smoothed_temps,
    'deviation_score': abs(adjusted_avg_dev),
    'stability': stability_metric,
    'weight': weight_map.get('temp', 0.3)
}

# Auxiliary function with some irrelevant logic
def calculate_final_score(data):
    base_score = 100.0
    
    # Relevant penalty factors
    dev_penalty = data['deviation_score'] * 15
    stability_penalty = min(data['stability'] * 5, 30)
    
    # Irrelevant intermediate calculation (dead path)
    hypothetical_bonus = 0
    if data['weight'] > 0.5:
        hypothetical_bonus = 10  # Never triggered
    
    # Weighted adjustment (only weight from data is used)
    adjustment_factor = data['weight'] * 20
    
    # Final composition
    score_components = [
        base_score,
        -dev_penalty,
        -stability_penalty,
        adjustment_factor
    ]
    
    # Add misleading component that cancels out
    temp_bias = sum(1 for t in data['readings'] if t > 24.0)
    anti_bias = sum(1 for t in data['readings'] if t <= 24.0)
    balance_correction = (temp_bias - anti_bias) * 0.5  # Net zero effect
    
    final_score = sum(score_components) + balance_correction
    return round(final_score, 2)

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")