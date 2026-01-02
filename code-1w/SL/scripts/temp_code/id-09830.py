def analyze_system_health():
    # Simulated telemetry data from distributed nodes
    node_a_latency = [120, 145, 130, 95, 200]
    node_b_latency = [110, 150, 135, 105, 190]
    packet_loss = [0.01, 0.03, 0.02, 0.01, 0.05]
    cpu_temps = [68, 72, 70, 69, 75]  # in Celsius

    # Irrelevant environmental sensor data (distractor)
    ambient_temp = [22, 23, 21, 22, 24]
    humidity_levels = [45, 47, 46, 44, 48]
    power_draw_watts = [145, 150, 148, 146, 155]

    # Misleading preprocessing path (dead code - not used in final calculation)
    def deprecated_normalization(data):
        mean_val = sum(data) / len(data)
        return [round((x - mean_val) / mean_val * 100, 2) for x in data]

    normalized_cpu = deprecated_normalization(cpu_temps)  # Dead assignment

    # Core diagnostic logic
    log_entries = list(map(lambda x: (x[0] + x[1]) // 2, zip(node_a_latency, node_b_latency)))
    
    # System load derived from composite factors (only some are relevant)
    base_load = sum(log_entries[-3:]) // 3
    fluctuation = max(log_entries) - min(log_entries)
    adjustment_factor = 0.8 if fluctuation > 60 else 1.1

    # Hidden threshold logic: count how many readings exceed dynamic baseline
    dynamic_threshold = base_load * adjustment_factor
    critical_count = len(list(filter(lambda x: x > dynamic_threshold, log_entries)))

    # Secondary decoy metric (not actually used in final result)
    stability_score = (100 - fluctuation) * adjustment_factor
    efficiency_ratio = round(stability_score / (base_load / 10), 3)  # Distractor

    # Actual payload computation chain
    def compute_stress_index(entries, load):
        stress = load
        for i, entry in enumerate(entries):
            if i % 2 == 0:
                stress += entry // 15
            else:
                stress -= entry // 25
        if stress < 0:
            stress = abs(stress) * 1.5
        return int(stress)

    # Simulate intermediate transformation (red herring)
    transformed_logs = []
    for val in log_entries:
        transformed_logs.append({
            'raw': val,
            'shifted': val << 1,
            'inverted': ~val,
            'flagged': bool(val & 1)
        })

    # Unused recursive function (decoy complexity)
    def predict_failure_risk(depth, current_risk=0.0):
        if depth <= 1:
            return current_risk
        return predict_failure_risk(depth - 1, current_risk + (0.05 * depth))

    predicted_risk = predict_failure_risk(5)  # Not used

    # Key execution point — this is where the real answer is computed
    final_diagnostic = process_metrics(log_entries, system_load=base_load)

    # Dummy mutation to obscure flow
    final_diagnostic ^= critical_count << 2
    final_diagnostic += int(predicted_risk * 100)

    # Print required at end
    print(f"Result: {final_diagnostic}")

    return final_diagnostic


def process_metrics(entries, system_load):
    # Real processing logic buried among distractions
    total = system_load * 2
    for val in entries:
        if val > 120:
            total += val // 10
        else:
            total -= val // 20
    
    # Apply bit manipulation twist
    total = (total ^ 255) + 100  # XOR with magic number
    
    # Final adjustment based on character count of string representation
    digit_sum = sum(int(c) for c in str(total) if c.isdigit())
    total += digit_sum
    
    return total

# Execute and capture result
current_diagnostic = analyze_system_health()