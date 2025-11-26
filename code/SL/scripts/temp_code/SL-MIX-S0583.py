data_stream = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
filter_mask = [True, False, True, False, True, True]
processed_items = []
valid_entries = 0
temp_sum = 0

# Process data stream with filtering
for idx, (item, mask) in enumerate(zip(data_stream, filter_mask)):
    if mask:
        processed_items.append(item.upper())
        valid_entries += 1
        temp_sum += idx * 2  # Distractor computation
    else:
        temp_sum -= idx      # More distraction

# Additional processing with slicing
middle_section = processed_items[1:3]
section_length = len(middle_section)

# Offset calculation (semi-relevant)
base_offset = 3
offset_adjustment = section_length * 2
offset_correction = base_offset + offset_adjustment

# Final computation
result = valid_entries + offset_correction
print(f"Result: {result}")