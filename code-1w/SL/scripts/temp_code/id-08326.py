def main():
    # Simulated sensor data with noise and metadata
    raw_sensor_stream = [23.1, 19.5, 107, -45, 88, 1003, 0, 12, 99, 107, 23.1, 19, 44, 107, 88, 66, 19]
    metadata_flags = {"device_id": "SNSR-7X", "calibration_offset": 1.1, "version": 2}
    temp_log = [round(x * 1.02, 2) for x in raw_sensor_stream if isinstance(x, float)]

    # Irrelevant transformation: convert to hex codes (dead path)
    hex_codes = [hex(int(x)) for x in raw_sensor_stream if isinstance(x, int) and x > 0]
    redundant_copy = raw_sensor_stream[:]

    # Extract and clean data: filter out non-numeric anomalies and duplicates
    cleaned_data = []
    seen = set()
    for val in raw_sensor_stream:
        if isinstance(val, (int, float)) and val != 1003 and val != -45:
            if val not in seen:
                cleaned_data.append(val)
                seen.add(val)

    # Checksum baseline
    base_checksum = sum(int(x) for x in cleaned_data if x < 100) % 97

    # Data windowing via slicing
    time_window_slice = cleaned_data[2:10]  # Only process middle segment
    reversed_window = time_window_slice[::-1]

    # Secondary filtering based on parity and magnitude
    filtered_data = []
    for x in reversed_window:
        if x % 2 == 0 and x in {88, 12, 66, 44}:
            filtered_data.append(x * 2)
        elif x == 23.1:
            filtered_data.append(46)
        else:
            filtered_data.append(abs(int(x) - 10))

    # Decoy function call (no side effects)
    def analyze_outliers(data):
        return [x for x in data if x > 50]
    outlier_report = analyze_outliers(cleaned_data)  # unused

    # Real computation begins here
    def compute_checksum(data):
        cs = 0
        for i, v in enumerate(data):
            cs += v * (i + 1)
        return cs % 100000

    filtered_checksum = compute_checksum(filtered_data)

    # Unused backup checksum method (distractor)
    backup_checksum = 0
    for idx in range(len(filtered_data)):
        backup_checksum += (filtered_data[idx] + idx) ** 2
    backup_checksum %= 98765

    # Spurious string operations
    status_msg = "Processing complete"
    status_chars = [c.upper() for c in status_msg if c in 'aeiou']
    char_count = len(status_chars)

    # Final red herring: nested conditional with no impact
    if base_checksum > 50:
        if len(filtered_data) < 10:
            for j in range(3):
                base_checksum -= j * 3
    else:
        temp_val = base_checksum ** 2
        temp_val %= 44

    # Critical execution point
    filtered_checksum = compute_checksum(filtered_data)

    print(f"Result: {filtered_checksum}")

if __name__ == "__main__":
    main()