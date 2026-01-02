def calculate_performance(results):
    score_map = {0: 5, 1: 10, 2: 20, 3: 40}
    normalized = [min(3, max(0, x)) for x in results]
    weights = [score_map[w] for w in normalized]
    total = sum(weights)
    count = len(weights)
    average = total / count if count else 0
    bonus = 10 if average > 25 else 0
    final = average + bonus
    return int(final)

# Simulated user test response counts
test_data = [1, 0, 2, 3, 3, 1, 2, 0]
bins = [x for x in test_data if x >= 0]

def ignore_temporary():
    temp_result = 0
    for i in range(3):
        temp_result += i
    return temp_result

unused_var = ignore_temporary()  # Irrelevant function call (minimal interference)

final_score = calculate_performance(bins)
print(f"Result: {final_score}")