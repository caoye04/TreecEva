def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x * 1.05 for x in raw_readings if x > 0]
    outlier_count = sum(1 for x in temp_buffer if x > 900)
    if outlier_count > 100:
        return -999  # Dead logic branch – never reached due to input size

    # Real processing begins: filtering and normalization
    filtered_data = [x for x in raw_readings if 100 <= x <= 800]
    normalized = [(x - 100) / 700 for x in filtered_data]

    # Misleading transformation with unused result
    transformed = [round(x ** 0.5, 3) for x in normalized]
    average_transform = sum(transformed) / len(transformed) if transformed else 0
    dummy_metric = int(average_transform * 1000) % 17  # Unused red herring

    # Core logic: frequency band analysis using modular arithmetic
    band_counts = {i: 0 for i in range(5)}
    for val in filtered_data:
        band = (val // 100) % 5
        band_counts[band] += 1

    # Use of enumerate and zip: align calibration weights with band indices
    calibration_map = {idx: weight for idx, weight in enumerate(calibration_sequence)}
    weighted_sum = sum(band_counts[i] * calibration_map.get(i, 1.0) for i in range(5))
    total_contributions = sum(band_counts.values())
    efficiency_ratio = weighted_sum / total_contributions if total_contributions else 0

    # Conditional expression determining system state
    system_state = 'stable' if efficiency_ratio >= 1.2 else 'degraded'

    # Decoy data structure with complex but irrelevant operations
    decoy_matrix = [[i * j + 2 for j in range(4)] for i in range(4)]
    checksum = sum(sum(row[i] for i in range(len(row))) for row in decoy_matrix) % 19

    # Destructuring assignment (tuple unpacking) - partially relevant
    primary_band, _, secondary_band = sorted(band_counts.items(), key=lambda x: x[1], reverse=True)[0], None, \
                                sorted(band_counts.items(), key=lambda x: x[1], reverse=True))[2]

    # Aggregate diagnostic metric based on top two bands and efficiency
    peak_value = filtered_data[primary_band[0] * 10 + 5] if len(filtered_data) > (primary_band[0] * 10 + 5) else 450
    secondary_value = filtered_data[secondary_band[0] * 10 + 3] if len(filtered_data) > (secondary_band[0] * 10 + 3) else 300

    # Final computation involving min/max/average and integer division
    span = abs(peak_value - secondary_value)
    base_reference = (peak_value + secondary_value) // 2
    adjusted_span = max(span - 50, 0)
    health_index = min(100, 150 - adjusted_span // 5)

    # Critical variable computed here — this is the answer
    final_diagnostic = int((health_index * efficiency_ratio) // 1.3)

    return final_diagnostic


def aggregate_metrics(chain, validator):
    return chain

# Simulated sensor readings and calibration profile
sensor_input = list(range(120, 751, 3))  # Deterministic sequence
calibration_profile = [0.9, 1.1, 1.3, 0.8, 1.4]

# Processing chain setup with distraction
processing_chain = sum(x for x in sensor_input if x % 2 == 0 and x > 200)
validation_map = {k: v * 0.95 for k, v in enumerate(calibration_profile)}

# Red herring: unused recursive function
def compute_entropy(data, depth=0):
    if depth > 5 or len(data) == 0:
        return 0
    mid = len(data) // 2
    return data[mid] * 0.1 + compute_entropy(data[:mid], depth + 1)

# Unused set operations creating illusion of complexity
observed_bands = {b % 5 for b in sensor_input}
critical_bands = {1, 2, 3}
overlap_score = len(observed_bands & critical_bands) + len(observed_bands - critical_bands)

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, validation_map)

# Actual call that produces the real value
final_diagnostic = analyze_sensor_data(sensor_input, calibration_profile)

print(f"Result: {final_diagnostic}")