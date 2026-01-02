def process_entry(entry):
    normalize = lambda x: (x - min(x, 10)) + 2
    if entry > 20:
        entry = normalize(entry) + 3
    else:
        entry = entry + (5 if entry % 2 == 0 else -2)
    return entry

raw_values = [8, 25, 14, 9]
processed_data = []

for val in raw_values:
    processed_val = process_entry(val)
    processed_data.append(processed_val)

# Irrelevant auxiliary variable (minor distraction)
checksum = sum([ord(c) for c in 'py'])

calculate_total = lambda data: sum(data) * 0.5

final_score = calculate_total(processed_data)
print(f"Result: {final_score}")