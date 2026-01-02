from collections import defaultdict, Counter

# Simulated benchmark data across multiple test phases
test_results = [
    {'phase': 'A', 'success': True, 'latency_ms': 120, 'attempts': 3},
    {'phase': 'B', 'success': False, 'latency_ms': 85, 'attempts': 1},
    {'phase': 'A', 'success': True, 'latency_ms': 95, 'attempts': 2},
    {'phase': 'C', 'success': True, 'latency_ms': 200, 'attempts': 4},
    {'phase': 'B', 'success': True, 'latency_ms': 110, 'attempts': 3},
    {'phase': 'C', 'success': False, 'latency_ms': 180, 'attempts': 2}
]

# Irrelevant statistical tracking (distractor)
avg_latency_tracker = defaultdict(float)
phase_counts = Counter([r['phase'] for r in test_results])
for phase in phase_counts:
    total = sum(r['latency_ms'] for r in test_results if r['phase'] == phase)
    avg_latency_tracker[phase] = total / phase_counts[phase]

# Misleading efficiency score calculation (not used in final result)
efficiency_scores = {}
for record in test_results:
    phase = record['phase']
    penalty = record['attempts'] - 1 if record['attempts'] > 1 else 0
    base_score = 100 - record['latency_ms'] * 0.1 - penalty * 5
    efficiency_scores[(phase, record['success'])] = base_score

# Core logic: compute performance based on success rate and attempt efficiency
success_by_phase = defaultdict(list)
attempts_by_phase = defaultdict(list)
for r in test_results:
    success_by_phase[r['phase']].append(1 if r['success'] else 0)
    attempts_by_phase[r['phase']].append(r['attempts'])

# Auxiliary function to compute weighted phase contribution
def compute_phase_weight(success_list, attempt_list):
    success_rate = sum(success_list) / len(success_list)
    avg_attempts = sum(attempt_list) / len(attempt_list)
    normalized_attempts = max(1, avg_attempts)
    # Weight combines success rate and inverse of attempts
    return int(100 * success_rate / normalized_attempts)

# Secondary distraction: hypothetical improvement modeling
projected_gains = []
for phase in success_by_phase:
    current_weight = compute_phase_weight(success_by_phase[phase], attempts_by_phase[phase])
    # Assume perfect success in next iteration
    improved_success = [1] * len(success_by_phase[phase])
    projected_weight = compute_phase_weight(improved_success, attempts_by_phase[phase])
    projected_gains.append(projected_weight - current_weight)

# Actual performance calculation
benchmark_data = []
for phase in sorted(success_by_phase.keys()):
    weight = compute_phase_weight(success_by_phase[phase], attempts_by_phase[phase])
    benchmark_data.append({'phase': phase, 'weight': weight})

def calculate_performance(data):
    base = 0
    multiplier = 1.0
    for entry in data:
        # Apply conditional bonus for later phases
        bonus = 5 if entry['phase'] > 'A' else 0
        contribution = entry['weight'] + bonus
        if contribution > 60:
            multiplier *= 1.1  # stacking multipliers
        base += contribution
    return int(base * multiplier)

# Critical execution point
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")