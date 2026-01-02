def analyze_patient(vital_signs):
    # Irrelevant preprocessing block (distractor)
    normalized = [v / max(vital_signs) for v in vital_signs]
    adjusted = [n * 1.07 for n in normalized]
    stats = {'mean': sum(adjusted) / len(adjusted), 'peak': max(adjusted)}

    # Red herring computation
    temp_flag = False
    if stats['mean'] > 0.8:
        temp_flag = True
        decay_rate = 0.92
        for i in range(len(adjusted)):
            adjusted[i] *= decay_rate
            decay_rate **= 0.5

    # Core logic disguised among distractions
    critical_count = 0
    for val in vital_signs:
        if val > 98 and val % 2 == 1:
            critical_count += 1

    return critical_count

# Decoy function that's never called
def compute_stress_index(data):
    stress = 0
    for d in data:
        stress += (d ** 0.5) * 3.14
        if stress > 100:
            stress -= 50
    return round(stress, 3)

# Another decoy: complex but unused transformation
echo_buffer = [0] * 16
for i in range(16):
    echo_buffer[i] = (i * 7 + 13) % 11

# Real processing begins here
health_data = [89, 92, 97, 99, 101, 103, 88, 95]

# Misleading intermediate calculation
drift_analysis = []
running_drift = 100.0
for reading in health_data:
    diff = abs(reading - running_drift)
    running_drift = (running_drift + reading) / 2
    drift_analysis.append(diff)

# Lambda-based threshold (required feature) - actually used
threshold_func = lambda x: x > 96 and (x % 5 == 0 or x % 7 == 0)

# Secondary distraction: tuple unpacking with irrelevant values
config_settings = ("mode_a", "debug_off", 0.05, 2048)
operation_mode, debug_flag, tolerance, _ = config_settings

# Unused recursive red herring
def predict_progression(value, days):
    if days == 0 or value > 110:
        return value
    return predict_progression(value * 1.03 - 2, days - 1)

# Data transformation chain with relevant and irrelevant parts
filtered_readings = list(filter(lambda x: x >= 90, health_data))

# Critical counting using modular arithmetic and conditions
anomaly_score = 0
for reading in filtered_readings:
    if reading % 3 == 2:
        anomaly_score += 1

# Core state variable updated through layered logic
status_flags = []
for val in health_data:
    if val < 90:
        status_flags.append(1)
    elif threshold_func(val):
        status_flags.append(3)
    else:
        status_flags.append(2)

# Final diagnostic depends on multiple prior results (integration point)
count_type_a = status_flags.count(1)
count_type_c = status_flags.count(3)

# Another distraction: bit manipulation with no effect
obfuscated_key = 0xABCD
for val in health_data:
    obfuscated_key ^= (val << 2) & 0xFFFF

# Actual answer derivation path
base_diagnostic = analyze_patient(health_data)
bonus_factor = count_type_c * 2
penalty = len(drift_analysis) // 4  # Uses misleading drift_analysis

# Final computation hidden among noise
final_diagnostic = base_diagnostic + bonus_factor - penalty

# This print must be present and match format
Target result: {final_diagnostic}