def calculate_total(data):
    base_score = sum(map(lambda x: x**2, data))
    bonus = len([x for x in data if x > 0])
    return base_score + bonus * 2

raw_input = [1, -3, 4, -2, 5]
filtered_data = [x for x in raw_input if x % 2 != 0]
processed_data = [x + 1 for x in filtered_data]
initial_sum = sum(raw_input)
dummy_var = [0] * len(raw_input)
count_positive = len([x for x in raw_input if x > 0])
final_score = calculate_total(processed_data)
print(f"Target result: {final_score}")