def process_signal(samples, filter_threshold=0.5):
    # Irrelevant preprocessing
    normalized = [x / max(samples) for x in samples]
    filtered = [x for x in normalized if abs(x) > filter_threshold]
    
    # Distractor: unused transformation
    inverted = [1.0 / (1 + x) for x in normalized if x != -1]
    stats = {
        'peak': max(normalized, default=0),
        'truncated_mean': sum(normalized[1:-1]) / len(normalized[1:-1]) if len(normalized) > 2 else 0,
        'length': len(filtered)
    }

    # Real computation path begins here
    magnitude_classes = []
    for val in samples:
        if val < 10:
            magnitude_classes.append(1)
        elif val < 50:
            magnitude_classes.append(2)
        else:
            magnitude_classes.append(3)

    class_counts = {1: 0, 2: 0, 3: 0}
    for cls in magnitude_classes:
        class_counts[cls] += 1

    # Secondary distractor: dead function
    def analyze_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        total = len(data)
        return -sum((count/total) * log(count/total) for count in freq.values())

    # Unused entropy call
    _ = analyze_entropy(magnitude_classes)  # red herring

    # Key transformation: slice and shift
    shifted_classes = magnitude_classes[::2]  # take every other element
    shifted_classes = [(x << 1) for x in shifted_classes]  # bit shift left by 1

    # Introduce string-based distractor
    status_log = "event:START|action:scan|result:success"
    log_parts = status_log.split('|')
    log_dict = {part.split(':')[0]: part.split(':')[1] for part in log_parts}
    
    # More distraction: character counting in fixed string
    debug_chars = "diagnostics_running_v2"
    char_freq = {c: debug_chars.count(c) for c in set(debug_chars)}
    unique_chars = len(char_freq)

    # Begin relevant chain
    base_score = class_counts[3] * 100  # weight high-magnitude events
    adjustment = (class_counts[2] - class_counts[1]) * 10
    raw_diagnostic = base_score + adjustment

    # Simulate threshold filtering using string-derived condition (misleading)
    trigger_word = log_dict.get('action', '')
    if 'scan' in trigger_word:
        raw_diagnostic += 25  # minor boost, but not final

    # Actual key logic hidden among distractions
    critical_values = [raw_diagnostic]
    for i in range(len(shifted_classes)):
        if i % 2 == 0:
            critical_values[0] += shifted_classes[i]
        else:
            critical_values[0] -= shifted_classes[i] // 2

    # Final aggregation with decoy inputs
    def aggregate_results(results, limits):
        # Another layer of slicing
        window = results[-1:]  # just last element
        cap = sum(limits) * 0.7
        temp = window[0]
        
        # Decoy loop with early break
        for lim in limits:
            temp += lim // 5
            if temp > cap:
                break
                temp += 1000  # unreachable
        
        # Final adjustment based on string length
        flag = "ENABLE_OFFSET"[:4]  # "ENAB"
        if flag.lower().startswith('en'):
            temp -= len(debug_chars)  # subtract unique_chars was distractor

        return int(temp)

    thresholds = [10, 20, 30]
    diagnostics = [raw_diagnostic]
    final_diagnostic = aggregate_results(diagnostics, thresholds)

    print(f"Result: {final_diagnostic}")