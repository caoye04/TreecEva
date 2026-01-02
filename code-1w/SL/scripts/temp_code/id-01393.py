import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50, 53, 57]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1013, 1015]

# Irrelevant calibration coefficients for unused sensors (distractor)
ph_calibration = [1.02, 0.98, 1.01, 0.99, 1.03]
oxygen_sensitivity = [0.88, 0.91, 0.89, 0.92, 0.90]

# Decoy function that appears useful but is never called (dead code path)
def analyze_soil_composition(samples):
    return sum([s ** 0.5 for s in samples if s > 0]) / len(samples)

# Misleading intermediate transformation with plausible but unused result
rolling_avg = []
for i in range(len(temperature_readings) - 2):
    rolling_avg.append(sum(temperature_readings[i:i+3]) / 3)

# Distractor: complex bit manipulation on unrelated diagnostic flags (red herring)
diagnostic_flags = 0b101101
shifted_flags = (diagnostic_flags << 3) & 0b11111111
inverted_flags = shifted_flags ^ 0b11001100
flag_parity = bin(inverted_flags).count('1') % 2

# Real processing begins here — subtle because surrounded by noise
sensor_zipped = list(zip(temperature_readings, humidity_readings, pressure_readings))
baseline_temp = sum(temperature_readings) / len(temperature_readings)
breached_indices = []

# First real logic: find readings where temperature exceeds dynamic threshold
dynamic_threshold = baseline_temp + 1.5
for idx, (temp, hum, pres) in enumerate(sensor_zipped):
    if temp > dynamic_threshold:
        breached_indices.append(idx)

# Extract subset based on breach condition
filtered_data = [sensor_zipped[i] for i in breached_indices]

# Multiple thresholds for different response levels (modular arithmetic used)
threshold_levels = {
    'warning': 47,
    'critical': 55,
    'emergency': 60
}

# Function that looks generic but contains key logic
def process_readings(data, levels):
    if not data:
        return -1
    
    # Combinatorics: count how many readings exceed each humidity tier
    warning_count = 0
    critical_count = 0
    total_humidity = 0
    
    for temp, hum, pres in data:
        total_humidity += hum
        if hum >= levels['warning']:
            warning_count += 1
            if hum >= levels['critical']:
                critical_count += 1
    
    # Compute base score using modular arithmetic
    base_score = (total_humidity * 17) % 97
    
    # Apply combinatorial penalty: reduce score by number of overlapping high-humidity events
    overlap_penalty = warning_count * critical_count
    adjusted_score = base_score - overlap_penalty
    
    # Use string method to encode status (idiomatic python usage)
    status_str = "high_alert" if critical_count > 1 else "elevated"
    alert_code = sum([ord(c) for c in status_str]) % 13
    
    # Final computation combines arithmetic, logic, and hashing
    final_value = adjusted_score * 2 + alert_code
    
    # Additional distractor: unused recursive helper (decoy)
    def recursive_dust(count):
        if count <= 1:
            return count
        return recursive_dust(count-1) + recursive_dust(count-2)
    
    return final_value

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_levels)

# Print result as required
print(f"Target result: {final_diagnostic}")