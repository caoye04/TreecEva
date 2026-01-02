from collections import defaultdict

# Simulate system log with event counts and resource usage
def generate_log_data():
    logs = [
        {'type': 'read', 'size': 120, 'priority': 2},
        {'type': 'write', 'size': 85, 'priority': 4},
        {'type': 'read', 'size': 95, 'priority': 1},
        {'type': 'delete', 'size': 0, 'priority': 5},
        {'type': 'write', 'size': 200, 'priority': 3},
        {'type': 'read', 'size': 60, 'priority': 2}
    ]
    return logs

# Misleading function: appears useful but not used in final computation
def analyze_frequency(logs):
    freq = defaultdict(int)
    for entry in logs:
        freq[entry['type']] += 1
    return freq

# Auxiliary function to compute weighted load (not directly used but looks relevant)
def compute_weighted_load(logs):
    total_load = 0
    for entry in logs:
        # Weighted by priority and size
        total_load += entry['size'] * entry['priority']
    normalized = total_load / 100.0 if total_load > 0 else 0
    return normalized

# Core logic: calculate remaining system capacity after filtering critical ops
def calculate_remaining_capacity(log_entries, threshold):
    base_capacity = 1000
    usage_reserve = 0
    high_priority_count = 0

    # Track cumulative usage for non-delete operations above threshold priority
    for entry in log_entries:
        if entry['type'] != 'delete':
            adjusted_size = entry['size'] + 5  # minor adjustment
            if entry['priority'] >= threshold:
                usage_reserve += adjusted_size
                high_priority_count += 1  # tracked but only partially relevant

    # Red herring calculation: complex but unused
    average_priority = sum(e['priority'] for e in log_entries) / len(log_entries)
    fake_reduction = int(average_priority ** 2) if average_priority > 3 else 0

    # Actual capacity logic
    projected_usage = usage_reserve * 1.1  # 10% overhead
    remaining = base_capacity - projected_usage

    # Final adjustment based on presence of high-priority writes
    has_high_write = any(e['type'] == 'write' and e['priority'] >= 4 for e in log_entries)
    safety_buffer = 50 if has_high_write else 20
    final_capacity = remaining - safety_buffer

    return int(final_capacity)

# Execution flow
def main():
    raw_logs = generate_log_data()
    
    # Distractor: frequency analysis that isn't used
    type_freq = analyze_frequency(raw_logs)
    
    # Distractor: weight-based metric computed but ignored
    dummy_load = compute_weighted_load(raw_logs)
    
    # Key configuration
    system_threshold = 3
    
    # Critical execution point
    final_capacity = calculate_remaining_capacity(raw_logs, system_threshold)
    
    # Print result as required
    print(f"Result: {final_capacity}")

if __name__ == "__main__":
    main()