from itertools import accumulate

# Simulate renewable energy generation over 7 days (in MWh)
daily_generation = [120, 135, 98, 145, 112, 160, 130]

# Calculate cumulative energy generated
cumulative_energy = list(accumulate(daily_generation))

# Total stored energy after week, assuming 90% storage efficiency
storage_efficiency = 0.90
total_stored_energy = cumulative_energy[-1] * storage_efficiency

# Unrelated meteorological data (distractor)
avg_wind_speed = 14.2
solar_irradiance = 850  # W/m²

temperature_fluctuations = [-2, 1, 3, -1, 0, 2, -3]
adjusted_temps = [temp * 1.1 for temp in temperature_fluctuations]  # Minor processing

# Transmission loss: 5% of total stored energy
transmission_loss = total_stored_energy * 0.05

# Final deliverable energy capacity
energy_capacity = total_stored_energy - transmission_loss

print(f"Result: {energy_capacity}")