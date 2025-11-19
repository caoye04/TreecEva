def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

@call_counter
def process_frequency(freq):
    if freq <= 0:
        return 0
    return freq ** 2

frequencies = [4, 6, 8, 12, 15]
processed_values = []
valid_frequencies = {f for f in frequencies if f > 0}
invalid_count = len(frequencies) - len(valid_frequencies)

for freq in valid_frequencies:
    if freq % 2 == 0 or freq > 10:  # Short-circuit evaluation
        processed_values.append(process_frequency(freq))

mean_val = sum(processed_values) / len(processed_values) if processed_values else 0
variance = sum((x - mean_val) ** 2 for x in processed_values) / len(processed_values) if processed_values else 0

frequency_set = frozenset(valid_frequencies)
first_element = next(iter(frequency_set))
lcm_value = lcm(first_element, len(processed_values))

gcd_value = gcd(int(mean_val), int(variance)) if variance > 0 else 1
final_metric = (process_frequency.call_count * lcm_value) + (gcd_value if gcd_value > 1 else 0) - invalid_count

print(f'Result: {final_metric}')