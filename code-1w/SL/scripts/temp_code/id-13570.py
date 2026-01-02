from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for combo in combinations(sequence, 3):
        if sum(combo) % 3 == 0:
            count += 1
    return count

def evaluate_consistency(data):
    baseline = len(data) // 2
    deviation = 0
    for i in range(len(data)):
        if data[i] % 2 != i % 2:
            deviation += 1
    return baseline - deviation

def calculate_performance_rating():
    raw_data = [3, 6, 9, 12, 15]
    transformed = [x // 3 for x in raw_data if x > 6]
    pattern_strength = analyze_pattern(raw_data)
    consistency = evaluate_consistency(transformed)
    
    # Irrelevant distraction: unused variable
    temp_result = ''.join(map(str, transformed))
    
    final_score = pattern_strength * consistency
    return final_score

result_value = calculate_performance_rating()
print(f"Result: {result_value}")