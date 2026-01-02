import math

def analyze_phase_shift(frequency, amplitude):
    # Irrelevant signal analysis function (dead code path)
    if frequency <= 0:
        return 0.0
    return amplitude * math.sin(frequency * math.pi / 180)

def generate_node_map(size):
    # Distractor: Builds a grid but isn't used in final computation
    return [[(i * size + j) % 7 for j in range(size)] for i in range(size)]

def evaluate_threshold(value, mode='strict'):
    # Misleading utility with conditional expression
    return value > 50 if mode == 'strict' else value > 30

def accumulate_diagnostics(log_entries):
    total = 0
    weights = [0.1, 0.2, 0.3, 0.4]  # Unused weight array - red herring
    multipliers = {"A": 2, "B": 3, "C": 1}  # Partially used dict
    for entry in log_entries:
        tag = entry[0]
        metric = entry[1]
        # Conditional expression used meaningfully
        adjustment = multipliers.get(tag, 0.5) if metric % 2 == 0 else 1.5
        total += int(metric * adjustment)
    return total

def validate_consistency(checksums):
    # Dead code - never called
    return sum(c ** 2 for c in checksums if c % 3 == 0)

def compute_integrity_score(state_log):
    # Core logic hidden among distractions
    base_score = 0
    temp_offset = 0
    for record in state_log:
        node_id = record['id']
        status_flag = record['flag']
        history = record['seq']
        
        # Real computation begins
        sequence_sum = sum(history)
        if len(history) > 4:
            mid_val = history[len(history) // 2]
            if mid_val % 2 == 0:
                base_score += node_id
        
        # Conditional expression affecting result
        penalty = 10 if status_flag == 'ERR' else (5 if status_flag == 'WARN' else 0)
        
        # Nested condition with decoy variables
        temp_var_x = node_id * 2 + sequence_sum
        temp_offset += temp_var_x % 7
        
        if status_flag in ['ERR', 'CRIT']:
            base_score -= penalty
        elif status_flag == 'OK':
            base_score += 3
    
    # Final transformation using average and min
    all_sums = [sum(r['seq']) for r in state_log]
    avg_sum = sum(all_sums) / len(all_sums)
    min_sum = min(all_sums)
    
    # Key manipulation: only this line contributes to final answer
    final_correction = int(avg_sum - min_sum)
    
    # Actual return value built from multiple steps
    result = base_score + final_correction + temp_offset % 13
    return result

# Main execution flow
if __name__ == '__main__':
    # Unused data structures - heavy distractors
    signal_data = [(50, 2.3), (60, 1.8), (0, 5.5)]
    node_grid = generate_node_map(8)  # Computed but unused
    thresholds = [evaluate_threshold(x) for x in [25, 40, 55, 60]]  # Redundant evaluation

    # Relevant input data
    network_state_log = [
        {'id': 12, 'flag': 'OK', 'seq': [1, 3, 5]},
        {'id': 15, 'flag': 'WARN', 'seq': [2, 4, 6, 8, 10]},
        {'id': 8, 'flag': 'ERR', 'seq': [1, 1, 1, 1]},
        {'id': 20, 'flag': 'OK', 'seq': [3, 6, 9, 12]},
        {'id': 10, 'flag': 'CRIT', 'seq': [5, 5]}
    ]

    # Decoy accumulation
    dummy_entries = [('A', 40), ('B', 60), ('X', 25)]
    dummy_score = accumulate_diagnostics(dummy_entries)  # Used nowhere

    # Critical statement
    final_diagnostic = compute_integrity_score(network_state_log)
    
    # Output required
    print(f"Target result: {final_diagnostic}")