def analyze_pattern(sequence, limit):
    magnitude = sum(x ** 2 for x in sequence if x > 0)
    normalized = magnitude / len(sequence)
    adjusted_sequence = [x + 1 for x in sequence]
    return normalized

# Sensor flow data simulation
turbulence_factors = [3, -1, 4, 1, -5, 9, 2, 6]
flow_data = turbulence_factors[::2]  # Every other reading represents active phase
baseline = sum(enumerate(flow_data)) // len(flow_data)

# Red herring: energy dispersion model (not used in final result)
dispersion_model = []
for i in range(len(flow_data)):
    dispersion = 0
    for j in range(i + 1):
        dispersion += abs(flow_data[j] - baseline)
    dispersion_model.append(dispersion)

threshold = 3
def calculate_equilibrium(data, thresh):
    valid_count = 0
    cumulative = 0
    for val in data:
        if abs(val) > thresh:
            valid_count += 1
            cumulative += val * val
    if valid_count == 0:
        return 0
    average_sq = cumulative / valid_count
    return int(average_sq ** 0.5)

# Secondary unused analysis path
aggregated_metrics = []
for idx, val in enumerate(flow_data):
    if val % 2 == 0:
        score = idx * val
        aggregated_metrics.append(score)  # Dead code branch

# Key computation path
equilibrium_score = calculate_equilibrium(flow_data, threshold)

# Noise variables
interim_result = analyze_pattern(turbulence_factors, 10)
scaling_factor = baseline * 0.75
final_output = equilibrium_score * scaling_factor

print(f"Result: {equilibrium_score}")