def main():
    # Simulate sensor data from a thermal regulation system
    raw_temperatures = [23.5, 24.1, 25.0, 26.3, 27.8, 28.0, 27.5, 26.0, 24.5, 23.0]
    time_intervals = list(range(len(raw_temperatures)))

    # Misleading preprocessing: irrelevant transformation
    offset_correction = sum([t ** 0.5 for t in raw_temperatures]) / len(raw_temperatures)
    corrected_temps = [t + offset_correction - 0.5 for t in raw_temperatures]

    # Actual relevant processing begins
    threshold = 25.0
    high_temp_indices = [i for i, t in enumerate(corrected_temps) if t >= threshold]
    
    # Slice to get stable phase (last 3 high-temp readings)
    if len(high_temp_indices) >= 3:
        analysis_window = corrected_temps[high_temp_indices[-3]:]
    else:
        analysis_window = corrected_temps[-5:]

    # Compute rolling average using lambda
    window_size = 2
    rolling_avg = lambda arr, n: [(sum(arr[i:i+n]) / n) for i in range(len(arr)-n+1)]
    smoothed_data = rolling_avg(analysis_window, window_size)

    # Secondary distraction: unused energy estimation
    baseline_power = 12.8
    duration_hours = len(time_intervals) / 2
    estimated_energy = baseline_power * duration_hours * (1 + (max(raw_temperatures) - min(raw_temperatures)) / 10)

    # Distractor function that's defined but not used
    def predict_next(temp_list):
        return sum(temp_list[-3:]) / 3 * 1.02

    # Process data for efficiency calculation
    processed_data = {
        'avg_smoothed': sum(smoothed_data) / len(smoothed_data),
        'stability_factor': len([x for x in smoothed_data if abs(x - sum(smoothed_data)/len(smoothed_data)) < 0.5]),
        'duration': len(smoothed_data)
    }

    # Key computation step
    efficiency_score = calculate_efficiency(processed_data)

    # Print result as required
    print(f"Result: {efficiency_score}")

    # Return for internal clarity (not affecting output)
    return efficiency_score


def calculate_efficiency(data):
    base = data['avg_smoothed'] * 0.8
    adjustment = data['stability_factor'] * 0.5
    duration_mod = (data['duration'] - 1) * 0.1
    return int(base - adjustment + duration_mod)

if __name__ == "__main__":
    main()