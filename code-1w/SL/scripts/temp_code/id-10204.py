def main():
    # Domain-specific context: Sensor data calibration with noise filtering
    raw_readings = [15, 23, 9, 42, 71, 6, 88, 33, 90, 105, 12, 47, 66, 73, 3]
    calibration_factor = 0.98
    threshold = 50
    offset = 17

    # Irrelevant statistical tracking (distractor)
    avg_reading = sum(raw_readings) / len(raw_readings)
    variance = sum((x - avg_reading) ** 2 for x in raw_readings) / len(raw_readings)
    entropy_approx = -(sum((x / sum(raw_readings)) * ((x / sum(raw_readings)) ** 0.5) for x in raw_readings if x > 0))

    # Signal processing pipeline
    amplified = [int(x * calibration_factor) for x in raw_readings]
    shifted = [x + offset for x in amplified]

    # Noise filtering: remove outliers beyond threshold (but not used in final path)
    filtered_outliers = [x for x in shifted if x < threshold * 1.5]

    # Decoy transformation chain (dead path)
    def decoy_transform(data):
        return [x ^ 0xF for x in data if x % 2 == 0]
    
    decoy_result = decoy_transform(shifted)  # unused

    # Core data refinement (relevant)
    normalized = [x // 2 for x in shifted]  # reduce to base scale

    # Conditional masking based on dual criteria (mixed logic)
    masked = []
    for val in normalized:
        if val > 30:
            if val % 5 == 0:
                masked.append(val * 2)
            else:
                masked.append(val)
        else:
            masked.append(val - (val % 4))  # align to lower multiple of 4

    # Simulated hardware register adjustment (bit manipulation red herring)
    reg_value = 0xABC
    for _ in range(3):
        reg_value = (reg_value << 1) | (reg_value >> 11)
        reg_value &= 0xFFFF

    # Data categorization (unused classification)
    categories = {}
    for x in masked:
        key = 'high' if x > 40 else 'low'
        categories[key] = categories.get(key, 0) + 1

    # Critical processing path begins here
    processed = []
    for x in masked:
        if x % 2 == 0:
            processed.append(x + 1)
        else:
            processed.append(x)

    # Finalize checksum through multi-step reduction
    temp_store = []
    for i, x in enumerate(processed):
        if i % 2 == 0:
            temp_store.append(x)

    # Key statement with lambda and conditional expression
    finalize = lambda x: x + 100 if x < 200 else x * 0.5
    checksum = finalize(sum(filter(lambda x: x % 3 == 0, temp_store)))

    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()