from collections import Counter

def calculate_performance(results):
    count = Counter(results)
    correct = count.get(True, 0)
    total = len(results)
    accuracy = correct / total
    
    base_score = accuracy * 100
    penalty = 0
    if count.get(False, 0) > 2:
        penalty = 10
    
    adjustment = (correct - count.get(False, 0)) // 5
    final_score = base_score - penalty + adjustment
    
    temp_debug = base_score + penalty  # irrelevant tracking
    unused_flag = False  # red herring variable
    return int(final_score)

# Simulated benchmark test outcomes
test_outcomes = [True, True, False, True, True, False, True, True, True, False]

final_score = calculate_performance(test_outcomes)
print(f"Result: {final_score}")