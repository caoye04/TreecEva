def main():
    # Sensor calibration constants (irrelevant to final result)
    calib_factor_a = 0.987
    calib_offset_b = -0.013
    baseline_noise = [0.002, -0.001, 0.004]

    # Simulated sensor readings from environmental monitoring array
    sensor_data = [
        {'id': 'S1', 'values': [12, 15, 14, 13], 'type': 'temp'},
        {'id': 'S2', 'values': [8, 10, 9, 11], 'type': 'temp'},
        {'id': 'S3', 'values': [25, 24, 26, 25], 'type': 'temp'}
    ]

    # Irrelevant diagnostic counters
    status_codes = {'OK': 0, 'WARN': 0, 'ERROR': 0}
    debug_trace = []

    # Auxiliary function for noise correction (never called)
    def correct_noise(readings):
        return [r + calib_factor_a * calib_offset_b for r in readings]

    # Data transformation pipeline (partially relevant)
    processed = []
    for entry in sensor_data:
        avg = sum(entry['values']) / len(entry['values'])
        processed.append({'id': entry['id'], 'avg': avg})

    # Threshold logic using lambda (critical component)
    threshold_func = lambda x: x > 13.5

    # Red herring: complex frequency analysis (unused)
    def compute_fft(magnitude_list):
        import math
        N = len(magnitude_list)
        fft_result = []
        for k in range(N):
            real = sum(magnitude_list[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
            imag = -sum(magnitude_list[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
            fft_result.append(complex(real, imag))
        return fft_result

    freq_analysis = compute_fft([1, 2, 1, 0])  # Dead computation

    # State tracking with misleading intermediate values
    system_state = {
        'last_update': '2023-11-15',
        'version': '2.1.0',
        'mode': 'diagnostic'
    }

    # Core analysis function with conditional expression
    def analyze_readings(data, threshold_check):
        valid_count = 0
        total_avg = 0.0
        for record in data:
            # Extract average computed earlier
            avg_val = next(p['avg'] for p in processed if p['id'] == record['id'])
            # Apply threshold
            if threshold_check(avg_val):
                valid_count += 1
                total_avg += avg_val
        # Conditional expression determines output
        return int(total_avg) if valid_count > 0 else -1

    # Critical execution point
    final_diagnostic = analyze_readings(sensor_data, threshold_func)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()