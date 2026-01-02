def analyze_feedback(reports):
    cumulative = 0
    temp_offset = 0
    for report in reports:
        if 'urgent' in report['flags']:
            temp_offset += len(report['comments'])
        elif 'reviewed' not in report['status']:
            cumulative += report['priority']
    return cumulative


def track_progress(logs):
    progress_tally = 0
    for log in logs:
        progress_tally += log.get('steps', 0)
    scaling_factor = 0.85
    adjusted = int(progress_tally * scaling_factor)
    return adjusted


def evaluate_performance(feedback, criteria):
    base = len(feedback)
    bonus = 0
    penalty = 0

    # Irrelevant tracking (distractor)
    debug_trace = []
    temp_cache = set()

    for item in feedback:
        if item.startswith('F'):
            bonus += 2
        elif item.endswith('X'):
            penalty += 3

    # Semi-relevant filtering
    filtered = {x for x in feedback if 'C' not in x}
    size_check = len(filtered) > 5

    # Misleading computation
    phantom_sum = 0
    for i in range(len(feedback)):
        if i % 3 == 0:
            phantom_sum += i * 1.5  # Unused later

    if size_check:
        bonus += 4

    # Core logic disguised among noise
    threshold = criteria['threshold']
    if len(filtered) >= threshold:
        penalty -= 2  # Net positive effect

    result = base + bonus - penalty
    return result


# Input data
feedback_set = ['FX01', 'ABC2', 'FXX3', 'DEF4', 'F005', 'FGH6', 'FXX7']
benchmark = {'version': '2.1', 'active': True, 'threshold': 6}

# Auxiliary irrelevant variables
aux_data = [10, 20, 30]
dummy_flag = False
offset_counter = 0

# Dead code path (never executed but looks relevant)
if dummy_flag:
    offset_counter = track_progress([{'steps': 5}, {'steps': 3}])

# Trigger analysis (irrelevant to final result)
analyze_feedback([
    {'flags': ['normal'], 'comments': [], 'priority': 1},
    {'flags': [], 'comments': ['minor'], 'priority': 0}
])

# Key execution point
final_score = evaluate_performance(feedback_set, benchmark)

print(f"Result: {final_score}")