import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
humidity_readings = [45, 47, 50, 44, 46]
raw_signal = [0.88, 0.91, 0.85, 0.93, 0.87, 0.90, 0.89]

# Irrelevant auxiliary data (distractor)
echo_reflections = [0.12, 0.15, 0.10, 0.14]
baseline_noise = sum([abs(x - 0.13) for x in echo_reflections])
noise_floor = baseline_noise / len(echo_reflections) if echo_reflections else 0.0

# Signal preprocessing with red herring transformations
normalized = [x / max(raw_signal) for x in raw_signal]
filtered = [x for x in normalized if x > 0.85]
squared_energy = sum([x**2 for x in filtered])

# Dummy transformation chain (dead path)
transformed_chain = []
for val in filtered:
    temp_a = math.sin(val * math.pi / 2)
    temp_b = math.cos(val * math.pi / 4)
    transformed_chain.append((temp_a + temp_b) / 2)

# Unused but plausible diagnostic (misleading intermediate)
spectral_entropy = -sum([x * math.log(x + 1e-9) for x in transformed_chain])

# Real processing path begins here (obfuscated by prior noise)
aggregated_temp = sum(temperature_readings) / len(temperature_readings)
aggregated_hum = sum(humidity_readings) / len(humidity_readings)

# Composite index calculation with conditional expression
climate_factor = 1.0 if aggregated_hum > 46 else 0.85
adjustment = 1.1 if aggregated_temp < 24.0 else 0.95
composite_index = aggregated_temp * climate_factor * adjustment

# Data window selection based on dynamic condition
window_size = 3 if composite_index < 22.0 else 2
processed_data = filtered[-window_size:]  # Use last N samples

# Auxiliary decoy function (never called)
def compute_resonance(seq):
    return sum([math.tan(x + 1e-5) for x in seq if x > 0.5])

# Another red herring: unused statistical check
drift_detected = any(abs(temperature_readings[i] - temperature_readings[i+1]) > 0.8 
                   for i in range(len(temperature_readings)-1))
stability_score = 100 - (sum([abs(humidity_readings[i] - humidity_readings[i+1]) 
                                 for i in range(len(humidity_readings)-1)]) * 2)

# Core analysis function with embedded logic
def analyze_signal(seq):
    if not seq:
        return 0.0
    
    # Weighted average with exponential emphasis
    weighted_sum = sum(val * math.exp(i) for i, val in enumerate(seq))
    scaling_factor = sum(math.exp(i) for i in range(len(seq)))
    
    # Conditional override based on length (key logic)
    base_result = weighted_sum / scaling_factor if len(seq) > 1 else seq[0]
    
    # Secondary adjustment using climate context (cross-domain dependency)
    global composite_index
    modifier = 1.25 if composite_index >= 23.5 else 0.9
    
    # Final non-linear transformation
    return round(base_result * modifier * 1000, 3)

# Execution point of interest
final_diagnostic = analyze_signal(processed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")