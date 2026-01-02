def aggregate_performance(entries, limits):
    # Preprocess: extract relevant numeric data from log entries
    parsed_values = [int(entry.split(':')[1]) for entry in entries if ':' in entry]
    
    # Irrelevant string processing (distractor)
    valid_labels = [entry.split(':')[0].strip() for entry in entries if len(entry.split(':')[0]) > 1]
    label_lengths = [len(label) for label in valid_labels]
    average_label_length = sum(label_lengths) / len(label_lengths) if label_lengths else 0

    # State tracking variables (some used, some not)
    performance_bins = {key: 0 for key in limits}
    cumulative_shift = 0
    temp_offset = 0  # Dead variable - not used in final logic

    # Bitwise weighting based on index (semi-relevant)
    for i, val in enumerate(parsed_values):
        if val >= limits['warning']:
            performance_bins['critical'] += val >> 2
        elif val >= limits['info']:
            shift_amount = i & 3  # Use index to modulate impact
            performance_bins['warning'] += val >> shift_amount
            cumulative_shift += shift_amount
        else:
            performance_bins['info'] += val | 1  # Minor bit flip

    # Secondary loop with zip and enumerate (moderate nesting)
    adjustments = []
    for idx, (raw, proc) in enumerate(zip(entries, parsed_values)):
        if 'error' in raw.lower():
            # Complex but partially redundant adjustment
            adj = proc * (idx % 2 + 1)
            if idx % 2 == 0:
                adj = adj ^ 5  # XOR for even indices
            adjustments.append(adj)

    # Final aggregation with misleading intermediate steps
    base_score = performance_bins['critical'] * 2 + performance_bins['warning']
    penalty = sum(adjustments) // len(adjustments) if adjustments else 0
    bonus = cumulative_shift * 3
    
    # Red herring calculation (never used)
    hypothetical_max = len(parsed_values) * max(limits.values())
    efficiency_ratio = base_score / hypothetical_max if hypothetical_max else 0

    # Actual final computation
    final_score = base_score + bonus - penalty
    return final_score


# Input data
log_data = [
    "sys:45", "net:error:62", "svc:30", "db:error:77", "cache:20",
    "api:88", "mon:15", "cfg:error:55"
]
thresholds = {
    'info': 25,
    'warning': 50,
    'critical': 75
}

# Execute
result = aggregate_performance(log_data, thresholds)
print(f"Target result: {result}")