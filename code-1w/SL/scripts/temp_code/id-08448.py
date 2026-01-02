from itertools import cycle, islice

# Simulated industrial filtration process parameters
temperature_readings = [22.5, 23.0, 22.8, 23.2, 24.1, 25.0, 24.8, 23.9]
pressure_cycles = [1.01, 1.03, 1.05, 1.04, 1.02, 1.06, 1.08, 1.07]
impurity_levels = [0.15, 0.12, 0.18, 0.10, 0.22, 0.25, 0.19, 0.14]

# Irrelevant baseline metrics (distractors)
baseline_metrics = {
    'vibration': [0.01, 0.03, 0.02, 0.05, 0.04, 0.06, 0.08, 0.07],
    'humidity': [45.2, 46.1, 47.0, 46.8, 48.3, 49.0, 48.7, 47.5],
    'flow_rate': [12.1, 12.3, 12.0, 12.5, 12.4, 12.6, 12.8, 12.7]
}

# Misleading intermediate calculations (dead paths)
total_vibration = sum(baseline_metrics['vibration'])
avg_humidity = sum(baseline_metrics['humidity']) / len(baseline_metrics['humidity'])
peak_flow = max(baseline_metrics['flow_rate'])

# Core process variables
base_temperature = temperature_readings[2]  # Index 2: 22.8°C
reference_pressure = pressure_cycles[-1]  # Last cycle: 1.07 atm
current_impurity = impurity_levels[5]  # Index 5: 0.25

# Distractor function: unused but plausible
def calculate_stress_factor(vib_seq, hum_seq):
    return sum(v ** 2 for v in vib_seq) * 0.01 + sum(hum_seq) * 0.001

# Another red herring: complex but irrelevant transformation
extended_cycle = list(islice(cycle([1.01, 1.03, 1.05]), 0, 20))
oscillation_pattern = [round((x - 1.03) ** 2, 4) for x in extended_cycle]
synchronized_phase = sum(oscillation_pattern[:12]) % 3.14159

# Linear search for threshold breach (relevant path)
def find_first_breach(data, threshold):
    for i, val in enumerate(data):
        if val > threshold:
            return i
    return -1

impurity_breach_index = find_first_breach(impurity_levels, 0.20)  # Returns 4

# Bit manipulation decoy (irrelevant)
status_flag = 0b10101010
masked_flag = status_flag & 0b11110000
shifted_flag = masked_flag >> 4

# Control flow with distractors
if base_temperature > 22.5:
    temp_offset = 0.5
    dummy_calc = (reference_pressure + 2j) ** 2  # Complex number distraction
else:
    temp_offset = 0.0

# Unused tuple unpacking (misdirection)
_, _, *remaining_temps = temperature_readings

# Actual relevant logic chain starts here
raw_stability_score = reference_pressure * (25.0 - base_temperature)  # 1.07 * 2.2 = 2.354

if current_impurity > 0.20:
    degradation_rate = 0.15
else:
    degradation_rate = 0.05

process_efficiency = raw_stability_score * (1 - degradation_rate)  # 2.354 * 0.85 = 2.0009

# Character counting red herring
log_entry = "FILT-2023-XJ"
letter_count = sum(1 for c in log_entry if c.isalpha())  # 8 letters

# Another dead end
if letter_count % 2 == 0:
    adjustment_curve = [x * 0.1 for x in range(8)]
    phase_shift = sum(adjustment_curve)  # 2.8

# Key data transformation
sorted_impurities = sorted(impurity_levels, reverse=True)
dominant_impurity = sorted_impurities[0]  # 0.25

# Main calculation components
base_yield = 42.0  # Base yield in kg/hour

# Adjustment based on breach index and dominant impurity
if impurity_breach_index >= 0:
    adjustment_factor = (dominant_impurity * 100) - (impurity_breach_index * 3)
else:
    adjustment_factor = 0

# Critical assignment statement
filtration_yield = process_efficiency * (base_yield + adjustment_factor)

# Print result as required
print(f"Result: {filtration_yield}")