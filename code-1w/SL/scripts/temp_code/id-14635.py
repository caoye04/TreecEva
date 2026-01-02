from collections import Counter

def calculate_final_score(results):
    count = Counter(results)
    base_score = 0
    bonus = 0
    
    for outcome, freq in count.items():
        if outcome == 'win':
            base_score += freq * 3
        elif outcome == 'draw':
            base_score += freq * 1
        elif outcome == 'loss':
            bonus -= freq  # penalty tracking

    adjustment = len(results) // 5
    total_score = base_score + bonus + adjustment
    return total_score

# Simulation data
match_results = ['win', 'win', 'draw', 'loss', 'win', 'loss', 'win']
extra_data = [10, 20, 30]  # irrelevant list
placeholder_value = sum(extra_data)  # distractor operation

results = match_results

total_score = calculate_final_score(results)
print(f"Result: {total_score}")