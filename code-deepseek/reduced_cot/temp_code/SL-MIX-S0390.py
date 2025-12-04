from collections import Counter

data_samples = [12, 8, 12, 15, 8, 20, 15, 12, 18]
frequency_analysis = Counter(data_samples)
unique_elements = {element for element in data_samples if frequency_analysis[element] == 1}
unique_count = len(unique_elements)
print(f"Result: {unique_count}")