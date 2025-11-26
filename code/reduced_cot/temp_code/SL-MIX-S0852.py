from collections import Counter

data_stream = [2, 5, 3, 7, 2, 8, 3, 5, 2, 1]
frequency_map = Counter(data_stream)

# Primary analysis
primary_sum = 0
for value, count in frequency_map.items():
    if count > 1:
        primary_sum += value * count

# Secondary analysis (distraction)
secondary_total = 0
temp_list = []
for num in data_stream:
    if num % 2 == 0:
        temp_list.append(num * 2)
    else:
        temp_list.append(num + 1)

# This loop doesn't affect the final answer
for item in temp_list:
    if item > 10:
        secondary_total += 3
    else:
        secondary_total += 1

# Calculate intermediate value (irrelevant)
intermediate_val = sum(data_stream) // len(data_stream)

# Final computation
final_metric = primary_sum - secondary_total
print(f"Result: {final_metric}")