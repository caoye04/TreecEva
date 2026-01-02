def process_entry(entry):
    normalize = lambda x: (x - min(entry)) / (max(entry) - min(entry)) if max(entry) != min(entry) else [0] * len(entry)
    return [round(norm, 3) for norm in normalize(entry)]

raw_data = [15, 25, 35, 45]
processed_data = process_entry(raw_data)

threshold_filter = lambda seq, thres: [val for val in seq if val >= thres]
filtered_values = threshold_filter(processed_data, 0.3)

def calculate_total(values):
    base = sum(values)
    bonus = 5 if len(values) > 3 else 0
    return round(base + bonus, 3)

final_score = calculate_total(processed_data)
print(f"Result: {final_score}")