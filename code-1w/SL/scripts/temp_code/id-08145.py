from itertools import compress, cycle

# Simulate a manufacturing process optimization task
def analyze_process_stages(stages):
    stage_flags = [s % 2 == 0 for s in stages]
    weights = [1.5 if s > 5 else 0.8 for s in stages]
    adjusted = [s * w for s, w in zip(stages, weights)]
    return adjusted, stage_flags

# Helper to simulate resource allocation drift
def compute_drift(values):
    drift = 0
    for i in range(len(values)):
        if i % 3 == 0:
            drift += values[i] * 0.1
        elif i % 3 == 1:
            drift -= values[i] * 0.05
    return abs(drift)

# Core efficiency calculation
def calculate_efficiency(chain, overhead):
    base = sum(x ** 0.5 for x in chain if x > 0)
    penalty = overhead * 0.75 if overhead > 10 else overhead * 0.3
    return int(base - penalty)

# Main simulation
process_ids = [3, 6, 9, 4, 7, 12, 5]
process_chain = [x + 2 for x in process_ids if x % 2 == 1]

# Irrelevant tracking of failed stages (distractor)
failed_stages = list(compress(process_ids, [x < 5 for x in process_ids]))
stage_cycle = cycle([1, 0])
dummy_mask = [next(stage_cycle) for _ in range(10)]

# Simulate intermediate diagnostics (semi-relevant)
diagnostics, flags = analyze_process_stages(process_chain)
diagnostic_sum = sum(d for d in diagnostics if d > 4)

# Noise injection: resource drift (irrelevant to final answer)
resource_pool = [2.1, 3.4, 1.2, 5.6]
drift_correction = compute_drift(resource_pool)
adjusted_diagnostics = [d - drift_correction for d in diagnostics]

# Key overhead computation from filtered data
active_count = len([f for f in flags if f])
overhead = active_count * 3 + len(process_chain)

# Critical statement
efficiency_score = calculate_efficiency(process_chain, overhead)

# Dead code path (dead branch - distractor)
if False:
    backup_chain = process_chain[::-1]
    efficiency_score = calculate_efficiency(backup_chain, 0)

# Print final result as required
print(f"Result: {efficiency_score}")