def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant pre-processing: Normalize data (not used in final path)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > thresholds[0]]

    # Distractor: complex-looking but unused signal transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val * 1.5)
        else:
            transformed.append(val * 0.7)

    # Real processing begins: windowed moving average
    window_size = 3
    moving_averages = []
    for i in range(len(raw_readings) - window_size + 1):
        window = raw_readings[i:i + window_size]
        avg = sum(window) / window_size
        moving_averages.append(avg)

    # Secondary distractor: frequency domain analysis (dead code)
    def compute_dft(signal):
        N = len(signal)
        dft = []
        for k in range(N):
            real = sum(signal[n] * __import__('math').cos(2 * __import__('math').pi * k * n / N) for n in range(N))
            imag = sum(-signal[n] * __import__('math').sin(2 * __import__('math').pi * k * n / N) for n in range(N))
            dft.append(complex(real, imag))
        return dft

    # Unused call - red herring
    _ = compute_dft(moving_averages[:4])

    # Actual logic: detect anomalies based on threshold crossings
    anomaly_flags = []
    for val in moving_averages:
        flag = 1 if val > thresholds[1] else 0
        anomaly_flags.append(flag)

    # Accumulate diagnostic score only at specific indices
    diagnostic_accumulator = 0
    indices_of_interest = [i for i in range(len(anomaly_flags)) if i % 3 == 0]
    for idx in indices_of_interest:
        diagnostic_accumulator += anomaly_flags[idx] * (idx + 1)

    # Bit manipulation decoy (irrelevant computation)
    bit_fiddling = 0
    temp = diagnostic_accumulator
    while temp:
        bit_fiddling ^= temp
        temp >>= 1

    # Real aggregation: cumulative sum of moving averages at even positions
    aggregate_metrics = []
    for i, avg_val in enumerate(moving_averages):
        if i % 2 == 0:
            if not aggregate_metrics:
                aggregate_metrics.append(avg_val)
            else:
                aggregate_metrics.append(aggregate_metrics[-1] + avg_val)

    # Correction factor derived from original data length (key dependency)
    base_offset = len(raw_readings)
    spike_count = sum(1 for x in raw_readings if x > thresholds[2])
    correction_factor = base_offset - spike_count  # This affects final result

    # Final combination - target execution point
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Red herring print (never reached)
    # print('Debug:', bit_fiddling, transformed[:3])

    # Output the target result
    print(f"Target result: {final_diagnostic}")

# Inputs
readings = [12, 15, 8, 20, 22, 10, 25, 18, 14]
thresholds_config = [9, 16, 21]

# Execute
analyze_sensor_data(readings, thresholds_config)