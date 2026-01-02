def calculate_final_score(records):
    base_scores = [rec['value'] for rec in records if rec['active']]
    adjustments = {i: (i % 3) - 1 for i in range(len(base_scores))}
    adjusted = [base_scores[i] + adjustments[i] for i in range(len(base_scores))]
    filtered = adjusted[1:-1]  # Slice to remove first and last
    return sum(filtered) // len(filtered)

data = [
    {'value': 10, 'active': False},
    {'value': 15, 'active': True},
    {'value': 20, 'active': True},
    {'value': 25, 'active': True},
    {'value': 30, 'active': False}
]

# Irrelevant auxiliary variable (minimal distraction)
status_flags = {1: 'valid', 2: 'invalid'}

final_score = calculate_final_score(data)
print(f"Result: {final_score}")