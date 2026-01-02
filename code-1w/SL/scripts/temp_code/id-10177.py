def analyze_crop_data(data_string):
    # Parse sensor data from IoT farm device
    segments = data_string.split('|')
    temperature = float(segments[0].split(':')[1])
    humidity = float(segments[1].split(':')[1])
    soil_nutrients = [int(x) for x in segments[2].split(':')[1].split(',')]

    # Distractor: irrelevant air pressure parsing
    air_pressure_str = segments[3].split(':')[1]
    air_pressure_mb = int(air_pressure_str.replace('mb', ''))

    # Misleading intermediate calculation (not used later)
    nutrient_balance_score = sum([n * 0.3 for n in soil_nutrients if n > 5])

    # Actual relevant transformation
    avg_nutrient = sum(soil_nutrients) / len(soil_nutrients)
    stability_factor = 1.0 if temperature < 30 and humidity > 40 else 0.7

    return avg_nutrient, stability_factor, air_pressure_mb


def calculate_degradation_rate(hours, exposure_index):
    # Complex but partially irrelevant degradation model
    base_loss = 0.0
    for h in range(1, hours + 1):
        if h % 5 == 0:
            base_loss += 0.012 * exposure_index
    return round(base_loss, 4)

# Main execution
sensor_input = "temp:28.5|humidity:45|nutrients:8,6,12,4,9|pressure:1013mb"
avg_nutrient, stability, pressure = analyze_crop_data(sensor_input)

# Simulate field conditions
area = 14.2  # hectares
treatment_days = 6
exposure = 2
moisture_level = 68  # percent

# Red herring: unused productivity index
baseline_productivity = area * 320.5
adjustment_ratio = (moisture_level / 100) * 0.9 + 0.1
productivity_index = baseline_productivity * adjustment_ratio

# Intermediate calculations with some dead computations
max_capacity = area * 400
projected_wilt_rate = calculate_degradation_rate(treatment_days, exposure)
yield_reduction = projected_wilt_rate * 100

# Core logic hidden among distractions
base_yield_per_hectare = 380
adjusted_yield = base_yield_per_hectare * (avg_nutrient / 8.0)
if stability > 0.8:
    adjusted_yield *= 1.15

if moisture_level > 60:
    adjusted_yield *= 1.08
elif moisture_level < 40:
    adjusted_yield *= 0.85
else:
    adjusted_yield *= 1.0

# Final integration step
final_yield = int(adjusted_yield * area)  # Key result

# Print final result as required
print(f"Result: {final_yield}")