def calculate_yield(data):
    total = 0
    for i, (crop, yield_per_acre) in enumerate(zip(data['crops'], data['yields'])):
        area = data['areas'][i]
        bonus = 1.0
        if 'high_yield' in data['tags'] and yield_per_acre > 80:
            bonus = 1.2
        total += area * yield_per_acre * bonus
    return int(total)

# Irrelevant utility function (minimal distraction)
def format_crop_name(name):
    return name.upper().replace('_', ' ')

# Main data structure
farm_data = {
    'crops': ['wheat', 'corn', 'soybeans'],
    'areas': [50, 30, 40],
    'yields': [70, 95, 65],
    'tags': ['fertile_soil', 'high_yield']
}

# Secondary variable with no impact (low interference)
crop_names_formatted = [format_crop_name(name) for name in farm_data['crops']]

# Critical computation
total_harvest = calculate_yield(farm_data)
print(f"Result: {total_harvest}")