from itertools import combinations

def evaluate_trial(data, threshold=5.0):
    above_threshold = [x for x in data if x > threshold]
    return len(above_threshold) / len(data) if data else 0

def generate_pairs(values):
    # Irrelevant utility function for distraction (minimal interference)
    return list(combinations(values, 2))

def calculate_performance(logs):
    scores = []n    for entry in logs:
        raw_data = entry['metrics']
        score = evaluate_trial(raw_data)
        scores.append(score * 100)
    
    # Apply weighting based on trial importance
    weighted = [scores[i] * (i + 1) for i in range(len(scores))]
    total = sum(weighted)
    
    # Key computation step
    final_score = total // len(scores) if scores else 0
    return final_score

# Simulated benchmark results from performance trials
benchmark_results = [
    {'metrics': [4.2, 6.1, 7.3, 5.5], 'trial_id': 'A1'},
    {'metrics': [5.0, 5.1, 6.0, 7.2], 'trial_id': 'A2'},
    {'metrics': [6.5, 8.1, 9.0], 'trial_id': 'A3'},
    {'metrics': [3.2, 4.1, 5.8, 6.9], 'trial_id': 'A4'}
]

# Distractor: unused variable (minor interference)
baseline_configs = ['cfg_x', 'cfg_y']

# Core execution leading to answer
final_score = calculate_performance(benchmark_results)

print(f"Result: {final_score}")