def analyze_soil_composition(data):
    # Irrelevant soil analysis with decoy computations
    ph_levels = [7.1, 6.8, 7.3, 6.9, 7.0]
    nutrient_score = 0
    for entry in data:
        nutrient_score += entry.get('nitrogen', 0) * 0.3
        nutrient_score += entry.get('phosphorus', 0) * 0.5  # Misleading weight
    return nutrient_score // len(data) if data else 0

def preprocess_sensor_readings(readings):
    # Distractor: sensor calibration that isn't used later
    calibrated = []
    offset = 0.23
    for r in readings:
        calibrated.append(r + offset if r < 50 else r - offset)
    smoothed = [sum(calibrated[i:i+3]) / 3 for i in range(len(calibrated) - 2)]
    return smoothed

def decode_growth_pattern(sequence):
    # Complex but irrelevant pattern decoder (dead path)
    binary_seq = ''.join(['1' if x > 0 else '0' for x in sequence])
    decimal_value = int(binary_seq[:8], 2) if len(binary_seq) >= 8 else 0
    return decimal_value ^ 255  # Red herring operation

def calculate_harvest_efficiency(areas, cycles):
    # Core relevant logic buried in noise
    efficiency_map = {}
    for i, area in enumerate(areas):
        total_yield = 0
        for j, cycle in enumerate(cycles[i]):
            # Key calculation: yield depends on area and growth rate
            growth_rate = cycle.get('rate', 1.0)
            pest_factor = cycle.get('pests', False)
            if pest_factor:
                growth_rate *= 0.6
            total_yield += area * growth_rate * (1 + 0.1 * j)  # Compounded over cycles
        efficiency_map[i] = total_yield / len(cycles[i])
    
    # Irrelevant aggregation distraction
    avg_efficiency = sum(efficiency_map.values()) / len(efficiency_map)
    max_efficiency = max(efficiency_map.values())
    
    # Actual answer derivation
    base_yield = efficiency_map[0]  # First plot's average yield
    bonus = 0
    if len(efficiency_map) > 1 and efficiency_map[1] > efficiency_map[0]:
        bonus = (efficiency_map[1] - efficiency_map[0]) * 0.25
    final_yield = int(base_yield + bonus)  # Final deterministic integer result
    
    # Unused complex transformation (distractor)
    inverted = {v: k for k, v in efficiency_map.items()}
    sorted_pairs = sorted(inverted.items(), reverse=True)
    
    return final_yield

# Simulated agricultural dataset
area_metrics = [120.5, 135.0, 110.2]
growth_cycles = [
    [
        {'rate': 1.2, 'pests': False},
        {'rate': 1.3, 'pests': True},
        {'rate': 1.5, 'pests': False}
    ],
    [
        {'rate': 1.1, 'pests': False},
        {'rate': 1.4, 'pests': False},
        {'rate': 1.3, 'pests': False}
    ],
    [
        {'rate': 1.0, 'pests': True},
        {'rate': 1.1, 'pests': True},
        {'rate': 1.2, 'pests': False}
    ]
]

# Dead code paths with misleading calls
soil_data = [{'nitrogen': 8, 'phosphorus': 5}, {'nitrogen': 7, 'phosphorus': 6}]
sensor_logs = [45, 52, 48, 55, 49]
_ = analyze_soil_composition(soil_data)
_ = preprocess_sensor_readings(sensor_logs)
_ = decode_growth_pattern([1, -1, 1, 0, 1, -1, 1])

# Key execution point
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
print(f"Target result: {final_yield}")