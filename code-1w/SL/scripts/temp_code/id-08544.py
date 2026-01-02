def analyze_sensor_data():
    # Simulated environmental sensor readings (temperature, pressure, humidity)
    raw_readings = [
        (23.5, 1013.25, 45.0),
        (24.1, 1012.80, 47.3),
        (19.8, 1014.10, 50.1),
        (22.0, 1013.50, 44.7),
        (25.3, 1011.90, 48.8)
    ]

    # Irrelevant transformation: convert to string format (dead-end path)
    stringified = [f'T{t:.1f}_P{p:.2f}_H{h:.1f}' for t, p, h in raw_readings]
    temp_labels = [s.split('_')[0] for s in stringified]

    # Extract temperature values for trend analysis
    temperatures = [reading[0] for reading in raw_readings]

    # Misleading intermediate: calculate moving average (not used later)
    moving_avg = []
    window_size = 3
    for i in range(len(temperatures) - window_size + 1):
        avg = sum(temperatures[i:i+window_size]) / window_size
        moving_avg.append(round(avg, 2))

    # Compute first-difference (delta) sequence for anomaly detection
    temp_deltas = []
    for i in range(1, len(temperatures)):
        temp_deltas.append(temperatures[i] - temperatures[i-1])

    # Apply exponential smoothing as secondary signal (unused distractor)
    alpha = 0.3
    smoothed = [temperatures[0]]
    for t in temperatures[1:]:
        smoothed.append(alpha * t + (1 - alpha) * smoothed[-1])

    # Identify significant change points (abs(delta) > threshold)
    threshold = 1.5
    spikes = [abs(d) > threshold for d in temp_deltas]

    # Count transitions between spike/non-spike states (red herring)
    state_changes = 0
    for i in range(1, len(spikes)):
        if spikes[i] != spikes[i-1]:
            state_changes += 1

    # Compute cumulative deviation from mean
    mean_temp = sum(temperatures) / len(temperatures)
    cum_devs = []
    cum_sum = 0
    for t in temperatures:
        cum_sum += (t - mean_temp)
        cum_devs.append(round(cum_sum, 2))

    # Generate time-based weights (increasing influence over time)
    time_weights = [i**1.5 for i in range(1, len(temperatures)+1)]

    # Weighted cumulative deviation index
    weighted_cumdev = []
    for i, dev in enumerate(cum_devs):
        weighted_cumdev.append(dev * time_weights[i])

    # Normalize to create stability index (0-100 scale)
    max_abs_weighted = max(abs(x) for x in weighted_cumdev)
    stability_index = [100 - abs(w / max_abs_weighted * 100) for w in weighted_cumdev]

    # Secondary metric: rate of change acceleration
    acceleration = []
    for i in range(1, len(temp_deltas)):
        acceleration.append(temp_deltas[i] - temp_deltas[i-1])

    # Combine stability and acceleration into composite health score (unused)
    health_scores = []
    for i in range(len(acceleration)):
        score = stability_index[i+1] * 0.7 + (2 - abs(acceleration[i])) * 5
        health_scores.append(max(0, min(100, score)))

    # Primary processing path: frequency domain analysis via manual DFT (simulated)
    signal = cum_devs  # Use cumulative deviation as base signal
    dft_real = []
    dft_imag = []
    N = len(signal)
    for k in range(N):
        real = 0.0
        imag = 0.0
        for n, x in enumerate(signal):
            angle = 2 * 3.1415926535 * k * n / N
            real += x * __import__('math').cos(angle)
            imag -= x * __import__('math').sin(angle)
        dft_real.append(real)
        dft_imag.append(imag)

    # Focus on dominant low-frequency component (k=1)
    magnitude_at_k1 = (dft_real[1]**2 + dft_imag[1]**2)**0.5

    # Map magnitude to diagnostic confidence (linear scaling)
    confidence_scale = 50.0
    diagnostic_confidence = magnitude_at_k1 * confidence_scale

    # Correction based on initial transient behavior
    early_spikes = sum(spikes[:3])
    correction_factor = 0
    if early_spikes == 0:
        correction_factor = 5.0
    elif early_spikes == 1:
        correction_factor = 2.5
    else:
        correction_factor = -3.0

    # Final aggregation metrics
    aggregate_metrics = [
        mean_temp * 1.5,
        diagnostic_confidence,
        len([d for d in temp_deltas if d > 0]) * 10.0,
        state_changes * 3.5,
        stability_index[-1]
    ]

    # Key assignment statement
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Print result for observable output
    print(f"Result: {final_diagnostic}")

    # Dead code: unused visualization prep
    time_stamps = [f"T{i:02d}" for i in range(len(raw_readings))]
    labeled_data = list(zip(time_stamps, temperatures, stability_index))
    critical_peaks = [label for label, temp, idx in labeled_data if temp > 24.0]

    return final_diagnostic

# Execute function
analyze_sensor_data()