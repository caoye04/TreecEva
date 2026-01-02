from collections import Counter

# Simulate data stream from sensor nodes
raw_data = 'IN,IN,OUT,IN,RESET,OUT,OUT,IN,IN,IN,OUT'
processed_events = raw_data.split(',')

# State tracking variables
current_state = 'active'
checkpoint_log = []
dummy_accumulator = 0

# Counters for flow analysis
inflow_counter = Counter()
outflow_counter = Counter()
transition_matrix = {'IN': 0, 'OUT': 0, 'RESET': 0}

for event in processed_events:
    # Irrelevant case transformation (distractor)
    normalized_event = event.lower()

    # Update transition matrix (semi-relevant, not used in final result)
    if event in transition_matrix:
        transition_matrix[event] += 1

    # Track inflows with additional logic
    if event == 'IN' and current_state == 'active':
        inflow_counter['in'] += 1
        dummy_accumulator += len(normalized_event)  # Distractor computation
    
    # Handle outflows
    if event == 'OUT':
        outflow_counter['out'] += 1
        if dummy_accumulator > 5:
            dummy_accumulator -= 2  # Misleading state adjustment

    # Simulate rare reset condition (dead code path - never triggers)
    if event == 'RESET':
        inflow_counter = Counter()  # This would reset but is blocked by logic
        current_state = 'inactive'

# Critical statement: compute net flow
dummy_calc = sum(inflow_counter.values()) * 0.5  # Distractor float computation
net_flow = inflow_counter['in'] - outflow_counter['out']

# Additional irrelevant slicing operation (meets language feature requirement)
event_snapshot = processed_events[2:8]
summary_tag = ''.join([e[0] for e in event_snapshot]).lower()

# Final output
print(f"Result: {net_flow}")