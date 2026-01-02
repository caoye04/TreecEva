def calculate_emissions(fleet):
    emission_factors = {
        'sedan': 120,
        'suv': 180,
        'truck': 250,
        'van': 200
    }
    total = 0
    for vehicle_type, count in fleet.items():
        if vehicle_type in emission_factors:
            total += count * emission_factors[vehicle_type]
    return total

# Irrelevant auxiliary variable (minor distraction)
placeholder_value = "N/A"

vehicles = {
    'sedan': 3,
    'suv': 2,
    'truck': 1,
    'bike': 5  # Note: 'bike' not in emission_factors, should be ignored
}

maintenance_schedule = ["Q1", "Q2"]  # Distractor: unused variable

total_emissions = calculate_emissions(vehicles)
print(f"Result: {total_emissions}")