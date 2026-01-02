def calculate_final_score(entries):
    base_scores = [entry['score'] for entry in entries if entry['valid']]
    penalties = {i: 2 * (idx + 1) for i, idx in enumerate(range(len(base_scores)))}
    adjusted = [base_scores[i] - penalties[i] for i in range(len(base_scores))]
    return sum(adjusted)

# Irrelevant auxiliary data (minor distraction)
data_log = [{'timestamp': '12:01', 'type': 'debug'}, {'timestamp': '12:05', 'type': 'info'}]

candidate_results = [
    {'score': 88, 'valid': True},
    {'score': 92, 'valid': True},
    {'score': 76, 'valid': False},  # Invalid, will be filtered out
    {'score': 85, 'valid': True},
    {'score': 90, 'valid': True}
]

# Key computation
total_score = calculate_final_score(candidate_results)
print(f"Result: {total_score}")