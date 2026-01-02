def process_efficiency(elements, filter_func):
    unique_elements = set(elements)
    filtered_set = {x for x in unique_elements if filter_func(x)}
    base_score = sum(filtered_set)
    adjustment = len(unique_elements) - len(filtered_set)
    return base_score - adjustment * 2

# Sensor readings with duplicates
readings = [10, 15, 15, 20, 25, 30, 30, 10, 40]

# Threshold logic for acceptable efficiency range
threshold_func = lambda x: x >= 15 and x <= 30

# Compute final filtration score
filtration_score = process_efficiency(readings, threshold_func)

print(f"Result: {filtration_score}")