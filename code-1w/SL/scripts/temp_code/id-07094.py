def analyze_rainfall(data):
    wet_days = [x for x in data if x > 5]
    total_rain = sum(wet_days)
    avg_rain = total_rain / len(wet_days) if wet_days else 0
    return avg_rain

soil_nutrients = {'nitrogen': 0.8, 'phosphorus': 0.4, 'potassium': 0.6}
decoy_result = 0

for i in range(3):
    temp_val = (i + 1) * 0.1
    decoy_result += temp_val ** 2

climate_data = [4.2, 6.1, 7.3, 3.0, 8.5, 9.1, 2.4, 5.6]
threshold = 6.0
exceedance_count = 0
for val in climate_data:
    if val > threshold:
        exceedance_count += 1

base_yield = len(climate_data) * 12.5
modifier = 0.0

if exceedance_count >= 3:
    modifier += 0.2
else:
    modifier -= 0.1

avg_moisture = analyze_rainfall(climate_data)

if avg_moisture > 6.0:
    modifier += 0.15
elif avg_moisture > 4.0:
    modifier += 0.1
else:
    modifier -= 0.05

# Simulate nutrient impact
nutrient_factor = (soil_nutrients['nitrogen'] + soil_nutrients['phosphorus'] + soil_nutrients['potassium']) / 3.0
if nutrient_factor > 0.6:
    modifier += 0.1

# Dummy list comprehension with no effect
useless_scaling = [round(base_yield * (1 + modifier)) // (i+1) for i in range(1, 4)]

final_yield = base_yield * (1 + modifier)
final_yield = int(final_yield)

# Irrelevant loop
buffer_sum = 0
for x in range(5):
    buffer_sum += x * 0.5

Result: final_yield