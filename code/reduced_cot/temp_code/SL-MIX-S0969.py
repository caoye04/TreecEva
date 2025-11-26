data_entries = {'A': 15, 'B': 8, 'C': 22, 'D': 17, 'E': 5}

# Process data entries with some transformations
processed_data = {}
for key, value in data_entries.items():
    temp_val = value * 2
    # This intermediate calculation doesn't affect the final result
    dummy_calc = temp_val + 10
    if value > 10:
        processed_data[key] = temp_val - 3
    else:
        processed_data[key] = temp_val + 1

# Find maximum value key with string manipulation
key_strings = list(processed_data.keys())
max_key = max(key_strings, key=lambda k: processed_data[k])

# Some irrelevant string operations that don't impact the result
string_test = ''.join(reversed(max_key))
length_check = len(string_test)

# Final result extraction
final_result = processed_data[max_key]
print(f"Result: {final_result}")