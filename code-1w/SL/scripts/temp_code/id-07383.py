def preprocess_sensor_noise(readings):
    # Irrelevant function: simulates sensor calibration but unused
    adjusted = [r * 0.98 + 1.5 for r in readings if r > 0]
    return [a for a in adjusted if a < 100]

# Simulated agricultural zone metadata (mostly irrelevant)
site_info = {
    'zone_7A': {'soil_type': 'clay', 'ph': 6.2, 'moisture': 0.35},
    'zone_8B': {'soil_type': 'loam', 'ph': 5.8, 'moisture': 0.41},
    'zone_9C': {'soil_type': 'sandy', 'ph': 6.9, 'moisture': 0.28}
}

# Fake historical data – red herring
historical_yields = [
    [1200, 1250, 1180, 1300],
    [1150, None, 1210, 1290],
    [1170, 1190, 1205, 1310]
]

# Distractor: complex-looking but unused transformation
def transform_grid_layout(grid):
    transposed = list(zip(*grid))
    rotated = [list(reversed(col)) for col in transposed]
    return [[val * 1.05 if i % 2 == 0 else val for i, val in enumerate(row)] for row in rotated]

# Unused recursive decoy function
def forecast_yield_drift(base, years):
    if years <= 1:
        return base * 1.03
    return forecast_yield_drift(base * 1.02, years - 1)

# Core logic disguised among noise
area_data = [2.5, 3.0, 1.8, 4.2, 2.9]
yield_map =  [480, 520, 400, 580, 510]

# Real computation buried in distractions
def calculate_harvest_efficiency(areas, yields):
    total_area = sum(areas)
    weighted_sum = 0
    
    # Use enumerate and zip together as required
    for i, (area, yield_per_hectare) in enumerate(zip(areas, yields)):
        contribution = area * yield_per_hectare
        weighted_sum += contribution
        
        # Red herring: intermediate calculation that looks important
        if i % 2 == 0:
            dummy_offset = (contribution / total_area) * 0.01
            _ = round(dummy_offset, 3)  # Dead computation
    
    average_yield = weighted_sum / total_area
    
    # Additional distraction: unrelated adjustment table
    adjustment_table = {i: (1 + 0.01 * i) for i in range(len(areas))}
    adjusted_yield = average_yield
    for key, factor in adjustment_table.items():
        if key < 3:
            adjusted_yield *= factor  # Misleading inflation
        else:
            adjusted_yield /= factor  # Then deflation – cancels out roughly
    
    # Final relevant operation
    efficiency_ratio = 0.92
    final_output = adjusted_yield * efficiency_ratio
    
    # More decoys
    outlier_zones = [idx for idx, y in enumerate(yields) if y < 450]
    buffer_zone_penalty = len(outlier_zones) * 15
    
    return int(final_output - buffer_zone_penalty)  # Deterministic integer result

# Unused data structure – creates confusion
agronomic_flags = {
    'nitrogen_rich': True,
    'irrigation_active': False,
    'pest_detected': None
}

# Key execution point
final_yield = calculate_harvest_efficiency(area_data, yield_map)

# Print required output
print(f"Result: {final_yield}")