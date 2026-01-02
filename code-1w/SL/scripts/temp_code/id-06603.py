def analyze_sensor_network():
    # Simulated sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 22100, 27890, 20010, 26750, 24330, 28990]

    # Irrelevant auxiliary data (distractor)
    calibration_offsets = [120, -85, 200, -45, 90, -110, 65, -75]
    device_ids = ['A7', 'B3', 'C9', 'D2', 'E5', 'F8', 'G1', 'H6']
    location_grid = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1)]

    # Decoy transformation (never used)
    adjusted_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]

    # Critical filtering: only sensors with ID containing odd digits
    active_indices = [i for i, dev_id in enumerate(device_ids) if int(dev_id[1]) % 2 == 1]

    # Filter relevant readings based on device activity
    filtered_data = [raw_readings[i] for i in active_indices]

    # Spurious intermediate calculation (red herring)
    average_offset = sum(calibration_offsets[j] for j in range(0, len(calibration_offsets), 2)) // 4

    # Simulate environmental interference correction (unused path)
    def apply_noise_cancellation(data):
        return [x - 50 if x > 25000 else x + 30 for x in data]

    # Unused recursive helper (dead code)
    def integrate_recursively(values, index=0):
        if index >= len(values):
            return 0
        return values[index] + integrate_recursively(values, index + 1)

    # Real processing begins here
    def smooth_data(seq):
        if len(seq) < 3:
            return seq
        result = [seq[0]]
        for i in range(1, len(seq) - 1):
            result.append(round((seq[i-1] + seq[i] + seq[i+1]) / 3))
        result.append(seq[-1])
        return result

    def classify_trend(value):
        return 'HIGH' if value > 25500 else 'NORMAL'

    def process_readings(data):
        # Step 1: Smooth the data
        smoothed = smooth_data(data)

        # Step 2: Apply unit conversion to degrees Celsius (divide by 1000)
        celsius_values = [x / 1000.0 for x in smoothed]

        # Step 3: Extract names from device IDs (irrelevant but looks important)
        label_fragments = [f'Sensor_{dev[0]}' for dev in device_ids if int(dev[1]) % 2 == 1]

        # Step 4: Create diagnostic codes using string slicing (distractor)
        codes = [frag[7:] + str(int(val * 10) % 100) for frag, val in zip(label_fragments, celsius_values)]

        # Step 5: Determine alert level using conditional expression
        alerts = [100 if classify_trend(val * 1000) == 'HIGH' else 10 for val in celsius_values]

        # Step 6: Aggregate final score with weighted sum
        weights = [0.8, 1.0, 1.2][:len(alerts)]  # Dynamic weighting
        weighted_sum = sum(alerts[i] * weights[i % len(weights)] for i in range(len(alerts)))

        # Step 7: Apply final adjustment based on parity of first reading
        adjustment_factor = 0.95 if int(str(smoothed[0])[-1]) % 2 == 0 else 1.05

        # Final diagnostic computation
        final_score = weighted_sum * adjustment_factor

        # Additional red herring: unused bit manipulation
        masked_value = int(final_score) & 0xFFFF
        shifted_mask = (masked_value << 3) | (masked_value >> 13)

        return int(final_score)  # Only integer part matters

    # Execute main logic
    final_diagnostic = process_readings(filtered_data)

    # Output result as required
    print(f"Result: {final_diagnostic}")

    # Never-used diagnostics (more distraction)
    def generate_report(data):
        return {"count": len(data), "max": max(data), "sum_hex": hex(sum(data))}

    return final_diagnostic

# Run the analysis
analyze_sensor_network()