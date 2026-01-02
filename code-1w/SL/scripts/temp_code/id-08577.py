def main():
    # Sensor data calibration and transformation
    raw_readings = (14.2, 17.5, 13.8, 16.1)
    offset = 1.2
    scale_factor = 0.8

    # Apply calibration using lambda for dynamic adjustment
    calibrate = lambda x: round((x - offset) * scale_factor, 2)
    calibrated = tuple(map(calibrate, raw_readings))

    # Filter significant values above threshold
    threshold = 10.0
    filtered = tuple(x for x in calibrated if x > threshold)

    # Process data through aggregation
    processed_data = sum(filtered) + len(filtered)

    # Final nonlinear transformation
    transform = lambda x: int(x * 0.9 + 2.5)
    result = transform(processed_data)

    print(f"Result: {result}")

main()