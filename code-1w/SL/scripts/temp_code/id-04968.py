def calculate_crop_yield():
    base_yields = [23, 45, 12, 67, 34]
    growth_factors = [1.1, 0.9, 1.2, 0.8, 1.0]
    adjustments = []
    
    for i, (yield_val, factor) in enumerate(zip(base_yields, growth_factors)):
        adjusted = yield_val * factor
        if adjusted < 30:
            adjustments.append(adjusted + 5)
        else:
            adjustments.append(adjusted)
    
    temp_sum = 0
    for val in adjustments:
        temp_sum += val
    
    total_harvest = sum(adjusted_yields)
    return total_harvest

# Note: there's a typo above — `adjusted_yields` is undefined; correct version follows

base_yields = [23, 45, 12, 67, 34]
growth_factors = [1.1, 0.9, 1.2, 0.8, 1.0]
adjusted_yields = []

for i, (yield_val, factor) in enumerate(zip(base_yields, growth_factors)):
    adjusted = yield_val * factor
    if adjusted < 30:
        adjusted_yields.append(adjusted + 5)
    else:
        adjusted_yields.append(adjusted)

ignored_value = max(adjusted_yields) - min(adjusted_yields)
total_harvest = sum(adjusted_yields)
print(f"Result: {total_harvest}")