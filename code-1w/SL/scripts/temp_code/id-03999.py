def process_entry(entry):
    normalize = lambda x: (x - min(entry)) / (max(entry) - min(entry)) if max(entry) != min(entry) else [0.5] * len(entry)
    return [round(val, 3) for val in normalize(entry)]

raw_data = [15, 25, 35, 45]
threshold = 20
filtered_data = [x for x in raw_data if x >= threshold]

processed_data = process_entry(filtered_data)

compute_weight = lambda vals: sum(val * 0.1 for val in vals)

def calculate_total(data):
    base = sum(data)
    bonus = compute_weight(data)
    penalty = 0.05 if len(data) > 3 else 0
    return round(base + bonus - penalty, 3)

final_score = calculate_total(processed_data)
print(f"Result: {final_score}")