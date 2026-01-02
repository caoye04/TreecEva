def main():
    # Simulate sensor data streams for thermal equilibrium analysis
    temperatures = [22.1, 23.5, 24.0, 25.8, 26.3, 27.0, 25.9, 24.2]
    pressures = [101.3, 102.1, 103.5, 104.0, 103.8, 102.7, 101.9, 100.5]
    humidity = [45, 47, 50, 55, 58, 60, 57, 53]

    # Misleading preprocessing: irrelevant transformation
    processed_humidity = [h * 1.05 for h in humidity if h > 40]
    avg_humid = sum(processed_humidity) / len(processed_humidity)
    deviation_factor = (max(processed_humidity) - min(processed_humidity)) / avg_humid

    # Core data for flow dynamics
    flow_magnitudes = [abs(t - p / 10) for t, p in zip(temperatures, pressures)]
    flow_directions = [1 if t > 25 else -1 for t in temperatures]

    # Annotate flow with index and direction using enumerate and zip
    flow_data = []
    for idx, (mag, dir_) in enumerate(zip(flow_magnitudes, flow_directions)):
        flow_data.append({'index': idx, 'magnitude': mag, 'direction': dir_, 'raw_t': temperatures[idx]})

    # Auxiliary computation: appears important but not used in final result
    trend_pairs = list(zip(temperatures, temperatures[1:]))
    rising_phases = [1 for a, b in trend_pairs if b > a + 0.1]
    stability_metric = len(rising_phases) / len(trend_pairs)

    # Threshold function with lambda abstraction
    threshold_func = lambda x: x['magnitude'] > 1.5 and x['raw_t'] >= 24.0

    # Secondary distraction: unused helper attempting pattern detection
    def detect_oscillation(data, window=3):
        if len(data) < window:
            return False
        oscillations = 0
        for i in range(len(data) - window + 1):
            segment = data[i:i+window]
            diffs = [segment[j+1] - segment[j] for j in range(window-1)]
            if all(d != 0 and diffs[j] * diffs[j+1] < 0 for j in range(len(diffs)-1)):
                oscillations += 1
        return oscillations > 1

    # Unused call that looks relevant
    has_instability = detect_oscillation(pressures)

    # Key state tracking: compute equilibrium score based on filtered bidirectional flows
    def calculate_equilibrium(flows, threshold):
        positive_contributions = []
        negative_contributions = []

        for entry in flows:
            if threshold(entry):
                if entry['direction'] == 1:
                    positive_contributions.append(entry['magnitude'])
                else:
                    negative_contributions.append(entry['magnitude'])

        sum_pos = sum(positive_contributions)
        sum_neg = sum(negative_contributions)

        # Compute net balance weighted by counts to avoid division by zero
        count_pos = len(positive_contributions)
        count_neg = len(negative_contributions)

        # Distraction: dead code path due to logic
        adjustment = 0.0
        if count_pos > count_neg * 2:
            adjustment = 1.5  # Never reached in this data

        base_score = (sum_pos - sum_neg) * (count_pos + 1) / (count_neg + 1)
        return int(base_score + adjustment)  # Deterministic integer output

    # Critical execution point
    equilibrium_score = calculate_equilibrium(flow_data, threshold_func)

    # Print result as required
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()