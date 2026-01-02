def calculate_final_score(results, threshold):
    filtered = [r for r in results if r >= threshold]
    weighted = list(map(lambda x: x * 1.1 if x < 75 else x * 1.05, filtered))
    return int(sum(weighted))

# Simulated student test results
raw_scores = [68, 72, 85, 54, 91, 43, 77]
passing_threshold = 55

# Irrelevant distraction: unused variable
average_baseline = sum(raw_scores) / len(raw_scores)

# Key processing pipeline
results = [score + 3 for score in raw_scores if score % 2 == 0]  # Only even base scores get bonus

final_score = calculate_final_score(results, passing_threshold)
print(f"Result: {final_score}")