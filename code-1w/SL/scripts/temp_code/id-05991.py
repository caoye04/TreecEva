from collections import defaultdict, Counter
from itertools import cycle

# Simulate user interaction feedback over multiple sessions
def generate_feedback_sequence():
    raw_inputs = ['error', 'success', 'warning', 'success', 'success', 'info', 'error']
    processed = []
    temp_count = defaultdict(int)
    
    for entry in raw_inputs:
        temp_count[entry] += 1
        if entry == 'success':
            processed.append(1)
        elif entry == 'error':
            processed.append(-2)
        else:
            processed.append(0)
    
    # Distractor: unused transformation
    scaled = [x * 1.5 for x in processed]
    return processed

# Analyze pattern recurrence and weight recent feedback more heavily
def compute_decay_weights(length, decay_factor=0.8):
    return [decay_factor ** (length - i) for i in range(length)]

# Track state across nested conditions
def evaluate_performance(feedback_log):
    weights = compute_decay_weights(len(feedback_log))
    weighted_sum = 0
    
    # Apply decaying importance to historical entries
    for i, score in enumerate(feedback_log):
        weighted_sum += score * weights[i]
    
    # Secondary metric (distractor): frequency analysis
    freq = Counter(feedback_log)
    peak_streak = 0
    current_streak = 0
    
    for val in feedback_log:
        if val == 1:
            current_streak += 1
        else:
            peak_streak = max(peak_streak, current_streak)
            current_streak = 0
    peak_streak = max(peak_streak, current_streak)
    
    # Irrelevant transformation chain
    dummy_map = {k: v * 1.1 for k, v in freq.items()}
    normalized_dummy = sum(dummy_map.values()) / len(dummy_map) if dummy_map else 0
    
    # Real logic: base adjustment based on weighted trend
    adjustment = 5 if weighted_sum > 0 else -5
    base_score = int(weighted_sum + adjustment)
    
    # Final override condition based on streak (only matters if streak >= 2)
    if peak_streak >= 2:
        base_score += 3
    
    # Red herring calculation with no effect
    outlier_check = any(abs(x) > 2 for x in feedback_log)
    consistency_flag = not outlier_check and len(set(feedback_log)) <= 3
    
    final_score = base_score  # This will be modified only once more
    
    # Last-minute offset unrelated to control flow
    final_score += len([x for x in feedback_log if x == 0]) // 2
    
    return final_score

# Unused helper: simulates alternative evaluation path
def debug_analyze(seq):
    return sum(x for x in seq if x > 0)

# Setup and execution
def main():
    feedback_chain = generate_feedback_sequence()
    
    # Distractor variables
    audit_trace = [f"Step-{i}: {v}" for i, v in enumerate(feedback_chain)]
    summary_stats = {
        'total': len(feedback_chain),
        'positive': sum(1 for x in feedback_chain if x > 0),
        'negative': sum(1 for x in feedback_chain if x < 0)
    }
    
    # Key computation point
    final_score = evaluate_performance(feedback_chain)
    
    # Print required result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()