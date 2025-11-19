from collections import defaultdict

events = [
    {'type': 'request', 'amount': 10},
    {'type': 'request', 'amount': 25},
    {'type': 'utilization', 'level': 80},
    {'type': 'request', 'amount': 5},
    {'type': 'release', 'threshold': 30},
    {'type': 'utilization', 'level': 45}
]

state = 'reserve'
bandwidth_pool = 0
reservation_buffer = []
utilization_history = []

# State transition logic with short-circuit guards
for event in events:
    if state == 'reserve' and event['type'] == 'request':
        reservation_buffer.append(event['amount'])
        buffer_sum = sum(reservation_buffer)
        # Short-circuit: Only check balance condition if buffer is non-empty
        if reservation_buffer and buffer_sum >= 30:
            state = 'balance'
    elif state == 'reserve' and event['type'] == 'utilization':
        utilization_history.append(event['level'])
        # Short-circuit: Transition to release only if last two readings are low
        if len(utilization_history) >= 2 and utilization_history[-1] < 50 and utilization_history[-2] < 50:
            state = 'release'
    elif state == 'balance':
        # Greedy redistribution: allocate half of excess over 30
        excess = max(0, sum(reservation_buffer) - 30)
        bandwidth_pool += excess // 2
        reservation_buffer = [x for x in reservation_buffer if x > 0]  # Reset buffer
        state = 'reserve'
    elif state == 'release' and event['type'] == 'release':
        # Release policy: free up to threshold amount
        released = min(bandwidth_pool, event['threshold'])
        bandwidth_pool -= released
        state = 'reserve'

# Final aggregation using dictionary comprehension
metrics = {
    'pool': bandwidth_pool,
    'buffer_total': sum(reservation_buffer),
    'history_avg': sum(utilization_history) // len(utilization_history) if utilization_history else 0
}

# Merge with derived metrics
enhanced_metrics = {
    **metrics,
    **{k + '_scaled': v * 2 for k, v in metrics.items()}
}

# Compute final bandwidth using a lambda reduction
compute_final = lambda d: d['pool'] + d.get('buffer_total', 0) - d.get('history_avg', 0)
final_bandwidth = compute_final(enhanced_metrics)

print(f"Result: {final_bandwidth}")