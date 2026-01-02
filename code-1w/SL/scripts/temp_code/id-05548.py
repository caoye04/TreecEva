def compute_final_score(students):
    total_score = 0
    scores = [s['grade'] for s in students if s['active']]
    indices = list(enumerate(scores))
    
    # Irrelevant auxiliary variable (minor distraction)
    avg = sum(scores) / len(scores) if scores else 0
    
    for i, score in indices:
        if i % 2 == 0:
            total_score += score * 1.1
        else:
            total_score += score
    return int(total_score)

students = [
    {'name': 'Alice', 'grade': 85, 'active': True},
    {'name': 'Bob', 'grade': 90, 'active': False},
    {'name': 'Charlie', 'grade': 78, 'active': True},
    {'name': 'Diana', 'grade': 92, 'active': True},
    {'name': 'Eve', 'grade': 88, 'active': False}
]

# Filtering only active students: Alice (85), Charlie (78), Diana (92)
# Indices: 0->85, 1->78, 2->92 → even indices: 0,2 → 85*1.1 and 92*1.1

irrelevant_data = {'version': '1.0', 'debug': True}

total_score = compute_final_score(students)
print(f"Result: {total_score}")