data_entries = [42, 18, 75, 33, 91, 27, 56, 84, 12, 65]
threshold = 50

# Calculate how many entries meet the threshold requirement
valid_entries = [x for x in data_entries if x > threshold]
total_valid = len(valid_entries)

# Some unrelated processing for intervention
backup_copy = data_entries[:]
temp_sum = sum(backup_copy)

# The key calculation
final_ratio = total_valid / len(data_entries)

print(f"Result: {final_ratio}")