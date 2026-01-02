def main():
    # Simulate sensor data stream for environmental monitoring
    raw_readings = [23.4, 18.9, 21.2, 25.1, 19.8, 24.3, 22.7, 20.5, 26.0, 17.9]
    
    # Irrelevant preprocessing: normalize to z-scores (not used in final computation)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in raw_readings]  # Dead end

    # Slice critical segment for analysis
    critical_window = raw_readings[2:8]

    # Apply moving average filter (partially relevant)
    smoothed = []
    for i in range(len(critical_window) - 1):
        smoothed.append((critical_window[i] + critical_window[i+1]) / 2)
    
    # Introduce misleading trend analysis
    increasing_trend = 0
    for i in range(1, len(smoothed)):
        if smoothed[i] > smoothed[i-1] + 0.5:
            increasing_trend += 1
    trend_ratio = increasing_trend / len(smoothed) if smoothed else 0  # Unused

    # Define threshold function using lambda (required feature)
    threshold_func = lambda x: x > 21.0

    # Construct flow data with metadata (tuple unpacking and slicing)
    timestamps = list(range(1000, 1000 + len(smoothed)))
    status_flags = ['OK', 'WARN', 'OK', 'OK', 'ERROR', 'OK']
    flow_data = []
    for i, val in enumerate(smoothed):
        flag = status_flags[i % len(status_flags)]
        flow_data.append((timestamps[i], val, flag))
    
    # Distractor: complex flag counting (not used)
    flag_count = {}
    for _, _, f in flow_data:
        flag_count[f] = flag_count.get(f, 0) + 1
    major_flag = max(flag_count, key=flag_count.get)

    # Core calculation function (uses recursion and slicing)
    def calculate_equilibrium(data, condition):
        if not data:
            return 0
        head, *tail = data  # Destructuring assignment
        t, v, flag = head
        if condition(v):
            # Recursive contribution with weight based on position
            contribution = v * 0.9 ** len(tail)
            return contribution + calculate_equilibrium(tail, condition)
        else:
            return 0.5 * calculate_equilibrium(tail, condition)

    # Key statement
    equilibrium_score = calculate_equilibrium(flow_data, threshold_func)

    # Additional red herring: FFT-like frequency check (irrelevant)
    signal_powers = [v ** 2 for t, v, f in flow_data]
    total_power = sum(signal_powers)
    spectral_rhythm = total_power / len(signal_powers) if signal_powers else 0

    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()