import math

# Irrelevant constants (distractors)
BASE_VOLTAGE = 230
MAX_PHASE_SHIFT = 15.7
REFERENCE_HUMIDITY = 45.0

# Simulated sensor data with red herring fields
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 23.9, 24.4]
humidity_readings = [42.1, 44.3, 46.0, 43.7, 45.2, 47.1, 44.0]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016]  # unused

# Decoy processing functions
def calculate_impedance(voltage, current):
    return voltage / current if current != 0 else 0  # dead path

# Unused transformation
calibrated_values = list(map(lambda x: round(x * 1.02, 2), temperature_readings))

# Fake anomaly detection (distractor logic)
anomalies = []
for i, temp in enumerate(temperature_readings):
    if abs(temp - sum(temperature_readings) / len(temperature_readings)) > 1.0:
        anomalies.append(i)

# Efficiency log derived from temperature fluctuations
efficiency_scores = []
for i in range(1, len(temperature_readings)):
    delta = temperature_readings[i] - temperature_readings[i-1]
    efficiency = math.cos(delta) * math.log(abs(delta) + 1)
    efficiency_scores.append(round(efficiency, 4))

# Redundant string-based status tracking (irrelevant)
status_flags = ['OK' if score >= 0 else 'LOW' for score in efficiency_scores]
summary_report = " | ".join(status_flags).upper().replace("OK", "NORMAL")

# Core computation disguised among noise
def process_thermal_metrics(metrics):
    # Nested filtering and transformation (3-level nesting)
    filtered = [m for m in metrics if m > -0.5]
    adjusted = [math.exp(val) for val in filtered]
    
    # Real logic hidden in lambda and aggregation
    aggregator = lambda x, y: x + y**2
    accumulated = adjusted[0]
    for i in range(1, len(adjusted)):
        accumulated = aggregator(accumulated, adjusted[i])
    
    # Final adjustment using bit manipulation (uncommon in thermal contexts → misdirection)
    base_result = int(accumulated * 100)
    masked = base_result ^ 0xFF  # XOR mask
    shifted = (masked >> 4) | (masked << 12)  # circular-like shift simulation
    final_shifted = shifted & 0xFFFF  # clamp to 16 bits
    
    # Correct result emerges here despite distractions
    return final_shifted / 100.0

# Unused recursive function (dead code path)
def forecast_temperature(data, depth=0):
    if depth >= 3:
        return data[0]
    return forecast_temperature(data[1:], depth + 1)

# Key execution point
thermal_capacity = process_thermal_metrics(efficiency_log=efficiency_scores)

# Output requirement
print(f"Result: {thermal_capacity}")