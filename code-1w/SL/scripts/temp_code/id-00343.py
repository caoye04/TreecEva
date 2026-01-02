from collections import Counter, defaultdict

# Simulated system telemetry and user feedback processing
def collect_telemetry():
    raw_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    data_counter = Counter(raw_data)
    return data_counter

def generate_baseline():
    # Irrelevant computation - baseline for unused feature
    base = 1
    for i in range(5):
        base = (base * 2 + i) % 100
    temp_result = base ** 2  # Dead computation
    return base

def track_events():
    event_log = defaultdict(int)
    events = ['click', 'hover', 'click', 'scroll', 'click']
    for e in events:
        event_log[e] += 1
    # Misleading intermediate
    total_actions = sum(event_log.values())
    normalized = {k: v / total_actions for k, v in event_log.items()}
    return event_log

def validate_inputs(x, y):
    if x < 0 or y > 100:
        return False
    elif x == y:
        return True
    else:
        return x % 2 == 0

# Orchestration function with mixed concerns
def main_pipeline():
    # Step 1: Collect telemetry
    sensor_counts = collect_telemetry()
    
    # Step 2: Generate irrelevant baseline (distractor)
    dummy_base = generate_baseline()
    adjustment_factor = dummy_base * 0.75  # Not used later
    
    # Step 3: Track UI events (partially relevant)
    ui_events = track_events()
    click_count = ui_events['click']  # Relevant extraction
    hover_ratio = ui_events['hover'] / sum(ui_events.values()) if ui_events else 0  # Distractor
    
    # Step 4: Simulate feedback accumulation
    feedback_stream = ['good', 'bad', 'good', 'neutral', 'good', 'good']
    feedback_counter = Counter(feedback_stream)
    
    # Step 5: Build metrics log (mixed usage)
    metrics_log = {}
    metrics_log['positive'] = feedback_counter['good']
    metrics_log['negative'] = feedback_counter['bad']
    metrics_log['volume'] = len(feedback_stream)
    metrics_log['consistency'] = feedback_counter['good'] ** 2 - feedback_counter['bad']
    
    # Step 6: Hidden distractor chain
    temp_array = [i * 2 for i in range(6)]
    shifted = [(x >> 1) + 3 for x in temp_array]  # Bitwise distraction
    checksum = sum(shifted) % 97  # Unused security check
    
    # Step 7: Conditional override simulation (never triggers due to data)
    if validate_inputs(checksum, 42):
        metrics_log['consistency'] = 0  # Dead code path
    
    # Step 8: Core evaluation logic (answer derivation)
    def evaluate_performance(fb, log):
        pos = log['positive']
        neg = log['negative']
        vol = log['volume']
        base_score = (pos - neg) * 10
        if vol > 5:
            base_score += 5
        if fb['neutral'] > 0:
            base_score -= 2
        multiplier = 2 if fb['good'] >= 3 else 1
        final = base_score * multiplier
        return int(final)
    
    final_score = evaluate_performance(feedback_counter, metrics_log)
    
    # Step 9: Print result (required output format)
    print(f"Result: {final_score}")
    
    # Step 10: Additional red herring
    debug_trace = []
    for k, v in feedback_counter.items():
        debug_trace.append(f"{k}:{v}")
    trace_str = "|".join(debug_trace)  # Unused string op

    return final_score

if __name__ == "__main__":
    main_pipeline()