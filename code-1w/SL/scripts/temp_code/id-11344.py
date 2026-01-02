def analyze_user_behavior(raw_data, threshold=5):
    # Irrelevant preprocessing (distractor)
    temp_buffer = [x.strip() for x in raw_data if x.strip()]
    filtered_data = []
    for entry in temp_buffer:
        if 'ERROR' not in entry and 'DEBUG' not in entry:
            filtered_data.append(entry.lower())

    # Real processing begins: parse log entries
    log_entries = []
    for line in filtered_data:
        parts = line.split('|')
        if len(parts) >= 3:
            timestamp, action, details = parts[0], parts[1], parts[2]
            log_entries.append({
                'time': int(timestamp[-6:]) % 86400,
                'action': action.strip(),
                'length': len(details.strip())
            })

    # Decoy analysis function (never called)
    def compute_entropy(data):
        from math import log
        freq = {}
        total = 0
        for c in ''.join(data):
            freq[c] = freq.get(c, 0) + 1
            total += 1
        entropy = 0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p, 2)
        return entropy

    # Unused data transformation (red herring)
    reversed_logs = [{'rev_action': act[::-1]} for act in [le['action'] for le in log_entries]]
    aggregated_stats = {"max_time": 0, "total_actions": 0}
    time_buckets = {}
    for le in log_entries:
        bucket = le['time'] // 3600
        time_buckets[bucket] = time_buckets.get(bucket, 0) + 1
        aggregated_stats["total_actions"] += 1
        if le['time'] > aggregated_stats["max_time"]:
            aggregated_stats["max_time"] = le['time']

    # Real logic buried here — character counting and filtering
    critical_events = []
    for le in log_entries:
        if le['length'] > threshold * 2 and 'click' in le['action']:
            critical_events.append(le)

    # Bit manipulation decoy (unused)
    def scramble_value(x):
        return ((x << 3) & 0xFF) ^ 0xAA

    # Dictionary and set operations mixed with real and fake logic
    unique_actions = set()
    action_counter = {}
    for le in log_entries:
        act = le['action']
        unique_actions.add(act)
        action_counter[act] = action_counter.get(act, 0) + 1

    frequent_actions = {k for k, v in action_counter.items() if v > threshold}

    # Core calculation path
    base_score = 0
    for event in critical_events:
        base_score += event['length'] // 2
        if event['time'] % 7 == 0:
            base_score -= 1

    adjustment_factor = len(frequent_actions) if frequent_actions else 1

    # Secondary irrelevant transform
    shadow_map = {i: val for i, val in enumerate(sorted(time_buckets.values()))}
    median_bucket_usage = 0
    if shadow_map:
        mid_idx = len(shadow_map) // 2
        median_bucket_usage = shadow_map[mid_idx]

    # Final scoring uses only selected components
    stability_offset = len(unique_actions) - len(log_entries) // 4
    final_score = base_score * adjustment_factor + stability_offset

    # Dead code branch (never executed)
    if False:
        final_score = int(scramble_value(final_score))

    # Output target result
    print(f"Result: {final_score}")

    return final_score


# Simulated input data
simulated_logs = [
    "123456|view  |Product page load",
    "123457|click |Add to cart successful",
    "123458|hover |Tooltip shown",
    "123459|click |Proceed to checkout",
    "123460|input |Entered shipping info",
    "123461|click |Confirmed purchase",
    "123462|nav   |Back to homepage",
    "123463|click |Promo banner click",
    "123464|click |User profile access",
    "123465|click |Settings updated"
]

user_threshold = 3

# Key execution point
final_score = evaluate_performance(simulated_logs, user_threshold)

# Renaming confusion: define correct function after usage (but we fix reference)
def evaluate_performance(data, thresh):
    return analyze_user_behavior(data, thresh)
