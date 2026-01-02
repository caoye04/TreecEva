from itertools import compress

# Simulate daily system load analysis across multiple servers
def analyze_workload(log_entries):
    base_load = 0
    temp_adjustments = []
    usage_levels = []
    
    for entry in log_entries:
        parts = entry.split('|')
        timestamp = parts[0]
        server_id = parts[1]
        load = int(parts[2])
        temperature = float(parts[3])

        # Irrelevant environmental adjustment (distractor)
        adjusted_temp = temperature - 27.5
        if adjusted_temp > 5:
            temp_adjustments.append(adjusted_temp * 1.2)
        else:
            temp_adjustments.append(0)

        # Core logic: accumulate normalized usage
        hour = int(timestamp.split(':')[0])
        normalized_load = load * (1 + (hour // 6) * 0.1)  # Load increases by 10% per 6-hour block
        
        # Conditional expression with lambda filtering (required python feature)
        is_peak_hour = (lambda h: True if h in [8, 9, 10, 18, 19, 20] else False)(hour)
        boosted_load = normalized_load * 1.3 if is_peak_hour else normalized_load
        
        usage_levels.append(boosted_load)
        
        # Dead code path - never executed due to structure (distractor)
        if server_id == "S999":
            base_load += 100  # unreachable in current data

    # Secondary processing with compress (itertools)
    valid_hours = [int(e.split('|')[0].split(':')[0]) in range(6, 22) for e in log_entries]
    filtered_usage = list(compress(usage_levels, valid_hours))

    # Key statement
    peak_capacity = max(usage_levels)

    # Extra unrelated aggregation (distraction)
    avg_temp_adj = sum(temp_adjustments) / len(temp_adjustments) if temp_adjustments else 0
    phantom_score = sum(filtered_usage) * avg_temp_adj * 0.01

    # Output required result
    print(f"Result: {peak_capacity}")

    return peak_capacity

# Input data
logs = [
    "08:15|S001|450|32.1",
    "14:22|S002|320|30.5",
    "20:05|S003|510|33.8",
    "06:45|S001|280|28.9",
    "19:10|S002|490|31.7"
]

result = analyze_workload(logs)