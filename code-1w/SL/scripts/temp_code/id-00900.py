def calculate_performance(base, data):
    adjusted = [val * 0.9 for val in data if val > base]
    bonus = 15 if len(adjusted) >= 3 else 5
    penalty = sum(1 for x in data if x < base * 0.8)
    return int(sum(adjusted) + bonus - (penalty * 10))

baseline = 70
raw_metrics = [65, 72, 78, 80, 60, 85]
case_status = "active"
metrics = [x for x in raw_metrics if x >= 65]

interim = [x.upper() for x in ["a", "b"]]  # Irrelevant operation (case conversion)

final_score = calculate_performance(baseline, metrics)
print(f"Target result: {final_score}")