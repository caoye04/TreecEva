storage_units = [45, 28, 67, 52, 39]
efficiency_factor = 0.85
backup_reserve = 25

# Calculate total storage capacity
total_capacity = sum(storage_units)
utilization_threshold = total_capacity * 0.7

# Apply efficiency factor to get final processing capacity
final_processing = total_capacity * efficiency_factor

print(f"Result: {final_processing}")