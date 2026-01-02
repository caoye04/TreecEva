import math

# Simulated atmospheric data processing with red herrings and distractions
def analyze_pressure_readings(readings):
    if len(readings) < 3:
        return 0

    # Irrelevant transformation (dead path)
    inverted = [round(1.0 / x, 4) for x in readings if x != 0]

    # Real computation begins: find stable window (three consecutive near-equal values)
    stable_window_found = False
    for i in range(len(readings) - 2):
        a, b, c = readings[i], readings[i+1], readings[i+2]
        if abs(a - b) <= 0.1 and abs(b - c) <= 0.1:
            median_stable = (a + b + c) / 3
            stable_window_found = True
            break

    if not stable_window_found:
        median_stable = sum(readings) / len(readings)

    # Decoy calculation - looks important but unused
    smoothed = []
    for j in range(len(readings)):
        window = readings[max(0, j-1):min(j+2, len(readings))]
        smoothed.append(sum(window) / len(window))
    trend_score = sum(smoothed[i] - smoothed[i-1] for i in range(1, len(smoothed)))

    # Distractor: complex bit manipulation with no effect on result
    magic_key = 0
    for val in readings:
        shifted = int(val * 10) & 0xFF
        magic_key ^= (shifted << 1) | (shifted >> 7)
    magic_key = magic_key & 0xFFFF

    # Slice-based anomaly check (irrelevant to final result)
    mid_section = readings[len(readings)//3 : 2*len(readings)//3]
    anomaly_detected = any(x > 1.5 * median_stable for x in mid_section)

    # Another decoy function embedded inside
    def predict_next(arr):
        return arr[-1] + (arr[-1] - arr[0]) / len(arr)

    predicted = predict_next(readings)  # Unused

    # Core logic hidden among noise: normalize and extract control signal
    raw_signal = median_stable * 100
    control_signal = int(raw_signal) & 0xFF  # Keep lower 8 bits

    # Linear search for closest power of two (distractor)
    powers_of_two = [2**i for i in range(16)]
    best_match = 1
    for p in powers_of_two:
        if abs(p - control_signal) < abs(best_match - control_signal):
            best_match = p

    # Actual path: use control_signal to index into transformed slice
    phase_shift = [math.sin(i * math.pi / 8) for i in range(16)]
    index = control_signal % 16
    phase_value = phase_shift[index]

    # Final computation chain
    base_pressure = abs(median_stable)
    correction_term = math.log(base_pressure + 1) if base_pressure > 0 else 0
    final_pressure = base_pressure + correction_term

    adjustment_factor = 0.85 + (phase_value * 0.15)  # Modulates based on phase

    # Key statement
    equilibrium_score = final_pressure * adjustment_factor

    # Print required output
    print(f"Result: {equilibrium_score}")
    return equilibrium_score

# Irrelevant dataset preparation
sensor_data = [0.88, 0.91, 0.89, 1.05, 1.42, 0.87, 0.90, 0.89, 1.11, 1.73]
offset_calib = [x + 0.02 for x in sensor_data]
duplicate_filtered = list(dict.fromkeys(offset_calib))

# Entry point
result = analyze_pressure_readings(sensor_data)
