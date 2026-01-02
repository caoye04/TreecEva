import math

# Simulated environmental sensor readings (temperature, pressure, humidity)
sensor_readings = [
    (23.5, 1013.25, 45),
    (24.1, 1012.80, 47),
    (22.9, 1013.50, 44),
    (25.3, 1011.90, 50),
    (26.0, 1011.45, 52)
]

def extract_metrics(data):
    temperatures = [d[0] for d in data]
    pressures = [d[1] for d in data]
    humidities = [d[2] for d in data]
    return temperatures, pressures, humidities

# Irrelevant transformation: converts to binary string representations (dead path)
def to_binary_sequence(num_list):
    return [''.join(format(int(x * 10), '08b')) for x in num_list]

# Unused function - decoy for signal processing
def apply_fourier_transform(signal):
    transformed = []
    for i in range(len(signal)):
        real = sum(signal[j] * math.cos(2 * math.pi * i * j / len(signal)) for j in range(len(signal)))
        imag = sum(-signal[j] * math.sin(2 * math.pi * i * j / len(signal)) for j in range(len(signal)))
        transformed.append(complex(real, imag))
    return transformed

# Auxiliary calculation: computes entropy of a normalized distribution
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Distractor list: derived but unused metrics
temps, press, humids = extract_metrics(sensor_readings)
binary_temps = to_binary_sequence(temps)  # Dead end
entropy_humidity = compute_entropy(humids)  # Misleading intermediate result

# Calibration map for different operational modes (only one key used)
calibration_map = {
    'eco': 0.88,
    'std': 1.00,
    'boost': 1.15,
    'turbo': 1.25  # Never accessed
}

calibration_factor = calibration_map['std']

# Real processing begins here
def preprocess_readings(raw_data, scale):
    processed = []
    for temp, press, humid in raw_data:
        # Physical model: corrected flow based on ideal gas approximation
        corrected_pressure = press * (1 + 0.00012 * (temp - 20))
        humidity_ratio = 0.622 * (humid * 0.01 * 3.169) / (corrected_pressure - humid * 0.01 * 3.169)
        density = corrected_pressure / (287.05 * (temp + 273.15))  # kg/m^3
        flow_base = density * 0.5  # base velocity assumption
        adjusted_flow = flow_base * (1 + humidity_ratio) * scale
        processed.append(adjusted_flow)
    return processed

# Secondary filter: removes outliers using IQR method (used only once)
def remove_outliers_iqr(values):
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals) // 4]
    q3 = sorted_vals[3 * len(sorted_vals) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

# Main optimization logic
def calculate_optimal_flow(data, factor):
    flows = preprocess_readings(data, factor)
    
    # Apply outlier removal
    valid_flows = remove_outliers_iqr(flows)
    
    # Compute statistical moments
    mean_flow = sum(valid_flows) / len(valid_flows)
    variance = sum((x - mean_flow) ** 2 for x in valid_flows) / len(valid_flows)
    std_dev = math.sqrt(variance)
    
    # Weighted combination using lambda-based adjustment
    adjuster = lambda x: math.tanh(x / mean_flow)  # Smooth nonlinearity
    adjustment = adjuster(std_dev)
    
    # Incorporate historical baseline (simulated)
    historical_baseline = 0.892
    hybrid_score = 0.6 * mean_flow + 0.4 * historical_baseline * adjustment
n    
    # Final optimization step: apply efficiency envelope
    efficiency_multiplier = 1.05 + 0.02 * math.sin(len(valid_flows))
    final_optimized = hybrid_score * efficiency_multiplier
    
    # Red herring: unused peak detection
    peak_flow = max(flows)
    normalized_peak = peak_flow / mean_flow if mean_flow != 0 else 0
    
    # Another decoy: hypothetical future projection
    projected_next = sum(math.cos(i) * f for i, f in enumerate(flows))
    
    return final_optimized

# Execute main logic
optimized_flow_rate = calculate_optimal_flow(sensor_readings, calibration_factor)

# Print result as required
print(f"Result: {optimized_flow_rate}")