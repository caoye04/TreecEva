from itertools import compress, count

def calculate_thermal_response(energy_levels, threshold):
    # Initialize tracking variables
    cumulative_load = 0
    fluctuation_count = 0
    peak_moment = None
    decay_factor = 0.85

    # Misleading pre-processing: normalize with no real impact
    normalized_levels = [e * 0.99 for e in energy_levels]
    filtered_indices = [i for i, e in enumerate(normalized_levels) if e > threshold * 0.75]

    # Real logic begins: track significant energy surges
    surge_points = []
    for i, energy in enumerate(energy_levels):
        if energy > threshold:
            surge_points.append(i)
            cumulative_load += energy * 0.33
            fluctuation_count += 1

    # Simulate thermal inertia using decay on prior loads (distractor-heavy)
    inertial_buffer = 0
    for tick in range(len(energy_levels)):
        inertial_buffer = inertial_buffer * decay_factor + energy_levels[tick] * 0.1

    # Use zip to pair indices and original values for filtering valid responses
    valid_responses = []
    for idx, val in zip(count(), energy_levels):
        if val > threshold * 1.1:
            valid_responses.append(val * 0.45)

    # Core calculation: thermal capacity based on weighted valid response
    base_integral = sum(valid_responses)
    adjustment = len(surge_points) * 0.62
    thermal_capacity = int(base_integral - adjustment)  # Final answer contribution

    # Dead code path: never executed due to fixed condition
    if False:
        fallback = [x ** 0.5 for x in energy_levels]
        thermal_capacity = sum(fallback)

    return thermal_capacity

# Main execution
energy_sequence = [12, 15, 8, 23, 19, 4, 31, 27, 11, 20, 16, 9]
threshold_level = 20

monitor_log = []
for t in range(len(energy_sequence)):
    if energy_sequence[t] > threshold_level:
        monitor_log.append(f"Alert at t={t}")

# Key statement
thermal_capacity = calculate_thermal_response(energy_sequence, threshold_level)

# Print result as required
print(f"Result: {thermal_capacity}")