def assess_performance(checker, levels):
    results = []
    for level in levels:
        if checker(level):
            results.append(level * 1.5)
        else:
            results.append(level * 0.8)
    return sum(results)

# Irrelevant helper (mild distraction)
def normalize(value):
    return value / 10.0

threat_levels = [10, 20, 30, 40]
defense_fn = lambda x: x % 15 == 0  # Triggers on multiples of 15

# Key computation step
cached_result = [x * 2 for x in threat_levels]  # Distractor list

final_score = assess_performance(defense_fn, threat_levels)
print(f"Result: {final_score}")