from collections import Counter

data_sequence = [8, 15, 22, 29, 36, 43]
processed_data = []
for index, value in enumerate(data_sequence):
    processed_value = value + index
    processed_data.append(processed_value)

enumerate_data = processed_data[1:4]
total_processed = sum(enumerate_data) + len(enumerate_data)
print(f"Target result: {total_processed}")