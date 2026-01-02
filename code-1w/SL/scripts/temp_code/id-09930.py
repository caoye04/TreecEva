def analyze_performance(scores, thresholds):
    high_performers = []
    penalty_adjustment = 0
    bonus_applied = False
    
    for idx, (name, score) in enumerate(scores):
        if score > thresholds['excellent']:
            high_performers.append((idx, name))
            if idx % 2 == 0:
                penalty_adjustment -= 2
        elif score > thresholds['good']:
            if not bonus_applied:
                score += 5
                bonus_applied = True
        else:
            continue

        temp_data = [score * 1.1 for _ in range(3)]  # Irrelevant computation
        processed = sum(temp_data) / len(temp_data)

        scores[idx] = (name, min(processed, 100))

    return high_performers, scores, penalty_adjustment


def calculate_average(scores):
    total, count = 0, 0
    for _, score in scores:
        total += score
        count += 1
    return round(total / count, 2) if count else 0


def compute_final_score(student_records, config):
    raw_scores = [(record['name'], record['grade']) for record in student_records]
    adjustments = {'excellent': 85, 'good': 70}
    
    # Distractor: unused transformation
    reversed_names = [name[::-1].title() for name, _ in raw_scores]
    name_length_map = {name: len(name) for name in reversed_names}
    
    performers, updated_scores, penalty = analyze_performance(raw_scores, adjustments)
    avg_score = calculate_average(updated_scores)
    
    # Semi-relevant logic with red herring variables
    multiplier = 1.0
    if len(performers) >= 2:
        multiplier = 1.2
    elif len(performers) == 1:
        multiplier = 1.1

    stability_check = [i for i, _ in enumerate(updated_scores) if i % 3 == 0]
    offset = sum(stability_check) % 5
    
    base_value = avg_score + penalty
    final_score = int((base_value * multiplier) + offset)
    
    # Debugging remnants (dead code path)
    debug_mode = False
    if debug_mode:
        print(f"Performers: {performers}")
        print(f"Adjustments: {adjustments}")

    return final_score

# Input data
students = [
    {'name': 'alice', 'grade': 88},
    {'name': 'bob', 'grade': 76},
    {'name': 'charlie', 'grade': 90},
    {'name': 'diana', 'grade': 65},
    {'name': 'evan', 'grade': 72}
]

config_params = {'debug': False, 'version': '2.1'}

final_score = compute_final_score(students, config_params)
print(f"Result: {final_score}")