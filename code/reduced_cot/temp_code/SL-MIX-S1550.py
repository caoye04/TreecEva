from functools import reduce
from collections import defaultdict

def transform_signal(coefficients, depth=0):
    if depth >= 3:
        return sum(coefficients) % 17
    next_coeffs = []
    for i in range(len(coefficients)):
        val = coefficients[i] * (i + 1)
        if val % 2 == 0:
            next_coeffs.append(val // 2)
        else:
            next_coeffs.append(val * 3 + 1)
    return transform_signal(next_coeffs, depth + 1)

initial_signal = [2, 4, 1, 5]
mapped_signal = list(map(lambda x: x**2 if x%2==0 else x*2, initial_signal))
filtered_signal = list(filter(lambda x: x > 5, mapped_signal))
processed_data = defaultdict(int)
for idx, val in enumerate(filtered_signal):
    processed_data[idx] = val
expanded_data = {k: v+1 for k, v in processed_data.items()}
merged_data = {**processed_data, **expanded_data}
sorted_values = sorted(merged_data.values())
final_coefficient = transform_signal(sorted_values)
print(f"Result: {final_coefficient}")