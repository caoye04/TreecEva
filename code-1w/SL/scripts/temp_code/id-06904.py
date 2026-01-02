import itertools

# Simulated sensor array data for fluid dynamics optimization
turbulence_readings = [0.45, 0.72, 0.33, 0.81, 0.54, 0.63]
pressure_gradients = [1.1, -0.9, 1.3, 0.7, -1.2, 0.5]
thermal_variations = [298.15, 301.2, 296.4, 303.0, 295.8]

# Irrelevant environmental telemetry (distractor)
ambient_humidity = [45, 48, 52, 49, 51]  # Not used in calculation
wind_speed_kph = [12.3, 14.1, 11.8, 13.7, 15.0]  # Dead code path input

# Core system parameters
base_flow_rate = 18.5
modulation_factor = 0.67
threshold_limit = 0.75

# Historical benchmark values (decoy data)
historical_maxima = {
    'flow': 98.3,
    'pressure': 2.1,
    'turbulence_index': 0.88
}

# Data transformation pipeline
mapped_turbulence = list(map(lambda x: round(x ** 2 * 10, 3), turbulence_readings))
filtered_gradients = [x for x in pressure_gradients if abs(x) > threshold_limit]

# Complex conditional processing with red herring logic
if len(mapped_turbulence) > 5:
    adjusted_base = base_flow_rate * 1.15
else:
    adjusted_base = base_flow_rate * 0.92  # This branch actually executes

# Dummy function to mislead about data usage
def analyze_wind_patterns(data):
    return sum(x ** 2 for x in data) / len(data) if data else 0

# Unused but plausible-looking analysis (dead code)
average_wind_energy = analyze_wind_patterns(wind_speed_kph)

# Critical intermediate computation with distraction
aggregated_thermal = sum(thermal_variations) / len(thermal_variations) - 273.15
scaling_coefficient = modulation_factor if aggregated_thermal > 25 else 0.44

# Construct composite signal using itertools (relevant)
synchronized_signals = list(itertools.product(
    mapped_turbulence[::2],
    filtered_gradients
))

# Generate fluctuation matrix (key component)
fluctuations = [
    (a * b * scaling_coefficient) for a, b in synchronized_signals
    if a > 2.0 and b > 0
]

# Initialize target variable
optimized_flow_rate = adjusted_base

# Secondary adjustment using conditional expression (core logic)
optimized_flow_rate = (
    optimized_flow_rate * 1.08 if len(fluctuations) > 4 
    else optimized_flow_rate * 0.97
)

# Redundant status logging (distractor output)
status_flags = {i: 'STABLE' if val > 0 else 'FLUCTUATING' for i, val in enumerate(filtered_gradients)}

# Final processing function
def process_network(noise_pattern, rate):
    # Local transformation
    net_effect = sum(abs(x) for x in noise_pattern) / len(noise_pattern) if noise_pattern else 0
    # Apply dampening
    final_rate = rate * (1 + 0.01 * min(net_effect, 2.5))
    return final_rate

# Execute critical statement
final_output = process_network(fluctuations, optimized_flow_rate)

# Print result as required
print(f"Target result: {optimized_flow_rate}")