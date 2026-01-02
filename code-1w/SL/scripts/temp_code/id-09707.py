def analyze_system_load(usage_log):
    # Irrelevant transformation: converts timestamps but not used later
    time_segments = [entry['time'] // 100 for entry in usage_log if 'time' in entry]
    temp_analysis = {ts: time_segments.count(ts) for ts in set(time_segments)}

    # Distractor: complex-looking but unused statistical calculation
    avg_time = sum(time_segments) / len(time_segments) if time_segments else 0
    variance_proxy = sum((t - avg_time) ** 2 for t in time_segments) / len(time_segments) if time_segments else 0

    # Real data extraction (relevant)
    cpu_readings = [entry['cpu'] for entry in usage_log if entry.get('type') == 'system']
    mem_readings = [entry['mem'] for entry in usage_log if entry.get('type') == 'system']

    # Dead code path — looks important but never called
    def deprecated_normalize(data):
        m = min(data)
        return [(x - m) / (max(data) - m) for x in data]

    # Actual processing: only this part matters
    filtered_cpu = [c for c in cpu_readings if c > 50]
    high_load_count = len(filtered_cpu)
    total_mem = sum(mem_readings)

    # Secondary distraction: bit manipulation with no downstream effect
    magic_flag = 0b101010
    for val in cpu_readings[:3]:
        magic_flag ^= (val & 0b1111) << 2
        magic_flag |= (magic_flag >> 3) & 0b111

    # Real metric computation begins here
    safety_margin = 100 - max(cpu_readings) if cpu_readings else 100
    instability_factor = abs(cpu_readings[-1] - cpu_readings[0]) if len(cpu_readings) > 1 else 0

    # Create derived metrics using dictionary operations and slicing
    metrics = {
        'load_count': high_load_count,
        'total_memory': total_mem,
        'stability': 100 - instability_factor,
        'headroom': safety_margin
    }

    # Weight assignment via lambda (not used directly, but influences real logic)
    weight_func = lambda x: 0.1 if x < 10 else (0.25 if x < 50 else 0.4)
    weights = {
        'load_count': 0.3,
        'total_memory': 0.1,
        'stability': weight_func(instability_factor),  # dynamic weight
        'headroom': 0.35
    }

    # Decoy scoring (never executed due to condition)
    if False:
        dummy_score = 0
        for k in metrics:
            dummy_score += metrics[k] * (weights[k] + 0.1)

    # Actual evaluation function (uses dictionary and lambda indirectly)
    def evaluate_performance(metrs, wghts):
        base = 0.0
        for key in metrs:
            if key in wghts:
                base += metrs[key] * wghts[key]
        bonus = 5 if metrs['stability'] > 85 and metrs['headroom'] > 20 else 0
        penalty = 10 if metrs['load_count'] > 8 else 0
        return int(base + bonus - penalty)

    final_score = evaluate_performance(metrics, weights)

    # Output result as required
    print(f"Result: {final_score}")

    # Unused complex structure: red herring involving case conversion and slicing
    raw_tags = ["ERR", "WARN", "INFO"]
    processed_tags = [tag.lower()[::-1] for tag in raw_tags]  # reversed lowercase: 'rre', 'nrAw', 'ofni'
    tag_frequency = {tag: processed_tags.count(tag) for tag in processed_tags}

    return final_score

# Input data
log_data = [
    {'time': 1200, 'cpu': 60, 'mem': 320, 'type': 'system'},
    {'time': 1210, 'cpu': 75, 'mem': 340, 'type': 'system'},
    {'time': 1220, 'cpu': 55, 'mem': 360, 'type': 'system'},
    {'time': 1230, 'cpu': 85, 'mem': 380, 'type': 'system'},
    {'time': 1240, 'cpu': 90, 'mem': 400, 'type': 'system'},
    {'time': 1250, 'cpu': 45, 'mem': 420, 'type': 'system'},
    {'time': 1260, 'cpu': 65, 'mem': 440, 'type': 'system'},
    {'time': 1270, 'cpu': 70, 'mem': 460, 'type': 'system'},
    {'time': 1280, 'cpu': 50, 'mem': 480, 'type': 'system'},
    {'time': 1290, 'cpu': 80, 'mem': 500, 'type': 'system'}
]

analyze_system_load(log_data)