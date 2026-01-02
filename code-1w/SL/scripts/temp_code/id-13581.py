def process_floral_data(data_entries):
    total_entries = len(data_entries)
    normalized = [entry.strip().lower() for entry in data_entries]
    valid_count = sum(1 for item in normalized if 'flower' in item)
    return valid_count

# Simulate sensor readings from garden zones
data_log = [
    ' FLOWER_ZONE_1 ',
    'WEED_AREA',
    'FlOwEr_zone_2',
    'ROCK_BED',
    'FLOWER_ZONE_3 '
]

# Environmental factors
humidity = 68
soil_ph = 6.4
bee_efficiency = 0.82 + (humidity * 0.001)  # Enhanced by humidity

# Distraction: Irrelevant temperature scaling
temp_celsius = 24.5
kelvin_offset = 273.15
adjusted_temp = temp_celsius + kelvin_offset  # Not used later

# Flower counts per zone (aligned with log)
flowers = [120, 0, 95, 0, 140]

# Distractor: unused transformation
inverted_ph = round((14 - soil_ph), 2)

# Validate input through dummy check
valid_records = process_floral_data(data_log)
expected_records = 5
mismatch_penalty = abs(expected_records - valid_records) * 5

# Primary logic: yield calculation with recursive helper
def calculate_harvest(counts, efficiency, index=0):
    if index >= len(counts):
        return 0
    
    current_base = counts[index]
    boosted = int(current_base * efficiency)
    bonus = 0
    
    # Case-based bonus: even-indexed zones get pollination boost
    if index % 2 == 0 and current_base > 0:
        bonus = int(current_base * 0.1)
    
    # Recursive accumulation
    return boosted + bonus + calculate_harvest(counts, efficiency, index + 1)

# Secondary distraction: string-based status
growth_status = "Optimal" if soil_ph > 6.0 else "Suboptimal"
status_code = growth_status.lower().replace("optimal", "OK")  # Unused

# Key execution point
final_yield = calculate_harvest(flowers, bee_efficiency)

# Add noise: unrelated bitwise shift
noise_factor = (humidity << 2) ^ 10  # Unused

# Output result as required
print(f"Result: {final_yield}")