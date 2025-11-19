from collections import defaultdict
import statistics

def process_batch_cycles(initial_composition, cycle_rules):
    current_state = 'pending'
    purity_scores = []
    for cycle in range(cycle_rules['max_cycles']):
        if current_state == 'pending':
            purity_gain = cycle_rules['refinement_base'] + (cycle * 0.7)
            new_purity = min(100, initial_composition['purity'] + purity_gain)
            purity_scores.append(new_purity)
            if new_purity >= cycle_rules['acceptance_threshold']:
                current_state = 'refined'
        elif current_state == 'refined':
            stability_test = (purity_scores[-1] * 0.6) + (cycle * 1.2)
            if stability_test > cycle_rules['stability_target']:
                current_state = 'stable'
        if current_state == 'stable':
            break
    return current_state, purity_scores

def calculate_approval_metric(batch_results):
    states = defaultdict(int)
    all_purities = []
    for state, scores in batch_results:
        states[state] += 1
        all_purities.extend(scores)
    avg_purity = statistics.mean(all_purities) if all_purities else 0
    state_factor = states['stable'] * 10 + states['refined'] * 5 + states['pending'] * 1
    return int(avg_purity + state_factor)

production_batches = [
    {'id': 'BATCH_001', 'purity': 72.5},
    {'id': 'BATCH_002', 'purity': 68.0},
    {'id': 'BATCH_003', 'purity': 75.3}
]

cycle_protocol = {
    'max_cycles': 4,
    'refinement_base': 5.5,
    'acceptance_threshold': 80.0,
    'stability_target': 55.0
}

processed_results = [process_batch_cycles(batch, cycle_protocol) for batch in production_batches]
final_approval_score = calculate_approval_metric(processed_results)
print(f"Result: {final_approval_score}")