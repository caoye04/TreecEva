def calculate_harvest(yield_data, threshold):
    indexed_data = enumerate(yield_data)
    filtered_yields = [yield_amount for index, yield_amount in indexed_data if yield_amount > threshold and index % 2 == 0]
    total_harvest = sum(filtered_yields)
    temp_offset = 0.5  # Irrelevant variable (minimal interference)
    return total_harvest

# Simulated crop yield per plot (kg)
yields = [12, 8, 15, 7, 23, 6, 19, 4]
base_threshold = 10
total_harvest = calculate_harvest(yields, base_threshold)
print(f"Result: {total_harvest}")