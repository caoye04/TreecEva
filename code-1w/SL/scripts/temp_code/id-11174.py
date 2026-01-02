from itertools import zip_longest

def analyze_sensor_data(raw_readings):
    processed = []
    offset_correction = 0.987
    for i, val in enumerate(raw_readings):
        corrected = val * (1 + 0.02 * i) - offset_correction
        if corrected < 0:
            corrected = 0
        processed.append(round(corrected, 3))
    return processed

def build_energy_profile(timestamps, readings):
    profile = {}
    temp_cache = []
    for t, r in zip(timestamps, readings):
        adjusted_r = r * 1.05 if r > 50 else r * 0.95
n        temp_cache.append(adjusted_r)
        if len(temp_cache) % 3 == 0:
            avg_temp = sum(temp_cache[-3:]) / 3
            profile[t] = round(avg_temp, 2)
    # Dead code path - never accessed due to loop logic
    if len(temp_cache) == 0:
        profile['init'] = 0
    return profile

def calculate_thermal_output(energy_map, efficiency_log):
    total = 0.0
    base_multiplier = 1.1
    decay_factor = 0.95
    cumulative_loss = 0
    
    # Simulate time-decayed contribution from past states
    for i, (energy, efficiency) in enumerate(zip_longest(energy_map.values(), efficiency_log, fillvalue=1.0)):
        if i >= len(efficiency_log):  
            break
        raw_contribution = energy * efficiency * (base_multiplier * (decay_factor ** i))
        total += raw_contribution
        
        # Track loss without affecting main calculation
        instantaneous_loss = energy * (1 - efficiency)
        cumulative_loss += instantaneous_loss
        
    diagnostic_floor = int(total) - 100  # Irrelevant computation
    if diagnostic_floor < 0:
        diagnostic_floor = 0
    
    return round(total, 4)

# Main execution block
timestamps = [1000, 1001, 1002, 1003, 1004]
sensor_readings = [45, 67, 89, 34, 78]

# Step 1: Process sensor inputs
filtered_data = analyze_sensor_data(sensor_readings)

# Step 2: Build temporal energy map
energy_map = build_energy_profile(timestamps, filtered_data)

# Step 3: Generate synthetic efficiency log (simulating system wear)
efficiency_log = [0.92, 0.88, 0.85, 0.80, 0.75]

# Step 4: Compute thermal output with decay model
thermal_capacity = calculate_thermal_output(energy_map, efficiency_log)

# Misleading secondary calculation (dead-end)
redundant_capacity = sum(energy_map.values()) * efficiency_log[0]  # Not used later

# Final result output
print(f"Result: {thermal_capacity}")