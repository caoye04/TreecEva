def analyze_performance(marks, thresholds):
    passing = set()
    for mark in marks:
        if mark >= thresholds['pass']:
            passing.add(mark)
    return passing

marks_list = [55, 72, 88, 49, 91, 67]
thresholds_config = {'pass': 60, 'distinction': 85}

# Irrelevant computation - distractor
average_mark = sum(marks_list) / len(marks_list)
deviations = [abs(m - average_mark) for m in marks_list]
variance_estimate = sum(d**2 for d in deviations) / len(deviations)

qualified_set = analyze_performance(marks_list, thresholds_config)
distinction_candidates = {m for m in qualified_set if m >= thresholds_config['distinction']}

# Simulate penalty system
penalty_map = {88: 5, 91: 10, 72: 2}
penalties = []
for score in marks_list:
    if score in penalty_map:
        penalties.append(penalty_map[score])
    else:
        penalties.append(0)

results = []
for s in sorted(qualified_set):
    count = 0
    for p in penalties:
        if p > 0:
            count += 1
    results.append(s - count * 2)

# Secondary irrelevant tracking
status_log = []
for r in results:
    if r > 70:
        status_log.append('high')
    elif r > 50:
        status_log.append('medium')
    else:
        status_log.append('low')

# Core calculation with moderate nesting and logic
running_total = 0
multiplier = 1
for idx, val in enumerate(results):
    temp_offset = 0
    if idx % 2 == 0:
        temp_offset = 3
    else:
        temp_offset = -1
    
    intermediate = val + temp_offset
    if intermediate > 75:
        running_total += intermediate * 1.1
    elif intermediate > 60:
        running_total += intermediate * 1.05
    else:
        running_total += intermediate

    # Dead code path - distractor
    if multiplier > 100:
        reset_flag = True
        running_total = 0

    multiplier += 1

# Final aggregation with set-based adjustment
def calculate_final_score(scores, deductions):
    base = int(sum(scores))
    deduction_total = sum(deductions)
    adjustment_factor = len(distinction_candidates)  # only depends on global state
    bonus = adjustment_factor * 7
    return base - deduction_total + bonus

final_score = calculate_final_score(results, penalties)
print(f"Result: {final_score}")