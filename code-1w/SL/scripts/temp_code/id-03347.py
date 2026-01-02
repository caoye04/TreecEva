def analyze_growth_patterns(soil_data, temp_records):
    weighted_index = 0
    adjustment_factor = 0.85
    dummy_sum = 0  # Distractor: used in dead code

    for i, (moisture, ph) in enumerate(soil_data):
        if i % 2 == 0:
            weighted_index += moisture * (ph + adjustment_factor)
        else:
            temp_offset = temp_records[i] - 20
            weighted_index -= temp_offset * 0.1

    # Dead code path — irrelevant to final result
    if len(soil_data) > 100:
        for x in soil_data:
            dummy_sum += x[0] + x[1]

    return weighted_index


def calculate_harvest_efficiency(field_readings, thresholds):
    base_efficiency = 0
    peak_moment = None
    cumulative_stress = 0

    # List comprehension with filtering and transformation
    processed_readings = [
        (day, temp, humidity) for day, temp, humidity in field_readings
        if temp > thresholds['min_temp']
    ]

    # Lambda function for dynamic threshold check
    is_critical = lambda h, t: h < 30 or t > 35

    for idx, (day, temp, humidity) in enumerate(processed_readings):
        if is_critical(humidity, temp):
            base_efficiency -= 2
        else:
            base_efficiency += 1

        # Simulate stress accumulation using character count from day string
        day_chars = sum(1 for c in day if c.isalpha())
        cumulative_stress += day_chars % 3

        if temp >= max(t for _, t, _ in processed_readings) and not peak_moment:
            peak_moment = idx

    # Unused helper computation — distractor
    avg_stress = cumulative_stress / len(processed_readings) if processed_readings else 0

    # Key answer-determining logic
    final_yield = base_efficiency * (peak_moment if peak_moment else 1) + 17

    # Additional misleading calculation
    phantom_yield = 0
    for reading in field_readings:
        phantom_yield += len(reading[0]) * 2
    phantom_yield = phantom_yield // 4 if phantom_yield > 0 else 0

    return final_yield

# Input data
soil_conditions = [(22, 6.1), (18, 5.8), (25, 6.3), (20, 6.0), (15, 5.9)]
temperatures = [18, 22, 25, 20, 17]
growth_data = [
    ('Day1', 24, 45),
    ('Day2', 28, 38),
    ('Day3', 32, 25),
    ('Day4', 36, 20),
    ('Day5', 30, 40)
]
thresholds_config = {'min_temp': 23}

# Execution
index_analysis = analyze_growth_patterns(soil_conditions, temperatures)
final_yield = calculate_harvest_efficiency(growth_data, thresholds_config)
print(f"Target result: {final_yield}")