import math

# Simulated sensor data from a thermal regulation system
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 25.9, 24.7, 26.2]
humidity_readings = [45, 47, 50, 55, 60, 58, 53, 51]

# Irrelevant auxiliary data (distractor)
sound_levels = [30, 32, 35, 40, 45, 42, 38, 36]
luminosity = [200, 210, 220, 240, 260, 250, 230, 215]

# Preprocessing: normalize temperature readings to baseline
baseline_temp = sum(temperature_readings) / len(temperature_readings)
normalized_temps = [round(t - baseline_temp, 3) for t in temperature_readings]

# Misleading transformation: irrelevant frequency analysis on humidity (red herring)
frequency_spectrum = []
for i in range(len(humidity_readings)):
    val = 0
    for j in range(len(humidity_readings)):
        angle = 2 * math.pi * i * j / len(humidity_readings)
        val += humidity_readings[j] * math.cos(angle)
    frequency_spectrum.append(round(val, 3))

# Dead code path: unused function (distractor)
def calculate_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Unused intermediate variables (decoy computations)
avg_luminosity = sum(luminosity) / len(luminosity)
max_sound = max(sound_levels)
delta_check = avg_luminosity - max_sound

# Core logic: process temperature fluctuations using modular arithmetic and bit manipulation
def extract_thermal_pattern(data):
    pattern = 0
    for idx, val in enumerate(data):
        shifted = int(abs(val) * 10) % 7  # Scale and modulate
        bit_position = idx % 4
        pattern ^= (shifted << bit_position)  # Bitwise mix with rotation effect
    return pattern

# Secondary processing: pair with index-aligned humidity adjustments (zip usage)
adjusted_phases = []
for temp, humid in zip(normalized_temps, humidity_readings):
    phase = temp * (humid / 50.0)
    adjusted_phases.append(round(phase, 3))

# Recursive smoothing filter (simple recursion + modular arithmetic)
def smooth_recursive(arr, depth=0):
    if depth >= 2 or len(arr) <= 1:
        return arr[0] if arr else 0
    new_arr = []
    for i in range(len(arr) - 1):
        avg_val = (arr[i] + arr[i+1]) / 2
        mod_val = (avg_val * 100) % 13  # Modular scaling
        new_arr.append(mod_val / 100.0)
    return smooth_recursive(new_arr, depth + 1)

# Apply recursive smoothing to adjusted phases
smoothed_diagnostic = smooth_recursive(adjusted_phases)

# Generate control checksum (irrelevant but plausible)
checksum = 0
for i, v in enumerate(enumerate(humidity_readings)):
    checksum += v[0] * v[1]
checksum %= 1000

# Destructuring assignment distraction (tuple unpacking)
first, *middle, last = temperature_readings
offset = (first + last) / 2

# Main signal processing chain
raw_pattern = extract_thermal_pattern(normalized_temps)
interim_key = (raw_pattern + int(smoothed_diagnostic * 1000)) % 97

# Final analysis function incorporating enumerate and complex logic
def analyze_signal(signal_data):
    accumulator = 0
    for index, value in enumerate(signal_data):
        if index % 2 == 0:
            accumulator += math.sin(value * math.pi / 4)
        else:
            accumulator -= math.cos(value * math.pi / 6)
    final_score = accumulator * 100
    return round(final_score, 4)

# Processed data used in final call
processed_data = [smoothed_diagnostic, interim_key * 0.1, baseline_temp - 25]

# Critical statement
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")