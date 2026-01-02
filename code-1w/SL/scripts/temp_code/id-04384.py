from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_logs = [
    {'node': 'A', 'status': 'active', 'load': 0.65, 'errors': 2},
    {'node': 'B', 'status': 'standby', 'load': 0.3, 'errors': 0},
    {'node': 'C', 'status': 'active', 'load': 0.88, 'errors': 5},
    {'node': 'D', 'status': 'active', 'load': 0.72, 'errors': 1},
    {'node': 'E', 'status': 'standby', 'load': 0.2, 'errors': 0}
]

# Irrelevant utility function (dead code path)
def normalize(value, min_val=0, max_val=1):
    return (value - min_val) / (max_val - min_val)

# Misleading transformation (not used in final calculation)
transformed = [normalize(log['load'], 0, 1) for log in telemetry_logs]

# Aggregate node statuses
status_count = defaultdict(int)
for log in telemetry_logs:
    status_count[log['status']] += 1

# Compute error distribution (distractor)
error_dist = Counter([log['errors'] for log in telemetry_logs if log['status'] == 'active'])

# Auxiliary computation: active node load sum (red herring)
total_active_load = sum(log['load'] for log in telemetry_logs if log['status'] == 'active')

# Weighted metric initialization (some weights are decoys)
weights = {
    'performance': 0.5,
    'reliability': 0.3,
    'scalability': 0.1,  # unused in final formula
    'efficiency': 0.1     # unused
}

# Raw metrics extraction
metrics = {}
metrics['performance'] = sum(log['load'] for log in telemetry_logs if log['status'] == 'active')
metrics['reliability'] = 10 - sum(log['errors'] for log in telemetry_logs)  # max penalty: 10

# Fake fusion logic (never called)
def fuse_metrics_wrong(m1, m2):
    return (m1 * m2) ** 0.5

# Actual evaluation logic
def evaluate_performance(m, w):
    # Intermediate distraction: sorting irrelevant keys
    sorted_keys = sorted(w.keys())
    score = 0
    
    # Only use 'performance' and 'reliability' despite more weights existing
    for key in sorted_keys:
        if key == 'performance':
            score += m['performance'] * w['performance']
        elif key == 'reliability':
            score += m['reliability'] * w['reliability']
        # Other keys ignored intentionally
    
    # Additional distraction: bitwise adjustment (has no effect due to masking)
    magic_offset = (len(telemetry_logs) << 2) & 7  # evaluates to 4 << 2 = 16 & 7 = 0
    
    # Final nonlinear scaling
    return (score ** 1.1) + magic_offset

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")