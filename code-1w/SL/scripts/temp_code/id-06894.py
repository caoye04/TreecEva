def calculate_thermal_capacity(components, efficiency_map):
    base_capacity = 0
    adjustment_factor = 1.0
    transient_buffer = 0
    stability_log = []
    
    for idx, (name, specs) in enumerate(components.items()):
        power_rating = specs['power']
        cooling_needed = specs['cooling']
        phase = specs['phase']
        
        # Irrelevant computation - logs but doesn't affect result
        transient_buffer += power_rating * (idx + 1) % 3
        if transient_buffer > 10:
            stability_log.append(transient_buffer)
            transient_buffer = 0

        # Real computation branch
        if phase == 2:
            base_capacity += power_rating * 0.85
        elif phase == 1:
            base_capacity += power_rating * 0.6
        else:
            base_capacity += power_rating * 0.4

        # Misleading efficiency adjustment (not actually used)
        temp_efficiency = efficiency_map.get(name, 1.0)
        dummy_adjustment = power_rating * (1 - temp_efficiency)
        adjustment_factor *= max(0.9, temp_efficiency)  # unused in final result

    # Additional distraction: processing unrelated metrics
    performance_markers = []
    for comp_name, eff in efficiency_map.items():
        if eff > 0.85:
            performance_markers.append((comp_name, 'HIGH'))
        elif eff > 0.7:
            performance_markers.append((comp_name, 'MEDIUM'))
    
    # Core logic continues: apply real efficiency from fixed rule
    total_efficiency = sum(efficiency_map.values()) / len(efficiency_map)
    final_multiplier = 0.9 if total_efficiency >= 0.8 else 0.75
    
    # Actual capacity calculation with real dependencies
    diagnostic_set = set()
    for name, specs in components.items():
        if specs['power'] > 100:
            diagnostic_set.add(f'{name}_high_load')

    enhanced_capacity = base_capacity * final_multiplier
    
    # Red herring: conditional that never triggers due to data
    if len(diagnostic_set) > 10:
        enhanced_capacity *= 0.5  # dead code path

    # Final adjustment based on tuple unpacking logic
    thresholds = [(200, 1.1), (150, 1.05), (100, 1.0), (50, 0.95)]
    bonus_multiplier = 1.0
    for threshold, multiplier in thresholds:
        if base_capacity > threshold:
            bonus_multiplier = multiplier
            break
    
    thermal_capacity = int(enhanced_capacity * bonus_multiplier)
    
    # Print required at end
    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Data setup
components = {
    'reactor_core': {'power': 120, 'cooling': 'active', 'phase': 2},
    'aux_heater': {'power': 45, 'cooling': 'passive', 'phase': 1},
    'condenser_unit': {'power': 80, 'cooling': 'hybrid', 'phase': 2},
    'booster_pump': {'power': 30, 'cooling': 'passive', 'phase': 3}
}

efficiency_map = {
    'reactor_core': 0.91,
    'aux_heater': 0.75,
    'condenser_unit': 0.87,
    'booster_pump': 0.65
}

# Execution point
thermal_capacity = calculate_thermal_capacity(components, efficiency_map)