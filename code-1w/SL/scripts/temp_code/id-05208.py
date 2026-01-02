from collections import Counter

def evaluate_performance(record):
    counts = Counter(record)
    correct = counts.get('pass', 0)
    attempts = len(record)
    return correct / attempts if attempts > 0 else 0

def calculate_final_score(results):
    scores = [evaluate_performance(r) for r in results]
    adjusted = [s ** 2 for s in scores]
    total_score = sum(adjusted)
    return total_score

def analyze_trend(data):
    # Irrelevant helper function (minimal interference)
    return [x - 0.1 for x in data]

# Main execution
session_results = [
    ['pass', 'fail', 'pass', 'pass'],
    ['fail', 'pass', 'pass'],
    ['pass', 'pass', 'pass', 'fail', 'pass']
]

auxiliary_data = [1, 2, 3]  # Slight distraction
interim = analyze_trend(auxiliary_data)

total_score = calculate_final_score(session_results)
print(f"Result: {total_score}")