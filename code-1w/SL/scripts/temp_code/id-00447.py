def calculate_final_score(phases):
    process = lambda x: (x[0] * 2) + (x[1] % 3)
    scores = []
    for i, phase in enumerate(phases):
        if i % 2 == 0:
            scores.append(process(phase))
    return sum(scores)

# Irrelevant auxiliary data (minimal distraction)
temp_data = [10, 20, 30]
phases = [(5, 7), (8, 6), (3, 5), (9, 2)]

result = calculate_final_score(phases)
print(f"Result: {result}")