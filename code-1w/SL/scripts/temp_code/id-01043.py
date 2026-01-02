def analyze_system_load(raw_logs, config_profile):
    # Irrelevant preprocessing (distractor)
    clean_logs = [line.strip() for line in raw_logs if line.strip()]
    filtered_entries = []
    temp_buffer = []
    for entry in clean_logs:
        if 'ERROR' in entry or 'WARNING' in entry:
            temp_buffer.append(entry)

    # Real data transformation path
    log_data = []
    for line in raw_logs:
        parts = line.split(',')
        if len(parts) == 4 and parts[2].isdigit():
            timestamp, component, load_val, status = parts
            load_int = int(load_val)
            log_data.append((timestamp, component, load_int, status))

    # Dead code path - never executed due to above filter logic
    if False:
        aggregated = {}
        for item in temp_buffer:
            key = item.split()[0]
            aggregated[key] = aggregated.get(key, 0) + 1

    # Misleading metric calculation (looks important but unused)
    avg_temp_load = sum([item[2] for item in log_data]) / max(len(log_data), 1) if log_data else 0
    peak_spike = max([item[2] for item in log_data if item[3] == 'ACTIVE'], default=0)

    # Actual relevant structure
    categorized = {'CPU': [], 'MEM': [], 'DISK': []}
    for _, comp, val, stat in log_data:
        if comp in categorized:
            categorized[comp].append(val)

    return categorized


def compute_health_score(dataset, weights):
    score = 0.0
    for key, values in dataset.items():
        if values:
            base = sum(values) / len(values)
            if key == 'CPU':
                score += base * weights['cpu_factor']
            elif key == 'MEM':
                score += base * weights['mem_factor']
            elif key == 'DISK':
                score += base * weights['disk_factor']
    return score


def validate_checksum(entries):
    # Unused validation function (decoy)
    total = 0
    for idx, item in enumerate(entries):
        total += idx * len(item)
    return total % 17


def process_metrics(metrics_dict, thresholds):
    diagnostic_code = 0
    anomaly_count = 0

    # Use enumerate and zip (required Python features)
    for idx, (component, readings) in enumerate(metrics_dict.items()):
        if not readings:
            continue
        high_readings = [r for r in readings if r > thresholds[idx % len(thresholds)]]
        anomaly_count += len(high_readings)

        # Complex conditional branch with red herring
        temp_flag = False
        for val in readings:
            if val > 95 and component == 'CPU':
                temp_flag = True
        if temp_flag:
            diagnostic_code |= (1 << idx)

    # Linear search through dictionary items (relevant step)
    components = list(metrics_dict.keys())
    for i in range(len(components)):
        comp = components[i]
        data = metrics_dict[comp]
        if data and max(data) > 100:
            diagnostic_code += i * 10

    # Final computation using distractor-influenced path
    adjustment = 0
    all_values = [v for vals in metrics_dict.values() for v in vals]
    for pos, val in enumerate(all_values):
        if val % 13 == 0 and pos % 4 == 0:
            adjustment += 1  # Minor influence

    final_diagnostic = diagnostic_code * 100 + anomaly_count + adjustment
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    logs = [
        '10:01,CPU,85,ACTIVE',
        '10:02,MEM,92,IDLE',
        '10:03,DISK,70,ACTIVE',
        '10:04,CPU,96,ACTIVE',
        '10:05,MEM,88,ACTIVE',
        '10:06,CPU,105,ACTIVE',
        '10:07,DISK,60,IDLE'
    ]

    # Thresholds for detection
    system_thresholds = [90, 85, 65]

    # Irrelevant configuration map (distractor)
    system_config = {
        'version': '2.1.0',
        'mode': 'production',
        'debug_level': 3,
        'max_retries': 5
    }

    # Key processing steps
    parsed_data = analyze_system_load(logs, system_config)
    health_score = compute_health_score(parsed_data, {'cpu_factor': 1.2, 'mem_factor': 0.9, 'disk_factor': 0.7})
    checksum = validate_checksum(logs)  # Computed but not used

    final_diagnostic = process_metrics(parsed_data, system_thresholds)
    print(f"Result: {final_diagnostic}")