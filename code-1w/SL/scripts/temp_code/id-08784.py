def analyze_user_behavior(raw_data, threshold=0.5):
    # Irrelevant preprocessing (distractor)
    clean_data = [x.strip().lower() for x in raw_data if len(x) > 2]
    temp_stats = {'length': len(clean_data), 'chars': sum(len(s) for s in clean_data)}

    # Misleading transformation chain (red herring)
    encoded = []
    for entry in clean_data:
        transformed = ''.join(chr((ord(c) + 3) % 97 + 32) for c in entry if c.isalpha())
        encoded.append(transformed)

    # Dead code path - never used (distractor)
    def legacy_calculate(x):
        return (x ** 2 + 1) / (x + 0.1)

    metadata_summary = []
    for i, item in enumerate(encoded):
        if i % 2 == 0:
            metadata_summary.append(len(item))

    # Relevant logic begins: parse log entries with time decay
    log_entries = []
    for line in raw_data:
        parts = line.split(',')
        if len(parts) >= 3:
            try:
                timestamp = float(parts[0])
                action_type = parts[1].strip()
                confidence = float(parts[2].strip())
                log_entries.append((timestamp, action_type, confidence))
            except ValueError:
                continue

    # Time-weighted filtering (actual relevant logic)
    current_time = max([entry[0] for entry in log_entries]) if log_entries else 1.0
    recent_entries = [e for e in log_entries if current_time - e[0] <= 3600]

    # Decoy statistical calculation (misleading intermediate)
    avg_confidence = sum(e[2] for e in recent_entries) / len(recent_entries) if recent_entries else 0
    spike_count = sum(1 for e in recent_entries if e[2] > 0.8)

    # Complex conditional aggregation with string pattern matching (core logic)
    action_weights = {}
    for ts, act, conf in recent_entries:
        time_decay = 0.1 + 0.9 * (1 - (current_time - ts) / 3600)
        base_weight = conf * time_decay

        # String-based routing with slicing (required feature)
        key_prefix = act[:3].upper() if len(act) >= 3 else 'UNK'
        
        if key_prefix == 'CLK':
            action_weights['click'] = action_weights.get('click', 0) + base_weight * 1.2
        elif key_prefix == 'NAV':
            action_weights['navigation'] = action_weights.get('navigation', 0) + base_weight * 0.8
        elif key_prefix == 'SCN':
            action_weights['scan'] = action_weights.get('scan', 0) + base_weight * 1.5

    # Multiple assignment and tuple unpacking (required concept)
    click_score, nav_score, scan_score = (
        action_weights.get('click', 0),
        action_weights.get('navigation', 0),
        action_weights.get('scan', 0)
    )

    # Composite scoring with logical conditions and min/max (required paradigm)
    completeness = min(click_score, nav_score, scan_score) if all([click_score, nav_score, scan_score]) else 0
    balance_factor = 1.0 if abs(click_score - nav_score) < 0.5 and abs(nav_score - scan_score) < 0.7 else 0.6

    # Critical distractor: unused complex structure (dead data path)
    class PerformanceNode:
        def __init__(self, name, val):
            self.name = name
            self.value = val
            self.children = []

    root_node = PerformanceNode('root', completeness * 100)

    # Final aggregation function (key statement)
    def aggregate_performance(entries, user_threshold):
        raw_total = sum(w for _, _, w in entries)
        weighted_total = (click_score * 1.1) + (nav_score * 0.9) + (scan_score * 1.3)
        penalty = 10 * (1 - balance_factor)  # Poor balance reduces score
        adjustment = 5 if len([e for e in entries if e[1].startswith('CLK')]) > 2 else -2
        return int((weighted_total * balance_factor) + adjustment - penalty)

    final_score = aggregate_performance(log_entries, user_threshold)
    
    # Distractor output (never printed)
    debug_info = {"temp": temp_stats, "spikes": spike_count, "avg": round(avg_confidence, 3)}
    
    # Correct output
    print(f"Result: {final_score}")

# Simulated input data
input_logs = [
    "1678886400,CLK-start,0.91",
    "1678886460,NAV-menu,0.45",
    "1678886520,SCN-header,0.67",
    "1678886580,CLK-submit,0.93",
    "1678886640,NAV-back,0.51",
    "1678886700,SCN-footer,0.73",
    "1678886760,CLK-confirm,0.88",
    "1678886820,NAV-home,0.61"
]

# Execute main logic
analyze_user_behavior(input_logs, threshold=0.6)