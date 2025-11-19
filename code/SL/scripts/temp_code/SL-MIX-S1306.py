from functools import reduce
import math
def process_signal(input_samples, coeffs):
    memory = [0.0] * len(coeffs)
    filtered_output = 0.0
    for sample in input_samples:
        memory = [sample] + memory[:-1]
        filtered_output = sum(c * m for c, m in zip(coeffs, memory))
    return filtered_output

def recursive_filter(stages, initial_value):
    if stages == 0:
        return initial_value
    else:
        prev = recursive_filter(stages - 1, initial_value)
        return math.sqrt(prev) + 0.5 * math.log(max(1e-10, prev))

input_sequence = [reduce(lambda x, y: x + y, range(1, n+1)) for n in range(1, 6)]
coefficients = [1.0, -0.5, 0.25]
base_output = process_signal(input_sequence, coefficients)
filtered_output = recursive_filter(3, base_output)
print(f"Result: {filtered_output}")