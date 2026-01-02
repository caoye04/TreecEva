import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [56, 61, 59, 64, 70, 52, 48, 75]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1018, 1020, 1003]

# Irrelevant transformations (distractors)
decoy_transform_1 = [t ** 0.5 for t in temperature_readings if t > 24]
decoy_transform_2 = ''.join([chr(int(h % 30) + 97) for h in humidity_readings])
decoy_stats = {"max_h": max(humidity_readings), "min_p": min(pressure_readings)}

# Misleading diagnostic flag (unused but plausible)
alarm_triggered = any(t > 25 for t in temperature_readings) and (sum(h > 60 for h in humidity_readings) > 2)

# Real processing begins: Normalize readings to z-scores (relevance)
def normalize_z(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [(x - mean) / std_dev for x in data]

z_temps = normalize_z(temperature_readings)
z_humidity = normalize_z(humidity_readings)
z_pressure = normalize_z(pressure_readings)

# Combined risk index using phase-shifted products (key logic)
combined_risk = []
for i in range(len(z_temps)):
    phase_shift = (i % 3) * 0.1
    risk_score = z_temps[i] * z_humidity[i] + z_pressure[i] * phase_shift
    combined_risk.append(risk_score)

# Dead code path (distractor): never called
def legacy_diagnostic(seq):
    return sum(s ** 2 for s in seq if s < -0.5)

# Bit manipulation decoy (irrelevant but looks technical)
bitmask = 0b110101
encoded_flags = [int(abs(r * 10)) & bitmask for r in combined_risk]
flag_density = sum(encoded_flags) / len(encoded_flags) if encoded_flags else 0

# Conditional expression with filtering (core relevance)
effective_risks = [r for r in combined_risk if abs(r) > 0.3]

# Use of itertools: generate overlapping triplets and compute moving product
triplet_windows = list(itertools.windowed(effective_risks, n=3))
moving_products = [abs(a * b * c) for a, b, c in triplet_windows if all(x != 0 for x in [a, b, c])]

# Auxiliary distraction: string-based encoding of pressure states
pressure_states = ''.join(['H' if p > 1014 else 'L' for p in pressure_readings])
state_transition_count = pressure_states.count('HL') + pressure_states.count('LH')

# Final aggregation with threshold logic (target execution point)
if moving_products:
    avg_product = sum(moving_products) / len(moving_products)
    peak_risk = max(combined_risk)
    base_offset = -0.15
    # Critical statement
    final_diagnostic = avg_product * peak_risk + base_offset
else:
    final_diagnostic = -1.0

# Unused fallback logic (dead path)
recovery_mode = False
def reset_calibration():
    global recovery_mode
    recovery_mode = True

# Output result
print(f"Result: {final_diagnostic}")