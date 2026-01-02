from collections import defaultdict

def calculate_final_score(students):
    scores = defaultdict(float)
    adjustments = {"A": 5.0, "B": 3.0, "C": 1.0}
    
    for name, data in students:
        base = data['grade'] * data['attendance']
        tier = data['tier']
        bonus = adjustments.get(tier.upper(), 0.0)
        penalty = 0
        if data['attendance'] < 0.8:
            penalty = 2.0
        
        scores[name] = base + bonus - penalty
    
    avg_score = sum(scores.values()) / len(scores) if scores else 0
    
    # Irrelevant tracking variable (minor distraction)
    status_count = {"active": 0, "inactive": 0}
    for data in students:
        status_count["active" if data[1]['status'] else "inactive"] += 1
    
    return round(avg_score, 3)

# Input data
students_data = [
    ("Alice", {"grade": 8, "attendance": 0.95, "tier": "A", "status": True}),
    ("Bob", {"grade": 7, "attendance": 0.75, "tier": "B", "status": True}),
    ("Charlie", {"grade": 9, "attendance": 0.88, "tier": "A", "status": False}),
    ("Diana", {"grade": 6, "attendance": 0.90, "tier": "C", "status": True})
]

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")