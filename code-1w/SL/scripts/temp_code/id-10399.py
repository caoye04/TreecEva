from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic validation
def analyze_sensor_readings(log_entries):
    event_timeline = defaultdict(list)
    fault_flags = set()
    cumulative_power = 0
    transient_buffer = []
    baseline_offset = 0.0

    for timestamp, events in log_entries:
        sorted_events = sorted(events, key=lambda x: x['priority'])
        high_priority_count = 0

        # Irrelevant sorting and counting (distractor)
        for event in sorted_events:
            if event['type'] == 'POWER_SURGE':
                transient_buffer.append(event['value'])
            elif event['type'] == 'TEMP_WARNING':
                event_timeline[timestamp].append(event)

        # Real logic begins: count critical faults
        critical_faults = [e for e in events if e['diagnostic'] == 'CRITICAL']
        if len(critical_faults) > 1:
            fault_flags.add(timestamp)

        # Accumulate power usage only for specific condition
        for event in events:
            if event['type'] == 'POWER_DRAW' and event['source'] == 'MAIN_BUS':
                cumulative_power += event['value']

        # Red herring: modifies a variable but not used later
        baseline_offset += len(events) * 0.05

        # Another decoy accumulation
        high_priority_count = sum(1 for e in events if e['priority'] == 1)
        if high_priority_count > 2:
            transient_buffer.extend([1] * high_priority_count)

    # Secondary analysis: frequency of fault timestamps
    timeline_counter = Counter(event_timeline.keys())
    fault_duration = len(fault_flags)

    # Distractor: complex but unused data transformation
    zipped_analysis = list(zip(
        [x for x in range(len(transient_buffer))],
        enumerate(transient_buffer)
    ))

    # Core calculation chain (interleaved with noise)
    base_diagnostic = cumulative_power * 2.5
    adjustment_factor = 0
    if fault_duration > 0:
        adjustment_factor = 100 // fault_duration if fault_duration else 0

    # Decoy conditional block (never reached due to logic above)
    redundant_check = False
    if baseline_offset > 1000:
        for item in zipped_analysis:
            if item[1][1] > 50:
                redundant_check = True

    # Key computational path
    aggregate_score = base_diagnostic - (adjustment_factor * 15)

    # More irrelevant operations
    phantom_map = {i: val for i, val in enumerate(['A','B','C'])}
    temp_set = {x for x in range(5)}
    temp_set.union({6,7,8})  # Dead operation

    # Correction based on event distribution
    event_kinds = [e['type'] for sublist in log_entries for e in sublist[1]]
    kind_counts = Counter(event_kinds)
    dominant_type = kind_counts.most_common(1)[0][1] if kind_counts else 0

    correction_factor = 0
    if dominant_type > 3:
        correction_factor = 42

    final_diagnostic = aggregate_score + correction_factor
    return final_diagnostic

# Input data
log_data = [
    (1001, [
        {'type': 'POWER_DRAW', 'source': 'MAIN_BUS', 'value': 120, 'priority': 3, 'diagnostic': 'OK'},
        {'type': 'TEMP_WARNING', 'value': 75, 'priority': 2, 'diagnostic': 'OK'}
    ]),
    (1002, [
        {'type': 'POWER_DRAW', 'source': 'MAIN_BUS', 'value': 150, 'priority': 1, 'diagnostic': 'CRITICAL'},
        {'type': 'POWER_SURGE', 'value': 220, 'priority': 1, 'diagnostic': 'CRITICAL'},
        {'type': 'TEMP_WARNING', 'value': 80, 'priority': 3, 'diagnostic': 'OK'}
    ]),
    (1003, [
        {'type': 'POWER_DRAW', 'source': 'MAIN_BUS', 'value': 130, 'priority': 2, 'diagnostic': 'OK'},
        {'type': 'COMM_ERROR', 'value': 0, 'priority': 1, 'diagnostic': 'OK'}
    ]),
    (1004, [
        {'type': 'POWER_DRAW', 'source': 'MAIN_BUS', 'value': 110, 'priority': 3, 'diagnostic': 'CRITICAL'},
        {'type': 'POWER_DRAW', 'source': 'BACKUP', 'value': 60, 'priority': 2, 'diagnostic': 'OK'}
    ])
]

result = analyze_sensor_readings(log_data)
print(f"Result: {result}")