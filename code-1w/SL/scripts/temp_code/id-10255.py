def calculate_total(values):
    weight_func = lambda x: x * 1.5 if x > 10 else x * 0.8
    weighted = [weight_func(val) for val in values]
    return sum(weighted)

raw_data = [5, 12, 3, 15, 7]
adjustment_factor = 2
adjusted_values = [x + adjustment_factor for x in raw_data]
adjusted_values = [x for x in adjusted_values if x >= 10]

final_score = calculate_total(adjusted_values)
print(f"Target result: {final_score}")