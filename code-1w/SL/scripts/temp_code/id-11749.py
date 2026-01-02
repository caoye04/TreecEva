from collections import defaultdict, Counter

# Simulated agricultural sensor data across multiple farms
raw_data = [
    {'farm_id': 'A1', 'soil_ph': 6.2, 'temp_c': 24, 'humidity': 60, 'crop_type': 'wheat'},
    {'farm_id': 'A2', 'soil_ph': 5.8, 'temp_c': 26, 'humidity': 68, 'crop_type': 'wheat'},
    {'farm_id': 'B1', 'soil_ph': 7.1, 'temp_c': 22, 'humidity': 55, 'crop_type': 'corn'},
    {'farm_id': 'B2', 'soil_ph': 6.9, 'temp_c': 23, 'humidity': 58, 'crop_type': 'corn'},
    {'farm_id': 'C1', 'soil_ph': 4.5, 'temp_c': 27, 'humidity': 72, 'crop_type': 'rice'},
    {'farm_id': 'C2', 'soil_ph': 5.1, 'temp_c': 28, 'humidity': 75, 'crop_type': 'rice'}
]

# Irrelevant mapping (distractor)
crop_seeds = {'wheat': 25, 'corn': 18, 'rice': 40}

# Misleading preprocessing step (dead path)
def normalize_readings(data):
    result = []
    for entry in data:
        norm_entry = {k: v * 1.1 if isinstance(v, (int, float)) and k != 'soil_ph' else v for k, v in entry.items()}
        result.append(norm_entry)
    return result  # Never used

# Unused transformation function (red herring)
def transform_crop_code(crop_type):
    return sum(ord(c) for c in crop_type) % 100

# Distractor: Accumulates irrelevant stats
temp_stats = defaultdict(lambda: {'count': 0, 'total': 0})
for record in raw_data:
    crop = record['crop_type']
    temp_stats[crop]['count'] += 1
    temp_stats[crop]['total'] += record['temp_c']

# Fake clustering logic (unused)
humidity_ranges = [(0, 40), (41, 60), (61, 80)]
cluster_map = {}
for i, (low, high) in enumerate(humidity_ranges):
    cluster_map[i] = [f for f in raw_data if low <= f['humidity'] <= high]

# Real processing begins here
filtered_data = [entry for entry in raw_data if entry['soil_ph'] > 5.0]

# Character frequency analysis on farm_ids (irrelevant but plausible)
farm_chars = ''.join(entry['farm_id'] for entry in raw_data)
char_freq = Counter(farm_chars)

# More distractions: zip and enumerate used in non-critical path
indexed_humidity = []
for i, record in enumerate(raw_data):
    if record['temp_c'] > 25:
        indexed_humidity.append((i, record['humidity']))

paired_data = list(zip([r['temp_c'] for r in raw_data], [r['humidity'] for r in raw_data]))

# Core calculation setup
base_yield = {
    'wheat': 3.2,
    'corn': 4.1,
    'rice': 5.3
}

adjustment_factors = []
for entry in filtered_data:
    ph_adj = 1.0
    if entry['soil_ph'] < 6.0:
        ph_adj = 0.85
    elif entry['soil_ph'] > 6.8:
        ph_adj = 0.93
    else:
        ph_adj = 1.05

    temp_adj = 1.0
    if entry['temp_c'] < 23:
        temp_adj = 0.94
    elif entry['temp_c'] > 25:
        temp_adj = 0.88
    else:
        temp_adj = 1.02

    humidity_adj = 1.0
    if entry['humidity'] < 60:
        humidity_adj = 0.97
    elif entry['humidity'] > 70:
        humidity_adj = 0.91
    else:
        humidity_adj = 1.03

    adjustment_factors.append(ph_adj * temp_adj * humidity_adj)

# Secondary distractor: counting letters in crop names
letter_count = sum(len(crop) for crop in base_yield.keys())

# Actual yield computation
yields = []
for i, entry in enumerate(filtered_data):
    base = base_yield[entry['crop_type']]
    adj = adjustment_factors[i]
    yields.append(base * adj)

# Final aggregation
processed_data = {
    'average_yield': sum(yields) / len(yields),
    'total_records': len(yields),
    'peak_yield': max(yields)
}

# Critical function with misleading name but correct usage
def calculate_harvest_efficiency(data_dict):
    efficiency = data_dict['average_yield'] * data_dict['total_records']
    if data_dict['peak_yield'] > 4.5:
        efficiency *= 1.1
    return round(efficiency, 4)

# Key statement
final_yield = calculate_harvest_efficiency(processed_data)

# Output result
print(f"Result: {final_yield}")