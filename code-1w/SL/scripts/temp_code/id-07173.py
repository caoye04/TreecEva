import itertools

# Simulate agricultural yield prediction with noise filtering and red herrings
def analyze_crop_performance(data, threshold=0.75):
    smoothed = []
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        if avg > threshold:
            smoothed.append(avg)
    return smoothed

# Irrelevant helper: processes unrelated sensor metadata
def parse_sensor_tags(tags):
    result = {}
    for tag in tags:
        if 'calib' in tag:
            result[tag] = True
    return result  # Dead end, never used

# Decoy function: looks important but unused
def calculate_root_depth(soil_data):
    depth = 0
    for layer in soil_data:
        if layer > 0.5:
            depth += 0.3
    return depth * 1.5

# Main simulation with multiple distractions
years = [2020, 2021, 2022, 2023]
crop_data = {
    2020: [0.4, 0.6, 0.8, 0.7],
    2021: [0.5, 0.7, 0.6, 0.9],
    2022: [0.3, 0.8, 0.7, 0.6],
    2023: [0.6, 0.9, 0.8, 0.7]
}

# Fake sensor logs - irrelevant
tags = ['sensor_1_calib', 'sensor_2_raw', 'sensor_3_calib']
sensor_analysis = parse_sensor_tags(tags)

# Real processing begins
all_values = list(itertools.chain.from_iterable(crop_data.values()))
filtered = [v for v in all_values if v >= 0.6]
smoothed_data = analyze_crop_performance(filtered)

# Simulated seasonal efficiencies (distraction map)
efficiency_map = {
    'spring': 1.1,
    'summer': 1.3,
    'autumn': 0.9,
    'winter': 0.4
}

# Red herring: complex sorting that leads nowhere
decoy_sorted = sorted(smoothed_data, key=lambda x: abs(x - 0.75))
offset_index = 0
for idx, val in enumerate(decoy_sorted):
    if val > 0.7:
        offset_index += idx * 0.1
        break

# Actual critical path starts here
baseline = sum(smoothed_data) / len(smoothed_data)
adjusted = baseline * 1.15  # Model correction factor

# Seasonal scaling with zip and enumerate (required python features)
seasons = ['spring', 'summer', 'autumn', 'winter']
growth_rates = [1.05, 1.2, 0.85, 0.5]

rate_map = {}
for season, rate in zip(seasons, growth_rates):
    rate_map[season] = rate

# Apply real transformation
harvest = {}
for i, year in enumerate(years):
    scaling = growth_rates[i % 4]
    base_yield = adjusted * scaling
    harvest[year % 4] = base_yield  # Map year to index: 2020->0, 2021->1, etc.

# Introduce more noise: unused branch
if len(harvest) > 5:
    extra = 0
    for k in harvest:
        extra += k * 0.01

# Critical execution point
efficiency_factor = efficiency_map['summer']  # Key multiplier
season = 1  # Corresponds to 2021 -> index 1
final_yield = harvest[season] * efficiency_factor

# Output the target result
print(f"Result: {final_yield}")