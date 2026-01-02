from itertools import compress

crop_ids = [101, 102, 103, 104, 105]
yield_per_acre = [87, 94, 65, 103, 76]
soil_quality = [True, True, False, True, False]

# Calculate average yield for high-quality soil fields
selected_fields = list(compress(yield_per_acre, soil_quality))
avg_yield = sum(selected_fields) / len(selected_fields) if selected_fields else 0

# Filter yields above average from all crops
filtered_yields = [y for y in yield_per_acre if y > avg_yield]

# Final computation target
total_harvest = sum(filtered_yields)
print(f"Result: {total_harvest}")