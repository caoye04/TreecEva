def analyze_system_performance(raw_logs, min_duration):
    total_entries = len(raw_logs)
    valid_records = []
    temp_buffer = []
    duration_sum = 0
    outlier_count = 0

    for log in raw_logs:
        parts = log.split(',')
        try:
            duration = float(parts[2])
            category = parts[1]
            timestamp = parts[0]
        except (IndexError, ValueError):
            continue

        if duration < 0.1:
            outlier_count += 1
            continue

        duration_sum += duration
        
        if category == 'CRITICAL' and duration > min_duration:
            temp_buffer.append((timestamp, duration))
        elif category == 'INFO':
            pass  # Logging info suppressed
        else:
            valid_records.append(duration)

    average_duration = duration_sum / total_entries if total_entries else 0
    filtered_durations = [d for d in valid_records if d <= 3 * average_duration]

    processed_data = sorted(filtered_durations, reverse=True)

    def calculate_efficiency(data, limit):
        if not data:
            return 0.0
        peak_load = data[0] if data else 0
        steady_load = sum(data) / len(data)
        fluctuation = max(data) - min(data)
        compliance_ratio = sum(1 for x in data if x <= limit) / len(data)
        efficiency = (steady_load / (fluctuation + 1e-5)) * compliance_ratio
        return round(efficiency * 100, 4) if peak_load > 0 else 0.0

    threshold = 2.5
    baseline_check = [x for x in processed_data if x > 1.0]
    auxiliary_metric = len(baseline_check) / len(processed_data) if processed_data else 0
    scaling_factor = auxiliary_metric * 1.5 if auxiliary_metric > 0.5 else 1.0

    efficiency_score = calculate_efficiency(processed_data, threshold)
    efficiency_score *= scaling_factor  # Adjusted for stability

    debug_snapshot = {
        'entries_processed': total_entries,
        'outliers_removed': outlier_count,
        'average_duration': average_duration,
        'final_efficiency': efficiency_score
    }
    
    # Final output
    print(f"Result: {efficiency_score}")

# Simulated input data
dummy_logs = [
    "t0,A,0.5", "t1,B,1.2", "t2,CRITICAL,0.8", "t3,A,0.3", "t4,C,2.1",
    "t5,B,0.9", "t6,A,1.7", "t7,CRITICAL,3.3", "t8,C,0.4", "t9,B,1.1",
    "t10,A,2.4", "t11,C,0.2", "t12,B,1.6", "t13,A,0.7", "t14,CRITICAL,1.9"
]

analyze_system_performance(dummy_logs, 1.0)