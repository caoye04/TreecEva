def calculate_yield(data):
    total = 0
    for i, (crop, yield_per_unit) in enumerate(zip(data['crops'], data['yields'])):
        adjustment = data['adjustments'].get(crop, 1.0)
        contribution = yield_per_unit * data['areas'][i] * adjustment
        if contribution > 0:
            total += round(contribution)
    return total

# Irrelevant auxiliary variable (minimal distraction)
fake_yield_list = [0, 0, 0]

farm_data = {
    'crops': ['wheat', 'corn', 'barley'],
    'yields': [2.5, 3.0, 2.0],
    'areas': [40, 35, 25],
    'adjustments': {'wheat': 1.1, 'corn': 0.9}
}

total_harvest = calculate_yield(farm_data)
print(f"Result: {total_harvest}")