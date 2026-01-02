def calculate_performance(records):
    process = lambda x: (x[0] * 2) // (x[1] or 1)
    return sum(process(r) for r in records)

raw_inputs = [(12, 3), (15, 5), (8, 0), (20, 4)]
temp_buffer = [x for x in raw_inputs if x[0] > 10]
filtered_data = [item for item in temp_buffer if item[1] != 0]
efficiency_ratio = calculate_performance(filtered_data)
print(f"Result: {efficiency_ratio}")