import math

# Simulated sensor array data (temperature, pressure, humidity)
data_stream = [
    (23.5, 101.3, 45.0), (24.1, 101.5, 47.2), (19.8, 100.9, 60.1),
    (22.7, 101.1, 50.3), (35.0, 99.8, 30.0), (21.0, 101.4, 55.6),
    (20.5, 100.7, 58.9), (25.3, 101.6, 44.7), (100.0, 102.0, 20.0), # outlier
    (22.0, 101.2, 48.8)
]

# Irrelevant auxiliary constants for distraction
calibration_factor = 0.987
reference_pressure = 101.325
baseline_offset = 17.5
noise_floor = 0.003
max_theoretical_yield = 98.6

# Decoy function - never called
def compute_entropy(values):
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return entropy

# Misleading intermediate processing chain
temp_readings = [t for t, p, h in data_stream]
pressure_readings = [p for t, p, h in data_stream]
humidity_readings = [h for t, p, h in data_stream]

avg_temp = sum(temp_readings) / len(temp_readings)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings)

# Compute moving average (unused but plausible)
def moving_average(lst, window=3):
    if len(lst) < window:
        return lst[:]
    return [sum(lst[i:i+window]) / window for i in range(len(lst)-window+1)]

# Dead code path - unreachable due to logic
emergency_shutdown_triggered = False
def trigger_safety_protocol():
    global emergency_shutdown_triggered
    emergency_shutdown_triggered = True
    print("System: Safety protocol engaged")

# Outlier detection with string-based flags (distractor)
flags = []
for temp, press, humid in data_stream:
    flag = ""
    if temp > 30:
        flag += "HIGH_TEMP_"
    if press < 100.0:
        flag += "LOW_PRESS_"
    if humid < 35.0:
        flag += "DRY_ATMO_"
    flags.append(flag.rstrip('_'))

# Real processing begins here — filter out readings where temperature > 30 or humidity < 30
filtered_data = []
for entry in data_stream:
    temp, press, humid = entry
    if temp <= 30 and humid >= 30:
        filtered_data.append(entry)

# Auxiliary diagnostic functions
def calculate_stability_index(temps):
    if len(temps) < 2:
        return 0.0
    variance = sum((t - sum(temps)/len(temps))**2 for t in temps) / len(temps)
    return round(math.sqrt(variance), 4)

def normalize_humidity(humid):
    # Sigmoid-like normalization
    return 100 * (1 / (1 + math.exp(-0.1 * (humid - 50))))

def assess_pressure_deviation(pressures):
    deviations = [abs(p - reference_pressure) for p in pressures]
    return sum(deviations)

# Core processing function
def process_readings(readings):
    temps = [t for t, p, h in readings]
    pressures = [p for t, p, h in readings]
    humids = [h for t, p, h in readings]
    
    # Step 1: Stability index from temperature fluctuations
    stability = calculate_stability_index(temps)
    
    # Step 2: Accumulate normalized humidity scores
    norm_humid_sum = sum(normalize_humidity(h) for h in humids)
    
    # Step 3: Pressure deviation penalty
    pressure_penalty = assess_pressure_deviation(pressures)
    
    # Step 4: Apply calibration and baseline adjustments (some are red herrings)
    raw_score = (norm_humid_sum * stability) / (1 + pressure_penalty * 0.01)
    calibrated_score = raw_score * calibration_factor  # relevant
    adjusted_score = calibrated_score + baseline_offset  # misleading — not used
    
    # Step 5: String-based integrity check (uses python string method)
    identifier = f"SYS-{len(readings)}-CHK"
    checksum_chars = [ord(c) % 10 for c in identifier if c.isdigit()]
    integrity_boost = sum(checksum_chars) if 'CHK' in identifier.upper() else 0
    
    # Step 6: Final diagnostic computation
    final_diagnostic = int(calibrated_score + integrity_boost)
    
    # Early return trap (not triggered)
    if final_diagnostic < 0:
        return 0
        trigger_safety_protocol()  # dead code
    
    return final_diagnostic

# Execute key statement
final_diagnostic = process_readings(filtered_data)

# Print result as required
print(f"Result: {final_diagnostic}")