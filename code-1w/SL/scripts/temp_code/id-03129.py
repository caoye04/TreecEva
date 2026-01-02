def main():
    # System health monitoring simulation with diagnostic analysis
    raw_signals = [0.78, 0.91, 0.65, 0.83, 0.72, 0.88, 0.76, 0.85]
    calibration_factor = 1.04
    sample_rate = 100
    timestamp_offset = 1623475200

    # Irrelevant signal processing (distractor)
    filtered_data = [x * calibration_factor for x in raw_signals if x > 0.7]
    avg_filtered = sum(filtered_data) / len(filtered_data) if filtered_data else 0

    # Primary data transformation
    processed_readings = list(map(lambda x: round(x ** 2 * 100), raw_signals))

    # Decoy structure (dead path)
    class LegacyProcessor:
        def __init__(self):
            self.version = '1.0'
            self.active = False

        def process(self, data):
            return [d // 2 for d in data]  # Unused

    # Core diagnostic indicators
    critical_levels = {"high": 7500, "medium": 5000, "low": 2500}
    activation_flags = set()
    for reading in processed_readings:
        if reading > critical_levels["high"]:
            activation_flags.add("critical")
        elif reading > critical_levels["medium"]:
            activation_flags.add("elevated")

    # Auxiliary computation (misleading intermediate)
    peak_index = max(range(len(processed_readings)), key=lambda i: processed_readings[i])
    temporal_weight = (peak_index + 1) * sample_rate
    phantom_score = temporal_weight * 0.37  # Looks important but unused

    # Threshold mapping with set operations
    base_thresholds = {500, 1500, 2500, 3500, 4500, 5500, 6500, 7500}
    dynamic_adjustment = {x for x in base_thresholds if x % 1000 == 500}
    adjusted_set = base_thresholds - dynamic_adjustment  # Remove some elements
    threshold_map = {"A": min(adjusted_set), "B": sum(adjusted_set) // len(adjusted_set)}

    health_indicators = {
        "readings": processed_readings,
        "flags": activation_flags,
        "baseline": 1000,
        "version": 2.1
    }

    # Red herring function (never called)
    def deprecated_analysis(data):
        cumulative = 0
        for i in range(len(data)):
            if i % 2 == 0:
                cumulative += data[i] * 0.1
        return cumulative * 0.95

    # Real analysis function with recursion
    def analyze_metrics(data, thresholds):
        values = data["readings"]
        baseline = data["baseline"]
        flags = data["flags"]

        def recursive_contributions(idx, acc):
            if idx >= len(values):
                return acc
            contribution = (values[idx] - baseline) // 100
            new_acc = acc + (contribution if contribution > 0 else 0)
            return recursive_contributions(idx + 1, new_acc)

        base_influence = recursive_contributions(0, 0)
        
        # Conditional expression chain
        risk_modifier = 1.25 if "critical" in flags else (1.1 if "elevated" in flags else 1.0)
        adjustment_factor = thresholds["B"] / 5000.0
        
        # Final computation
        preliminary_score = base_influence * risk_modifier
        final_correction = preliminary_score * adjustment_factor
        
        # Secondary diagnostic path (looks parallel but isn't used)
        shadow_diagnostic = sum(values) / (len(values) * 10)  # Distractor
        
        return int(final_correction)

    # Execution point of interest
    final_diagnostic = analyze_metrics(health_indicators, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()