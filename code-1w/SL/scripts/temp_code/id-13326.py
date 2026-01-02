def analyze_particle_data(readings):
    raw_offsets = [r % 17 for r in readings if r > 50]
    adjusted_readings = [r * 1.05 + 3.2 for r in readings]
    outlier_threshold = sum([1 for x in adjusted_readings if x > 100])

    # Irrelevant transformation - decoy
    transformed = []
    for val in adjusted_readings:
        if val < 60:
            transformed.append(val ** 0.5)
        elif val > 90:
            transformed.append(val / 2.5)
    unused_metric = max(transformed) - min(transformed)

    # Core logic disguised among distractions
    microns = [x for x in readings if x % 4 == 0]
    shift_corrected = [(m >> 2) for m in microns]
    saturated = [min(s, 45) for s in shift_corrected]

    # Decoy conditional with misleading early return hint
    if len(microns) > 10:
        temp_result = sum(saturated) / len(saturated)
        flag = True
    else:
        temp_result = 0
        flag = False

    # Actual key computation embedded in list processing
    filtered_microns = [s for s in saturated if s > 15]
    
    # Dead code path - never executed due to data
    extreme_cases = []
    for item in readings:
        if item > 200:  # No reading exceeds 150
            extreme_cases.append(item << 3)
    cleanup = lambda x: x & 0xFF

    # Key statement
    filtration_yield = sum(filtered_microns) // len(filtered_microns)

    # Final red herring: complex but unused bitwise aggregation
    aggregate_signature = 0
    for i, v in enumerate(filtered_microns):
        aggregate_signature ^= (v << (i % 5)) | (i & 7)

    return filtration_yield

# Simulated sensor input - deterministic
sensor_readings = [48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104]

result = analyze_particle_data(sensor_readings)
print(f"Result: {result}")