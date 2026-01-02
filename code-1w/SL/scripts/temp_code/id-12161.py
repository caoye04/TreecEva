from itertools import combinations

def evaluate_pair(pair):
    a, b = pair
    return (a * b) + (a + b)

def calculate_final_score(raw_data):
    processed = [x * 2 for x in raw_data if x % 2 == 0]
    pairs = list(combinations(processed, 2))
    scores = [evaluate_pair(p) for p in pairs]
    temp_offset = sum([1 for x in raw_data if x > 5])  # distractor: counts but not used directly
    final_score = sum(scores) // len(scores) if scores else 0
    return final_score

data_set = [2, 3, 4, 5, 6]
result = calculate_final_score(data_set)
final_score = result
print(f"Result: {final_score}")