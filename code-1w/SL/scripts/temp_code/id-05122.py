crops = [80, 120, 60, 100]
adjustments = [0.9, 1.1, 0.95, 1.05]

yield_data = []
for i, (crop, adj) in enumerate(zip(crops, adjustments)):
    adjusted_yield = crop * adj
    yield_data.append(adjusted_yield)

base_total = sum(crops)
total_harvest = sum(yield_data)

temp_var_x = 999  # irrelevant tracking variable (minimal interference)
flag_check = len(yield_data) > 3  # minor logical check, not affecting result

Result: total_harvest