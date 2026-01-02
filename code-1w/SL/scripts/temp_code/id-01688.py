def analyze_phase_stability(temps):
    stability_flags = []
    for i, t in enumerate(temps):
        if t < -50:
            stability_flags.append(0)
        elif t > 300:
            stability_flags.append(2)
        else:
            stability_flags.append(1)
    return stability_flags

# Irrelevant helper function (decoy)
def compute_noise_floor(samples):
    mean_val = sum(samples) / len(samples)
    variance = sum((x - mean_val) ** 2 for x in samples) / len(samples)
    return mean_val - variance ** 0.5

# Unused but plausible signal processing function
def filter_outliers(data, threshold=2):
    mean = sum(data) / len(data)
    std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std]

# Core logic disguised among distractions
def calculate_transfer_efficiency(states):
    efficiency_seed = 0
    for idx, (mode, temp, pressure) in enumerate(zip(states['modes'], states['temps'], states['pressures'])):
        if mode == 'active' and temp > 0:
            efficiency_seed += (temp % 7) * (pressure & 3)  # bitwise and modular arithmetic
        elif mode == 'standby':
            efficiency_seed -= (idx + 1) * (temp // 100)
    return efficiency_seed * 1.75

# Simulated sensor readings (red herring: includes noise-like values)
sensor_logs = [987, 1023, 456, 12, 789, 111, 999, 345]
noise_baseline = compute_noise_floor(sensor_logs)
filtered_logs = filter_outliers(sensor_logs, threshold=1.5)

# Real input data buried in setup
temperatures = [-20, 150, 350, -60, 250]
pressures = [12, 8, 15, 3, 10]
modes = ['active', 'active', 'standby', 'active', 'standby']

# Distractor: complex-looking but unused calculation using list comprehension and zip
correlation_matrix = [
    sum(a * b for a, b in zip([x**2 for x in temperatures], [y+1 for y in pressures])) % 100 
    for _ in range(3)
]

# Another decoy structure
data_checksum = sum(p << 1 for p in pressures) ^ 255

# Main state container
process_states = {
    'temps': temperatures,
    'pressures': pressures,
    'modes': modes,
    'timestamp': 1712345678,
    'version': '2.1a'
}

# Critical execution point
phase_stability = analyze_phase_stability(process_states['temps'])
thermal_gradient = 0  # initialization

# This line contains the key statement
thermal_gradient = calculate_transfer_efficiency(process_states)

# Output result as required
print(f"Result: {thermal_gradient}")