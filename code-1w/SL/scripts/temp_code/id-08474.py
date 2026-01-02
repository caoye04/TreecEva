def preprocess(items):
    # Irrelevant transformation (distractor)
    return [x * 2 for x in items if x % 3 != 0]


def auxiliary_calc(data):
    # Dead function: never used but looks important
    total = 0
    for d in data:
        total += d ** 2
    return total // len(data) if data else 0

# Simulated sensor readings (red herring data)
sensor_log = {
    'temp': [23, 25, 22, 24, 26],
    'humidity': [45, 50, 55, 60, 65],
    'pressure': [1013, 1012, 1014, 1015, 1011]
}

# Unused complex structure (misleading)
config_template = {
    'version': '2.1',
    'mode': 'aggressive',
    'thresholds': {
        'low': 10,
        'high': 90,
        'critical': 95
    },
    'filters': ['noise', 'outlier', 'drift']
}

# Core configuration actually used (buried among noise)
config = {
    'scale': 3,
    'offset': -5,
    'active': True,
    'flags': [1, 0, 1]
}

# Raw input data
raw = [1, 2, 3, 4, 5]

# Step 1: Filter odd numbers (relevant)
filtered = [x for x in raw if x % 2 == 1]

# Step 2: Map to square (relevant)
processed = list(map(lambda x: x ** 2, filtered))  # [1, 9, 25]

# Step 3: Add dummy offset (partially relevant)
dummy_offset = 7  # distraction
adjusted = [x + config['offset'] for x in processed]  # [-4, 4, 20]

# Step 4: Transform via dictionary-based remapping (core logic)
remap_table = { -4: 100, 4: 200, 20: 300, 99: 999 }  # note: only 3 entries matter
transformed = [remap_table[x] for x in adjusted]  # [100, 200, 300]

# Step 5: Simulate legacy compatibility layer (irrelevant)
def legacy_support(mode='basic'):
    if mode == 'advanced':
        return sum([i*3 for i in range(10)]) // 2
    else:
        return 0

# Step 6: Real processing function (depends on config)
def process_data(values, cfg):
    scaled = [v * cfg['scale'] for v in values]  # [300, 600, 900]
    shifted = [s - 150 for s in scaled]          # [150, 450, 750]
    # Conditional mutation based on flag sum (actual dependency)
    flag_sum = sum(cfg['flags'])  # 2
    if flag_sum > 1:
        shifted = [x // 2 for x in shifted]  # [75, 225, 375]
    return sum(shifted)  # 75 + 225 + 375 = 675

# Misleading intermediate usage
placeholder = legacy_support('basic') + auxiliary_calc(sensor_log['temp'])

# Key execution point
final_output = process_data(transformed, config)

# Final result output
print(f"Result: {final_output}")