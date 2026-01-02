from collections import defaultdict
import itertools

# Simulate student test responses with timestamps and scores
test_sessions = [
    {'student': 'A', 'responses': [(True, 30), (False, 45), (True, 20)], 'section': 'math'},
    {'student': 'B', 'responses': [(False, 35), (True, 40), (True, 25)], 'section': 'math'},
    {'student': 'C', 'responses': [(True, 50), (True, 15), (False, 60)], 'section': 'logic'}
]

# Irrelevant metadata about test environment
test_metadata = {
    'location': 'Lab 4B',
    'supervisor': 'Dr. Evans',
    'max_duration': 120,
    'version': '2.1'
}

# Distractor: Unused function for audio analysis (simulated)
def analyze_ambient_noise(samples):
    if len(samples) == 0:
        return 0.0
    avg = sum(samples) / len(samples)
    return round(avg * 0.85, 2)

# Real processing begins here
response_stats = defaultdict(lambda: {'correct': 0, 'total_time': 0, 'count': 0})

for session in test_sessions:
    student = session['student']
    section = session['section']
    total_session_time = sum([t for _, t in session['responses']])
    
    # Filter out sessions that are too short (potential invalid data)
    if total_session_time < 60:
        continue
        
    for idx, (is_correct, time_taken) in enumerate(session['responses']):
        key = f"{student}_{section}"
        response_stats[key]['correct'] += 1 if is_correct else 0
        response_stats[key]['total_time'] += time_taken
        response_stats[key]['count'] += 1

# Compute per-key accuracy and efficiency ratios
efficiency_metrics = {}
for key, stats in response_stats.items():
    accuracy = stats['correct'] / stats['count']
    avg_time = stats['total_time'] / stats['count']
    efficiency = accuracy / (avg_time + 1e-5)  # Prevent division by zero
    efficiency_metrics[key] = {'accuracy': accuracy, 'efficiency': efficiency}

# Distractor: unused combination generation
candidate_pairs = list(itertools.combinations(efficiency_metrics.keys(), 2))
pair_similarity = defaultdict(float)
for a, b in candidate_pairs:
    acc_diff = abs(efficiency_metrics[a]['accuracy'] - efficiency_metrics[b]['accuracy'])
    pair_similarity[(a,b)] = round(1 - acc_diff, 3)

# Core aggregation logic
aggregate_inputs = []
for key, metrics in efficiency_metrics.items():
    base_score = metrics['accuracy'] * 100
    time_bonus = 50 / (metrics['efficiency'] * 10 + 1)  # Inverse relationship
    adjusted_score = base_score + time_bonus
    aggregate_inputs.append(adjusted_score)

# Final normalization using slicing of top performers
top_performers = sorted(aggregate_inputs, reverse=True)[:2]
avg_top = sum(top_performers) / len(top_performers)
penalty_factor = 0.95 if len(aggregate_inputs) > 2 else 1.0

# Introduce irrelevant intermediate calculation (distractor)
phantom_correction = 0
for i in range(len(aggregate_inputs)):
    if i % 2 == 0:
        phantom_correction += aggregate_inputs[i] * 0.01

# Critical execution point
final_score = int(avg_top * penalty_factor)  # Final result

# Print result as required
print(f"Result: {final_score}")