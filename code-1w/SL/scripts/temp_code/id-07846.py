from collections import defaultdict

def process_results(responses, importance_weights):
    score = 0
    response_count = defaultdict(int)

    for response in responses:
        response_count[response] += 1

    base_value = 0
    for i, val in enumerate(importance_weights):
        if i % 2 == 0:
            base_value += val * response_count.get(i % 4, 0)
        else:
            base_value -= val & (response_count.get(i % 4, 0) << 1)

    adjustment = 0
    temp = base_value
    while temp > 0:
        adjustment += temp & 1
        temp >>= 1

    final_result = base_value + adjustment
    return final_result

# Simulated input data
answers = [0, 1, 1, 2, 3, 0, 2, 1]
weights = [3, 7, 2, 5]

# Irrelevant distraction variable
unused_buffer = [0] * 10

final_score = process_results(answers, weights)
print(f"Result: {final_score}")