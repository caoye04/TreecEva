def calculate_total(data):
    base_fn = lambda x: x ** 2 - 3 * x
    bonus_fn = lambda x: x + 10 if x > 50 else x

    total = 0
    for key, value in data.items():
        if 'temp' in key:
            transformed = base_fn(value)
            total += bonus_fn(transformed)
    return total

# Irrelevant auxiliary variable (minimal distraction)
initial_offset = 7

raw_values = {'temp_a': 8, 'temp_b': 12, 'temp_c': 6, 'humidity': 40}
processed_data = {k: v + 2 for k, v in raw_values.items() if k.startswith('temp')}

final_score = calculate_total(processed_data)
print(f"Result: {final_score}")