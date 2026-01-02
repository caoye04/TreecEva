import math

def main():
    # System health monitoring simulation with heavy distractions

    # Core metrics (some relevant, some red herrings)
    cpu_load = [0.78, 0.82, 0.91, 0.87, 0.65]
    memory_usage = [0.64, 0.71, 0.76, 0.80, 0.85]
    disk_latency_ms = [12, 15, 11, 20, 24, 18, 14]
    network_packets = [980, 1012, 956, 1100, 1023]  # Irrelevant
    temp_celsius = [42, 45, 47, 50, 53]  # Slight relevance

    # Distractor: unused subsystem logs
    security_logs = [("login", 1), ("scan", 0), ("alert", 1)]
    audit_trail = {"user": "admin", "action": "view", "result": "success"}

    # Threshold baselines (mix of real and decoy)
    thresholds = {
        'load_critical': 0.90,
        'memory_warning': 0.75,
        'temp_limit': 60,
        'latency_normal': 18,
        'packet_min': 500  # Unused
    }

    # Derived statistics (many are distractions)
    avg_cpu = sum(cpu_load) / len(cpu_load)
    peak_memory = max(memory_usage)
    recent_temp_trend = [temp_celsius[i+1] - temp_celsius[i] for i in range(len(temp_celsius)-1)]
    rising_temps = list(filter(lambda x: x > 2, recent_temp_trend))  # Minor use later

    # Fake aggregation (dead path)
    def compute_fictitious_index(data):
        return sum(x ** 0.5 for x in data) * 0.3

    fictitious_score = compute_fictitious_index(network_packets)  # Dead end

    # Real-time anomaly detection (unused)
    anomalies = []
    for i, load in enumerate(cpu_load):
        if load > thresholds['load_critical'] and memory_usage[i] > thresholds['memory_warning']:
            anomalies.append(i)

    # Simulated prediction model (decoy ML)
    def predict_failure(seq):
        smoothed = [seq[i] * 0.6 + seq[i-1] * 0.4 for i in range(1, len(seq))]
        return 1 if sum(smoothed) / len(smoothed) > 0.75 else 0

    predicted_risk = predict_failure(cpu_load)  # Not used in final logic

    # Health metric computation (core path starts here)
    stability_score = 0
    for i in range(len(cpu_load)):
        if cpu_load[i] < 0.85:
            stability_score += 1

    # Latency risk factor
    high_latency_count = len([x for x in disk_latency_ms if x > thresholds['latency_normal']])

    # Temperature-derived stress factor (minor contributor)
    temp_stress = sum(1 for delta in rising_temps if delta >= 3)

    # Composite health vector (only some components used later)
    health_metrics = {
        'stability': stability_score,
        'spikes': len(anomalies),
        'latency_issues': high_latency_count,
        'thermal_events': temp_stress,
        'fictitious': fictitious_score  # Red herring
    }

    # Diagnostic engine (core logic buried in abstraction)
    def analyze_system_state(metrics, limits):
        base_rating = 100

        # Subtle arithmetic chain
        base_rating -= metrics['latency_issues'] * 7
        base_rating -= max(metrics['spikes'] - 1, 0) * 12
        base_rating -= metrics['thermal_events'] * 5

        # Conditional weight adjustment using lambda (real use)
        adjust = lambda x, th: x * 1.5 if x >= th else x * 0.8
        adjusted_stability = adjust(metrics['stability'], 3)

        # Final formula combines multiple concepts
        diagnostic_value = base_rating \
            + adjusted_stability \
            - (limits['load_critical'] * 100) \
            + (math.floor(limits['temp_limit'] / 10) * 3)

        # Normalize to prevent overflow
        return int(max(min(diagnostic_value, 100), 0))

    # --- KEY EXECUTION POINT ---
    final_diagnostic = analyze_system_state(health_metrics, thresholds)

    # Obfuscation: post-calculation noise
    def generate_report_code(code):
        return f"SYS-{hash(str(code)) % 10000}"

    report_id = generate_report_code(final_diagnostic)  # Unused

    # Output required result
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()