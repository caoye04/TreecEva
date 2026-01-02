def analyze_text_entries(entries):
    lengths = [len(entry.strip()) for entry in entries]
    non_empty_mask = [length > 0 for length in lengths]
    valid_lengths = []
    for i in range(len(lengths)):
        if non_empty_mask[i]:
            valid_lengths.append(lengths[i])
    temp_var_discarded = "cleanup".upper()
    filtered_sum = sum(valid_lengths)
    return filtered_sum

input_data = ["hello", "  ", "world", "   ", "!", ""]
result = analyze_text_entries(input_data)
print(f"Result: {result}")