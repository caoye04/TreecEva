from itertools import compress, count

# Simulated sensor array data with noise and redundancy
def analyze_sensor_readings(readings):
    base_indices = count(1)
    indexed_data = [(next(base_indices), val) for val in readings]

    # Irrelevant transformation: frequency emulation (dead path)
    freq_mod = [v % 127 for _, v in indexed_data if v > 50]
    normalized = [v / 1.8 for v in freq_mod]  # Distractor computation

    # Core logic: identify valid pulses above threshold
    thresholds = {i: 45 + (i % 5) for i in range(1, len(readings) + 1)}
    strong_pulse = [val >= thresholds[idx] for idx, val in indexed_data]
    pulse_magnitude = [val if mask else 0 for (idx, val), mask in zip(indexed_data, strong_pulse)]

    # Secondary filter: reject isolated spikes using neighbor consensus
    smooth_mask = []
    for i in range(len(strong_pulse)):
        left = strong_pulse[i-1] if i > 0 else False
        center = strong_pulse[i]
        right = strong_pulse[i+1] if i < len(strong_pulse) - 1 else False
        smooth_mask.append(center and (left or right))

    # Tertiary adjustment: phase shift correction (irrelevant but plausible)
    phase_shifts = [abs((val - 50) // 10) for val in readings]
    adjusted_indices = [i - ps for i, ps in enumerate(phase_shifts)]  # Unused

    # Critical filtering step: only contributions that pass spatial coherence
    spatial_weights = [0.9, 1.0, 1.1, 0.8, 1.2]
    weighted_contributions = []
    for i, mag in enumerate(pulse_magnitude):
        weight = spatial_weights[i % len(spatial_weights)]
        weighted_contributions.append(mag * weight)

    # Apply neighbor-smoothed mask
    filtered_contributions = [wc if sm else 0 for wc, sm in zip(weighted_contributions, smooth_mask)]

    # Dead-end branch: entropy approximation (red herring)
    bit_entropy = 0
    for x in filtered_contributions:
        if x > 0:
            import math
            bit_entropy += math.log(x) * (-x / 100)  # Not used later

    # Key assignment point — answer depends on this
    filtration_score = sum(filtered_contributions)

    # Final output with decoy formatting
    print(f"Sensor summary: {len([f for f in filtered_contributions if f > 0])} active")
    print(f"Total raw energy: {sum(pulse_magnitude):.2f}")
    print(f"Target result: {filtration_score}")
    return filtration_score

# Input data: calibrated test sequence
sensor_input = [42, 68, 55, 30, 73, 52, 28, 60, 77, 58]

result = analyze_sensor_readings(sensor_input)