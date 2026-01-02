def calculate_total(data):
    weighted_sum = sum(x * (i + 1) for i, x in enumerate(data))
    adjustment = lambda w, n: w // n if n > 0 else 0
    return adjustment(weighted_sum, len(data))

raw_values = [12, -4, 8, 3, -6]
processed_data = [x for x in raw_values if x > 0]

def apply_offset(items, offset=2):
    return [y + offset for y in items]

processed_data = apply_offset(processed_data)
final_score = calculate_total(processed_data)
print(f"Result: {final_score}")