from itertools import groupby

# Simulate inventory transfer log with timestamps and amounts
event_log = [
    (1, 'IN', 150),
    (2, 'OUT', 75),
    (3, 'IN', 200),
    (4, 'IN', 50),
    (5, 'OUT', 125)
]

# Irrelevant metadata (minimal distraction)
timestamp_labels = ['t0', 't1', 't2', 't3', 't4']
status_flags = [True, False, True]

# Key processing function
def process_transfers(logs, multiplier=1.0):
    # Group consecutive events by type using itertools.groupby
    sorted_logs = sorted(logs, key=lambda x: x[1])
    grouped = {k: list(v) for k, v in groupby(sorted_logs, key=lambda x: x[1])}
    
    inbound_total = sum(entry[2] for entry in grouped.get('IN', []))
    outbound_total = sum(entry[2] for entry in grouped.get('OUT', []))
    
    # Apply multiplier to net flow (e.g., unit conversion or batch scaling)
    net_flow = (inbound_total - outbound_total) * multiplier
    return int(net_flow)

# Secondary tracking variable (not used in final result)
cumulative_volume = sum(entry[2] for entry in event_log)

adjustment_factor = 1.2
log_entries = event_log

# Core computation
final_audit = process_transfers(log_entries, adjustment_factor)

# Determine inventory balance based on audit result
inventory_balance = final_audit + 10  # Base restocking bonus

# Output result as required
print(f"Target result: {inventory_balance}")