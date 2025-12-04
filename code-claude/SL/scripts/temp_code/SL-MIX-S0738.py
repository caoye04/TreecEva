import itertools

# Smart home power optimization problem
def calculate_efficiency(voltage, current):
    # Calculate power efficiency rating based on voltage and current
    base_power = voltage * current
    loss_factor = 0.05 * (current ** 2)  # Power loss increases with square of current
    return base_power - loss_factor

# Device data: (name, voltage, current, priority)
devices = [
    ("Refrigerator", 110, 1.5, 10),
    ("Television", 120, 0.8, 5),
    ("Air Conditioner", 220, 3.2, 8),
    ("Laptop Charger", 19, 3.4, 4),
    ("LED Light", 12, 0.5, 3),
    ("Water Heater", 240, 4.5, 7)
]

# Calculate power for each device
power_values = list(map(lambda d: calculate_efficiency(d[1], d[2]), devices))

# Sort devices by priority (distraction - not used in final answer)
sorted_by_priority = sorted(devices, key=lambda x: x[3], reverse=True)

# Filter devices that exceed minimum power threshold
min_power = 100
valid_devices = [(devices[i][0], power_values[i]) for i in range(len(devices)) if power_values[i] >= min_power]

# Add some low-power devices for testing (distraction)
test_devices = [("Smart Sensor", 5.8), ("LED Strip", 7.2)]
all_test_combinations = list(itertools.combinations(test_devices, 2))

# Find optimal device configuration
max_efficiency = 0
for i, device in enumerate(valid_devices):
    # Calculate theoretical maximum (distraction)
    theoretical_max = power_values[i] * 1.2
    
    # Check if this device is more efficient
    if device[1] > max_efficiency:
        max_efficiency = device[1]

# Sort filtered devices by power
filtered_devices = sorted(valid_devices, key=lambda x: x[1])

# Calculate average power (distraction)
avg_power = sum(d[1] for d in filtered_devices) / len(filtered_devices) if filtered_devices else 0

# Get the device with optimal power
optimal_power = filtered_devices[-1][1]

# Display result
print(f"Result: {optimal_power}")