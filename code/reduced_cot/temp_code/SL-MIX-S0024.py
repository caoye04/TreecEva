from collections import defaultdict

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_weighted_score(defect_sequence):
    # States: 0=queued, 1=spinning, 2=weaving, 3=dyeing, 4=finished
    score = 0
    for i, defects in enumerate(defect_sequence):
        score += fibonacci(i) * defects
    return score

def process_batches():
    batch_defects = [
        [1, 3, 2, 5, 1],  # Batch 1
        [0, 2, 1, 3, 0],  # Batch 2
        [2, 1, 4, 2, 1],  # Batch 3
    ]
    
    total_score = 0
    state_counter = defaultdict(int)
    
    for defects in batch_defects:
        batch_score = calculate_weighted_score(defects)
        total_score += batch_score
        
        # Update state machine counters
        for state_idx, defect_count in enumerate(defects):
            if defect_count > 0:
                state_counter[state_idx] += 1
    
    # Apply state machine bonus: if all stages have defects in at least 2 batches
    bonus = 10 if all(count >= 2 for count in state_counter.values()) else 0
    
    final_score = total_score + bonus
    return final_score

final_score = process_batches()
print(f"Result: {final_score}")