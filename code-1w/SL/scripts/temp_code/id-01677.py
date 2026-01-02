def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    phantom_entries = []

    for i, entry in enumerate(logs):
        time_spent = entry['duration']
        total_hours += time_spent
        if time_spent < 0.5:
            idle_count += 1
            phantom_entries.append(i)

    adjusted_hours = total_hours * (0.95 if idle_count > 2 else 1.0)
    return adjusted_hours, phantom_entries


def extract_keywords(tasks):
    keywords = []
    for task in tasks:
        cleaned = task.strip().lower().replace('urgent', '').replace('pending', '')
        words = cleaned.split()
        keywords.extend([w for w in words if len(w) > 2])
    keyword_freq = {}
    for kw in keywords:
        keyword_freq[kw] = keyword_freq.get(kw, 0) + 1
    return keyword_freq


def calculate_rating(entries, factor_map):
    base = 0
    bonus = 0
    penalty = 0

    for idx, val in enumerate(entries):
        key = f"task_{idx % 4}"
        scaling = factor_map.get(key, 1.0)
        
        temp_val = val * scaling
        if temp_val > 15:
            bonus += 3
        elif temp_val < 5:
            penalty += 1
        base += temp_val

    aggregate = base + bonus - penalty
    normalized = round(aggregate / len(entries), 2) if entries else 0
    return int(normalized)

# Main workflow
activity_logs = [
    {'duration': 1.2, 'type': 'dev'},
    {'duration': 0.3, 'type': 'meeting'},
    {'duration': 2.1, 'type': 'design'},
    {'duration': 0.4, 'type': 'review'},
    {'duration': 3.0, 'type': 'debug'}
]

raw_tasks = [
    "Implement core module urgent",
    "Fix bugs in pending components",
    "Optimize database layer",
    "Update documentation"
]

hours_worked, ignored_indices = analyze_productivity(activity_logs)
word_frequency = extract_keywords(raw_tasks)

contributions = [12, 18, 5, 22, 14]
efficiency = {
    'task_0': 1.1,
    'task_1': 0.9,
    'task_2': 1.0,
    'task_3': 1.2
}

staging_score = sum(contributions) // len(contributions)
staging_score += len(word_frequency)  # minor influence

# Misleading intermediate calculation
fuzzy_metric = 0
for k, v in word_frequency.items():
    fuzzy_metric += len(k) * v
fuzzy_metric = fuzzy_metric / 10 if fuzzy_metric > 0 else 0

final_score = calculate_rating(contributions, efficiency)

# Print result
Target result: {final_score}