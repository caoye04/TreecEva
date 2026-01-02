from collections import defaultdict, Counter

# Simulate system performance metrics across multiple test phases
def analyze_workload(phases):
    stats = defaultdict(int)
    efficiency_list = []
    
    for phase in phases:
        workload = phase['tasks']
        errors = phase['errors']
        duration = phase['duration']
        
        # Real metric: compute efficiency
        if duration > 0:
            efficiency = (workload - errors) / duration
        else:
            efficiency = 0
        
        efficiency_list.append(round(efficiency, 3))
        stats['total_tasks'] += workload
        stats['total_errors'] += errors
    
    avg_efficiency = sum(efficiency_list) / len(efficiency_list) if efficiency_list else 0
    return avg_efficiency, stats['total_errors'], stats

# Auxiliary function to count character patterns in logs (distractor)
def count_log_patterns(logs):
    char_freq = Counter(''.join(logs))
    vowels = 'aeiou'
    vowel_count = sum(char_freq[v] for v in vowels if v in char_freq)
    return vowel_count  # Not used in final result

# Another helper that computes unrelated combinatorics (semi-relevant distractor)
def compute_combinations(n, r):
    if r > n or r < 0:
        return 0
    result = 1
    for i in range(min(r, n - r)):
        result = result * (n - i) // (i + 1)
    return result

# Main evaluation logic
def evaluate_performance(eff, err, benches):
    base = eff * 100
    penalty = err * 2.5
    bonus = 0
    
    # Nested conditional with red herring computations
    if len(benches) > 2:
        adjustment = 5.0
        temp_var = compute_combinations(len(benches), 2)  # Distractor call
        bonus += adjustment if eff > 0.8 else 0
    
    for b in benches:
        if b['type'] == 'stress' and b['result'] == 'pass':
            bonus += 3
    
    # Final score calculation
    raw_score = base - penalty + bonus
    return int(round(raw_score))

# Input data setup
test_phases = [
    {'tasks': 45, 'errors': 3, 'duration': 9},
    {'tasks': 60, 'errors': 5, 'duration': 10},
    {'tasks': 30, 'errors': 1, 'duration': 5}
]

benchmark_logs = [
    'system_initiated',
    'process_started',
    'data_processed',
    'cycle_complete'
]

# Execute analysis
efficiency, error_count, detailed_stats = analyze_workload(test_phases)

# Distractor variables
log_vowel_count = count_log_patterns(benchmark_logs)
dummy_combo = compute_combinations(6, 3)  # Dead-end computation
redundant_slice = benchmark_logs[1:3]  # Irrelevant slicing

benchmarks = [
    {'type': 'baseline', 'result': 'pass'},
    {'type': 'stress', 'result': 'pass'},
    {'type': 'soak', 'result': 'fail'}
]

# Key statement
final_score = evaluate_performance(efficiency, error_count, benchmarks)

print(f"Result: {final_score}")