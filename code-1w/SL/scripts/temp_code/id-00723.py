def calculate_peak(loads):
    filtered = [load for load in loads if load > 0]
    smoothed = [filtered[i] + 0.5 * (filtered[i-1] + filtered[i+1]) 
               for i in range(1, len(filtered)-1)] if len(filtered) > 2 else filtered
    adjusted = [val * 0.9 for val in smoothed or filtered]
    return round(max(adjusted), 2) if adjusted else 0

# System load data in MW
base_load = 45.2
scheduled_maintenance = [-10, 0, 0, -5]
scheduled_loads = [38, 46, 52, 49, 58, -1, 0] + scheduled_maintenance

# Data correction using slicing
valid_inputs = scheduled_loads[:7]
extreme_outliers = valid_inputs[-1:]  # placeholder for monitoring

# Key computation
peak_capacity = calculate_peak(valid_inputs)

# Output result
print(f"Result: {peak_capacity}")