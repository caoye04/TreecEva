def analyze_growth_patterns(data_map):
    growth_rate = {}
    for key, readings in data_map.items():
        base = readings[0]
        peak = max(readings)
        rate = (peak - base) / base if base != 0 else 0
        growth_rate[key] = round(rate, 4)
    return growth_rate

sensor_data = {
    'sector_A': [12, 15, 13, 17, 20],
    'sector_B': [8, 10, 9, 14],
    'sector_C': [25, 24, 28, 30, 32, 29]
}

thresholds = {
    'min_growth': 0.15,
    'tolerance': 0.05,
    'max_fluctuation': 0.25
}

# Irrelevant transformation - distractor
inverted_map = {k: [1/x for x in v if x != 0] for k, v in sensor_data.items()}
decay_rates = analyze_growth_patterns({k: v[::-1] for k, v in sensor_data.items()})

# Unused helper function - dead code path
compute_zscore = lambda values, mean: [(v - mean) / (sum(values)/len(values)) for v in values]

mean_baseline = sum([sum(v) for v in sensor_data.values()]) / sum(len(v) for v in sensor_data.values())

# Simulate noise filtering (semi-relevant but not used in final result)
filtered_data = {}
for sector, logs in sensor_data.items():
    filtered = [x for x in logs if x >= mean_baseline * 0.8]
    filtered_data[sector] = filtered

# Core logic disguised among distractions
def calculate_optimal_yield(data, config):
    rates = analyze_growth_patterns(data)
    yield_values = []
    for sector, rate in rates.items():
        if rate >= config['min_growth']:
            adjustment = config['tolerance'] if rate < config['min_growth'] + config['max_fluctuation'] else 0
            adjusted_yield = (rate + adjustment) * 1000
            yield_values.append(adjusted_yield)
    # Key computation step
    total_yield = sum(yield_values)
    count = len(yield_values)
    return int(total_yield / count) if count > 0 else 0

# Misleading intermediate calculation
temp_analysis = {k: sum(v) * 0.1 for k, v in filtered_data.items()}

# Critical execution point
final_yield = calculate_optimal_yield(sensor_data, thresholds)

# Print required output
print(f"Result: {final_yield}")