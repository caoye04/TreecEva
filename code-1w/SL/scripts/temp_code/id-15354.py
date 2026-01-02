def calculate_final_score(entries):
    total_score = 0
    bonus_active = False
    
    for i, (name, score, completed) in enumerate(entries):
        if completed and score > 80:
            bonus_active = True
        adjustment = 1.1 if bonus_active else 1.0
        total_score += score * adjustment
    
    return int(total_score)

# Simulated assessment results
dummy_data = [("Module A", 75, True), ("Module B", 82, True), ("Module C", 90, False)]
results = [*zip([r[0] for r in dummy_data], [r[1] for r in dummy_data], [r[2] for r in dummy_data])]

# Irrelevant tracking variable (minor distraction)
processed_count = len(results)

# Key computation
total_score = calculate_final_score(results)

print(f"Result: {total_score}")