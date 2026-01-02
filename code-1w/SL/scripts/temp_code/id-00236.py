is_peak_hour = True
load_level = 87
base_load = 45
efficiency_factor = 0.8

# Determine energy threshold based on current demand period
energy_threshold = load_level if is_peak_hour else base_load * efficiency_factor

print(f"Result: {energy_threshold}")