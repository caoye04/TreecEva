def main():
    # System calibration parameters (some are distractions)
    base_frequency = 440.5
    sample_rate = 2048
    temperature_offset = -273.15
    adjustment_ratio = 1.05

    # Core signal processing variables
    signal_chain = [0.8, 1.2, 0.9, 1.5, 0.7]
    filtered_peaks = []
    peak_magnitude = 0.0

    for val in signal_chain:
        if val > 1.0:
            filtered_peaks.append(val * adjustment_ratio)
            peak_magnitude += val ** 2

    # Secondary computation: noise floor estimation (distractor block)
    noise_floor = 0.0
    for i in range(len(signal_chain)):
        noise_floor += (signal_chain[i] - 1.0) ** 2
    noise_floor /= len(signal_chain)

    # Threshold logic with lambda-based dynamic filter
    dynamic_filter = lambda x, t: list(filter(lambda y: y > t, x))
    threshold = 1.1
    logic_flow = dynamic_filter(filtered_peaks, threshold)

    # Scaling factor derived from physical constants (partially relevant)
    boltzmann_constant = 1.38e-23  # distractor
    scaling_factor = len(logic_flow) + (threshold // 0.55)

    # Helper function embedded within main scope
    def calculate_efficiency(peaks, thresh):
        if not peaks:
            return 0.0
        efficiency = 0.0
        temp_state = []
        for p in peaks:
            if p > thresh * 1.05:
                efficiency += 0.3
            elif p > thresh:
                efficiency += 0.15
            temp_state.append(efficiency)  # unused state
        return efficiency + 0.05  # fixed bonus for non-empty

    # Key statement where target variable is computed
    thermal_capacity = calculate_efficiency(logic_flow, threshold) * scaling_factor

    # Dead code path - never executed but looks meaningful
    if temperature_offset > 0:
        thermal_capacity *= (1 + noise_floor)

    # Irrelevant transformation on a copy
    final_peaks = [round(x * 100) / 100 for x in filtered_peaks]

    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()