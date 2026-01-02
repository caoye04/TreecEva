def main():
    # Sensor data calibration and transformation simulation
    raw_readings = [12, 15, 22, 8, 33]
    offset = 5
    calibrated = [x + offset for x in raw_readings]

    # Filter out values below threshold
    threshold = 20
    filtered = [x for x in calibrated if x > threshold]

    # Processing step with lambda abstraction
    process = lambda val: val * 2 - 4
    processed_data = sum(process(x) for x in filtered)

    # Final transformation function
    transform = lambda data: data + 10 if data < 100 else data - 5
    result = transform(processed_data)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()