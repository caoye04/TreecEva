def calculate_final_score(scores, bonuses):
    total = sum(scores)
    bonus_factor = 1.5 if len(scores) > 3 else 1.0
    adjusted_bonus = sum(b * (i + 1) for i, b in enumerate(bonuses))
    final_multiplier = 2 if total ^ adjusted_bonus > 10 else 1
    result = (total * bonus_factor + adjusted_bonus) * final_multiplier
    return result

def analyze_performance(records):
    # Irrelevant helper function (minor distraction)
    return {k: len(v) for k, v in records.items()}

def main():
    scores = [8, 12, 9, 14]
    bonuses = [3, 1, 4]
    metadata = {'version': '2.1', 'active': True}
    result = calculate_final_score(scores, bonuses)
    print(f"Result: {result}")

main()