from collections import defaultdict, Counter
import itertools

# System telemetry simulation for distributed task execution
node_statuses = ['active', 'standby', 'active', 'failed', 'active', 'failed', 'standby', 'active']
timing_log = [127, 153, 112, 205, 98, 134, 167, 103]
failure_flags = [False, True, False, True, False, True, False, False]
resource_caps = {'cpu': 92, 'memory_mb': 4096, 'disk_iops': 220}

# Irrelevant baseline metrics (distractor)
baseline_avg = sum([110, 120, 130, 140, 150]) / 5
scaling_factor = 1.08
offset_correction = -5

# Simulated node metadata (mostly unused)
node_metadata = {
    i: {
        'id': f'N-{i:03d}',
        'region': ['us-east', 'eu-west', 'ap-south'][i % 3],
        'version': (1, i % 4 + 1, 7),
        'uptime_days': (i + 1) * 12
    } for i in range(len(node_statuses))
}

# Dead code path: version compatibility check (never called)
def check_compatibility(ver):
    major, minor, patch = ver
    return minor >= 2 and patch > 5

# Unused diagnostic accumulator (red herring)
diagnostic_trace = defaultdict(int)
for idx, status in enumerate(node_statuses):
    if status == 'failed':
        diagnostic_trace['fail_count'] += 1
    elif status == 'standby':
        diagnostic_trace['standby_time'] += timing_log[idx]

# Spurious transformation chain (distractor block)
processed_times = []
for t in timing_log:
    adjusted = t * scaling_factor + offset_correction
    if adjusted > 150:
        processed_times.append(150)
    else:
        processed_times.append(adjusted)

# Decoy function: computes irrelevant health score (not used in final result)
def compute_health_score(status_list, thresholds):
    count = Counter(status_list)
    score = 0
    score += count['active'] * thresholds.get('active_weight', 1.0)
    score -= count['failed'] * thresholds.get('penalty', 2.0)
    return round(score, 2)

health_params = {'active_weight': 1.2, 'penalty': 2.5}
spurious_health = compute_health_score(node_statuses, health_params)  # Dead end

# Real computation begins here — conditional filtering based on failure flags
effective_durations = [
    t for i, t in enumerate(timing_log)
    if not failure_flags[i]  # Only use non-failed nodes
]

# Group durations by parity of index (artificial grouping, but used later)
even_group = [t for i, t in enumerate(effective_durations) if (i % 2) == 0]
odd_group = [t for i, t in enumerate(effective_durations) if (i % 2) == 1]

# Misleading intermediate: max from odd group (looks important, isn't used)
max_odd_duration = max(odd_group) if odd_group else 0

# Auxiliary function: counts transitions in status sequence
def count_transitions(seq):
    return sum(1 for a, b in itertools.pairwise(seq) if a != b)

status_transition_count = count_transitions(node_statuses)  # Computed but unused

# Core metric aggregation function
def aggregate_metrics(times, failures):
    # Filter out failed entries
    surviving_times = [t for f, t in zip(failures, times) if not f]
    
    # Compute statistical metrics (some are red herrings)
    raw_sum = sum(surviving_times)
    count_valid = len(surviving_times)
    mean_time = raw_sum / count_valid if count_valid else 0
    
    # Apply artificial weighting: even-indexed entries get +7ms boost
    weighted_sum = 0
    for i, t in enumerate(surviving_times):
        if i % 2 == 0:
            weighted_sum += t + 7
        else:
            weighted_sum += t
    
    # Diagnostic logic: if more than 3 valid entries, use weighted average, else sum
    if count_valid > 3:
        candidate_value = weighted_sum / count_valid
    else:
        candidate_value = raw_sum
    
    # Final adjustment: add number of active nodes
    active_node_count = node_statuses.count('active')
    final_score = candidate_value + active_node_count
    
    return int(round(final_score))

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, failure_flags)

# Output required format
print(f"Target result: {final_diagnostic}")