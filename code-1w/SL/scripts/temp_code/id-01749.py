from collections import Counter

def calculate_final_score(data, limit):
    filtered = [temp for temp in data if temp > limit]
    counts = Counter(filtered)
    adjusted = [k * v for k, v in counts.items()]
    aggregate = sum(adjusted) // len(adjusted) if adjusted else 0
    return aggregate + len(filtered)

temperature_data = [23, 25, 23, 27, 29, 25, 30, 28]
threshold = 26
auxiliary_list = [x.lower() for x in ['A', 'B', 'C']]  # irrelevant operation (minimal distraction)
result = calculate_final_score(temperature_data, threshold)
print(f"Result: {result}")