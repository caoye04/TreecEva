def analyze_metrics(data):
    total = 0
    count = 0
    bonus_factor = 1.5  # unused distractor
    for item in data:
        if item['active']:
            total += item['value']
            count += 1
    return total // count if count > 0 else 0


def adjust_weights(config):
    adjusted = {}
    base_scale = config.get('scale', 1)
    for key, value in config.items():
        if key != 'scale':
            adjusted[key] = value * base_scale
    return adjusted  # returned but not used in main logic


def evaluate_feedback(history):
    score = 0
    penalty = 0.1
    temp_result = 0
    for record in history:
        if record['type'] == 'positive':
            score += 10
        elif record['type'] == 'negative':
            score -= 5
        temp_result = score * 1.1  # semi-relevant, not directly used
    return int(score)


def evaluate_performance(feedback_dict):
    base = 0
    adjustments = 0
    multiplier = 1
    
    # Real computation path
    for category, entries in feedback_dict.items():
        if category == 'usability':
            for entry in entries:
                base += entry['rating']
        elif category == 'performance':
            for entry in entries:
                if entry['critical']:
                    adjustments -= 2
                else:
                    adjustments += 1

    # Distractor: irrelevant nested loop
    debug_log = []
    for i in range(2):
        for j in range(3):
            debug_log.append(i * j + 7)  # dead computation

    # Distractor: unused dictionary operation
    metadata = {'version': '2.1', 'mode': 'standard'}
    metadata.update({'timestamp': 12345})

    # Actual result calculation
    base = base // 2  # integer division
    multiplier = 3 if adjustments > 0 else 2
    final_score = base * multiplier + abs(adjustments)

    return final_score

# Main execution
raw_data = [
    {'value': 10, 'active': True},
    {'value': 20, 'active': True},
    {'value': 5, 'active': False}
]

config_params = {
    'scale': 2,
    'offset': 3,
    'limit': 10
}

feedback_history = [
    {'type': 'positive'},
    {'type': 'positive'},
    {'type': 'negative'}
]

# Trigger analysis (irrelevant to final result)
dummy_avg = analyze_metrics(raw_data)
dummy_config = adjust_weights(config_params)
dummy_feedback_score = evaluate_feedback(feedback_history)

# Core data for answer
depth_analysis = {
    'usability': [
        {'rating': 4},
        {'rating': 5},
        {'rating': 3}
    ],
    'performance': [
        {'critical': True},
        {'critical': False},
        {'critical': False}
    ]
}

final_score = evaluate_performance(depth_analysis)
print(f"Result: {final_score}")