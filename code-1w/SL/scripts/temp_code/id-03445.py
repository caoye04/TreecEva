def apply_calibration(weight, signal):
    calibrated = (weight ^ signal) + (weight & 7)
    return calibrated if calibrated > 0 else abs(calibrated)

# Sensor data processing
raw_signal = 23
base_offset = 15
logic_weight = 42

# Irrelevant diagnostic flag (distractor)
diagnostic_mode = False
if diagnostic_mode:
    print("Debug: Initializing sensor calibration")

# Key computation chain
intermediate = base_offset - 8
logic_weight = logic_weight >> 1  # Adjust weight using bit shift
logic_weight = logic_weight + (10 if intermediate > 5 else 0)

energy_threshold = apply_calibration(logic_weight, raw_signal)

# Final output
print(f"Result: {energy_threshold}")