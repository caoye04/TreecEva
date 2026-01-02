from collections import defaultdict
import itertools

# Simulate hourly resource allocation across departments
hours = list(range(24))
departments = ['dev', 'ops', 'qa', 'security']

# Initialize trackers
allocation_log = defaultdict(lambda: [0] * 24)
usage_tracker = defaultdict(int)
flagged_anomalies = []  # Distractor: not used in final result

# Base load profile with periodic spikes
base_load = [30 + 10 * (h // 6) for h in hours]
spike_mask = [int(h % 8 == 0) for h in hours]

# Simulate department-specific usage patterns
for dept in departments:
    shift_offset = hash(dept) % 4  # Randomize start
    for h in hours:
        hour_idx = (h + shift_offset) % 24
        base_amount = base_load[hour_idx]
        spike_bonus = 15 * spike_mask[hour_idx] * (hash(dept + str(h)) % 3)
        filtered_bonus = spike_bonus if spike_bonus > 20 else 0  # Semi-relevant filtering
        
        # Apply department scaling
        if dept == 'dev':
            scale = 1.8
        elif dept == 'ops':
            scale = 1.5
        else:
            scale = 1.2
            
        final_allocation = int((base_amount + filtered_bonus) * scale)
        allocation_log[dept][hour_idx] += final_allocation

        # Track total usage per hour (key computation)
        usage_tracker[hour_idx] += final_allocation

        # Dead code path - distractor
        if final_allocation > 1000:
            flagged_anomalies.append((dept, hour_idx, final_allocation))

# Additional irrelevant aggregation
summary_stats = {
    'total_allocated': sum(sum(allocation_log[d]) for d in departments),
    'peak_per_dept': {d: max(allocation_log[d]) for d in departments},
    'utilization_entropy': 0.0  # Placeholder, unused
}

# Compute entropy (irrelevant to answer)
counts = list(summary_stats['peak_per_dept'].values())
total = sum(counts)
if total > 0:
    entropy = sum((c / total) * (c / total) for c in counts)
    summary_stats['utilization_entropy'] = round(entropy, 4)

# Critical statement: determine peak system capacity requirement
peak_capacity = max(usage_tracker.values())

# Print result for evaluation
print(f"Result: {peak_capacity}")