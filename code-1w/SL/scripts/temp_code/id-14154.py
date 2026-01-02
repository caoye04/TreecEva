from itertools import compress

# Simulate sensor readings from renewable energy array
solar_readings = [120, 145, 130, 155, 160]
windspeed_flags = [True, False, True, True, False]

# Filter valid high-yield periods using sensor flags
efficient_periods = list(compress(solar_readings, windspeed_flags))

# Calculate total yield from efficient operation windows
total_yield = sum(efficient_periods)

# Apply system loss factor (15%)
adjusted_loss_factor = 0.15
energy_loss = total_yield * adjusted_loss_factor
final_yield = total_yield - energy_loss

# Threshold for minimum viable energy output
energy_threshold = 200

# Compute net usable energy beyond threshold
net_energy_output = final_yield - energy_threshold

print(f"Result: {net_energy_output}")