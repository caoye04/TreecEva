readings = [12, -5, 0, 37, 42, -15, 8, 0, 23]
min_energy = 10
max_duration = 5

# Normalize negative readings and apply time-based decay for long durations
decayed_readings = [r * 0.9 for r in readings if r > 0]

# Filter valid energy pulses above threshold and within operational duration
valid_pulses = [p for p in decayed_readings if p >= min_energy]

# Simulate signal loss by removing every second pulse beyond first two
cropped_pulses = valid_pulses[:2] + [valid_pulses[i] for i in range(2, len(valid_pulses)) if i % 2 == 0]

# Apply smoothing filter to reduce noise
smoothed = [cropped_pulses[i] for i in range(len(cropped_pulses)) if i == 0 or cropped_pulses[i] - cropped_pulses[i-1] <= 15]

# Final filtering step based on system stability window
stability_window = 3
filtered_readings = smoothed[-stability_window:] if len(smoothed) >= stability_window else smoothed

energy_threshold = filtered_readings[-1] if filtered_readings else 0
print(f"Result: {energy_threshold}")