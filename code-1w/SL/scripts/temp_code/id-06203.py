def analyze_signal(strength, noise_level):
    baseline = strength - noise_level
    adjustment_factor = lambda x: x ** 0.5 if x > 0 else 0
    return baseline * adjustment_factor(baseline)


def apply_calibration(value):
    calibration_map = [0.8, 0.9, 1.0, 1.1, 1.2]
    level = min(int(value // 10), 4)
    return value * calibration_map[level]

# Simulate sensor data processing
raw_strength = 144
ambient_noise = 45

# Step 1: Analyze raw signal with dynamic adjustment
processed_signal = analyze_signal(raw_strength, ambient_noise)

# Step 2: Filter based on minimum detectable threshold
if processed_signal < 30:
    threshold_score = 0
else:
    threshold_score = processed_signal * 1.25

# Step 3: Apply system calibration based on signal tier
final_diagnostic = apply_calibration(threshold_score)

print(f"Result: {threshold_score}")