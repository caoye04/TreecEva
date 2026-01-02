def analyze_events(raw_data, threshold_config):
    # Irrelevant preprocessing (distractor)
    normalized_data = [x * 1.05 for x in raw_data if x > 0]
    filtered_events = list(filter(lambda x: x < 1000, normalized_data))
    event_stats = {'count': len(filtered_events), 'sum': sum(filtered_events)}

    # Red herring computation
    temp_score = event_stats['count'] * 0.7 + event_stats['sum'] * 0.01
    adjustment_factor = 1.2 if temp_score > 50 else 0.8

    # Core logic disguised among distractions
    valid_entries = [x for x in raw_data if x >= threshold_config['base']]
    weighted_values = []
    for idx, val in enumerate(valid_entries):
        if idx % 2 == 0:
            weighted_values.append(val * 1.1)
        else:
            weighted_values.append(val * 0.9)

    # Decoy function call with unused result
    def compute_health_score(data):
        return sum(d ** 0.5 for d in data) / len(data) if data else 0
    
    health_diagnostic = compute_health_score(weighted_values)  # Unused

    # Tuple unpacking distraction
    (primary_cap, secondary_cap) = (max(weighted_values), min(weighted_values)) if weighted_values else (0, 0)
    capacity_ratio = primary_cap / secondary_cap if secondary_cap != 0 else 0

    # Real but hidden logic path
    clipped_values = [min(v, 300) for v in weighted_values]
    adjusted_total = sum(clipped_values)
    penalty = 0
    for v in clipped_values:
        if v > 250:
            penalty += v * 0.15

    net_yield = adjusted_total - penalty

    # Secondary irrelevant structure
    status_flags = []
    for v in clipped_values:
        status_flags.append('high' if v > 200 else 'normal')
    flag_distribution = {f: status_flags.count(f) for f in set(status_flags)}

    # Key control flow with conditional expression
    base_rating = net_yield / len(clipped_values) if clipped_values else 0
    final_diagnostic = int(base_rating + 0.5) if capacity_ratio > 1.5 else int(base_rating - 0.5)

    # Dead code path (never executed due to above condition)
    if capacity_ratio < 0.5:
        fallback_metric = sum(valid_entries) // (len(valid_entries) or 1)
        final_diagnostic = fallback_metric * 2

    return final_diagnostic


def process_metrics(entries, threshold):
    # String manipulation distraction
    log_header = "SYS_LOG_V2"
    header_valid = log_header.startswith("SYS") and len(log_header) == 9
    
    # List comprehension with filtering
    clean_entries = [int(x.strip().split()[0]) for x in entries if x.strip().isdigit() or (x.strip().isdigit() and len(x) < 6)]
    
    # Another decoy transformation
    reversed_checksum = sum(int(str(c)[::-1]) for c in clean_entries if len(str(c)) > 1)
    
    # Forward the real work
    result = analyze_events(clean_entries, {'base': threshold})
    return result

# Simulated input data (real signal embedded in noise)
log_entries = [
    "  95 ", "not_a_number", "120", "abc123", "150", "", "210", "305", "  88  ",
    "invalid", "260", "190", "  0  ", "400", "110"
]
system_threshold = 90

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Result: {final_diagnostic}")