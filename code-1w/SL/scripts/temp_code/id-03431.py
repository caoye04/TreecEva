def analyze_workload(data, threshold=50):
    # Irrelevant transformation
    processed = [x ** 2 for x in data if x < threshold]
    temp_result = sum(processed) // len(processed) if processed else 0

    # Distractor: complex but unused logic
    def noise_function(x):
        return (x ^ 255) & 127 | (x >> 3)

    noise_data = [noise_function(d) for d in data[::2]]
    aggregate_noise = sum(noise_data) * 0.1

    # Red herring: dead code path
    if len(data) > 1000:
        return -999  # Never reached

    # Meaningful intermediate calculation
    valid_entries = list(filter(lambda x: x > 0, data))
    normalized = list(map(lambda x: round(x / max(valid_entries), 3), valid_entries))

    # Bitwise obfuscation of a simple count
    count_above = 0
    for val in data:
        if val > threshold:
            count_above += 1
    masked_count = count_above ^ 15 ^ 15  # XOR cancel-out (red herring)

    # Irrelevant string processing distraction
    status_flags = ['HIGH', 'MEDIUM', 'LOW']
    flag_summary = ''.join([s[0] for s in status_flags])  # 'HML'
    encoded_flag = hash(flag_summary) % 100

    # Unused recursive function (decoy)
    def recursive_distractor(n):
        if n <= 1:
            return 1
        return n * recursive_distractor(n - 2)

    # Actual relevant logic begins here — well hidden
    outlier_mask = set()
    for i, v in enumerate(data):
        if v > threshold * 1.8 or v < 5:
            outlier_mask.add(i)

    clean_data = [v for i, v in enumerate(data) if i not in outlier_mask]
    avg_clean = sum(clean_data) / len(clean_data) if clean_data else 0

    # Simulated performance metric with multiple steps
    metrics = {
        'efficiency': avg_clean * 0.7,
        'stability': abs(aggregate_noise - temp_result) * 0.01,  # Misleading use
        'consistency': len(normalized) - len(outlier_mask),
        'peak_utilization': max(data) if data else 0
    }

    baseline = {
        'efficiency': 42.0,
        'stability': 10.0,
        'consistency': 20,
        'peak_utilization': 100
    }

    def evaluate_performance(met, base):
        score = 0
        weights = {'efficiency': 0.4, 'stability': 0.1, 'consistency': 0.3, 'peak_utilization': 0.2}
        for key in met:
            if key == 'stability':
                # Inverted logic: lower stability deviation increases score
                deviation = abs(met[key] - base[key])
                score += (1 - min(deviation / 100.0, 0.95)) * weights[key] * 100
            else:
                ratio = met[key] / base[key] if base[key] > 0 else 0
                score += min(ratio, 1.2) * weights[key] * 100
        return int(score)

    final_score = evaluate_performance(metrics, baseline)
    
    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Input data (deterministic)
data_stream = [65, 70, 40, 90, 48, 52, 60, 85, 30, 95, 55, 68, 72, 45, 80]

# Call entry point
result = analyze_workload(data_stream)