def calculate_system_efficiency(log_entries):
    total_operations = 0
    failed_ops = 0
    energy_consumption = 0.0
    peak_load = 0
    temp_buffer = []
    correction_factor = 1.0
    
    for entry in log_entries:
        op_type = entry['type']
        success = entry['success']
        power_used = entry['power']
        timestamp = entry['ts']

        if op_type == 'compute':
            total_operations += 1
            energy_consumption += power_used
            temp_buffer.append(power_used)
            
            if not success:
                failed_ops += 1

            if len(temp_buffer) > 2:
                avg_recency = sum(temp_buffer[-3:]) / 3
                if avg_recency > 80:
                    peak_load += 1

        elif op_type == 'idle':
            energy_consumption += power_used * 0.1  # reduced weight
            continue  # no operation counting for idle

    # Misleading secondary analysis (distractor)
    anomaly_detector = lambda x: x > 95
    anomalies = [p for p in temp_buffer if anomaly_detector(p)]
    if len(anomalies) > 5:
        correction_factor = 0.9
    else:
        correction_factor = 1.05

    # Irrelevant statistical moment calculation
    moment_sum = sum((x - energy_consumption / len(temp_buffer)) ** 3 for x in temp_buffer) if temp_buffer else 0
    skewness = moment_sum / (len(temp_buffer) or 1)

    # Core metric computation with distractors
    base_success_rate = (total_operations - failed_ops) / total_operations if total_operations else 0
    energy_per_op = energy_consumption / total_operations if total_operations else 0

    # Efficiency formula: combines success rate and penalizes high energy use
    raw_efficiency = base_success_rate * 100 - (energy_per_op * 0.5)

    # Apply unrelated time-based decay (distractor: no timestamps used meaningfully)
    time_decay = 1.0
    if len(log_entries) > 100:
        time_decay = 0.98
    adjusted_efficiency = raw_efficiency * time_decay

    # Final score with redundant clipping
    clipped_efficiency = max(0, min(adjusted_efficiency, 100))

    # Distractor: unused throughput calculation
    throughput = total_operations / (max(timestamp, 1) - log_entries[0]['ts']) if log_entries else 0

    # Key assignment point
    efficiency_score = int(correction_factor * clipped_efficiency)

    final_metrics = []
    final_metrics.append(efficiency_score)

    print(f"Result: {efficiency_score}")

# Simulated log data
log_data = [
    {'type': 'compute', 'success': True,  'power': 75, 'ts': t} for t in range(0, 50, 2)
] + [
    {'type': 'compute', 'success': False, 'power': 85, 'ts': t} for t in range(50, 60, 2)
] + [
    {'type': 'idle',    'success': True,  'power': 20, 'ts': t} for t in range(60, 70, 2)
]

calculate_system_efficiency(log_data)