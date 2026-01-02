def analyze_productivity(logs):
    base_efficiency = 1.0
    distractions = 0
    total_work_units = 0
    idle_periods = []

    for idx, entry in enumerate(logs):
        if 'idle' in entry:
            idle_periods.append(idx)
            distractions += len(entry) % 7
        elif 'task' in entry:
            units = len(entry.split()) - 1
            total_work_units += units * (0.9 + base_efficiency)

    adjusted_focus = base_efficiency - (distractions * 0.05)
    return total_work_units, adjusted_focus, idle_periods


def evaluate_innovation(ideas):
    novelty_scores = []
    for idea in ideas:
        score = sum(1 for c in idea if c.isupper())
        penalty = sum(1 for c in idea if not c.isalnum() and c != ' ')
        novelty_scores.append(max(1, score - penalty))
    return novelty_scores

# Simulated employee performance data
team_logs = [
    'task complete report analysis',
    'idle: waiting for feedback',
    'task fix critical bug in module',
    'task draft new api design',
    'idle checking emails',
    'task optimize database query',
    'task review pull request'
]

team_ideas = [
    'Improve UX with Dynamic Widgets!',
    'AI-driven Logging System (patent pending)',
    'Better Caching Using Redis Cluster',
    'Use JSON for config files instead of YAML?'
]

# Extract productivity metrics
total_units, focus_level, downtime = analyze_productivity(team_logs)
innovation_raw = evaluate_innovation(team_ideas)

# Irrelevant intermediate calculations (distractors)
theoretical_max_innovation = len(team_ideas) * 5
average_novelty = sum(innovation_raw) / len(innovation_raw) if innovation_raw else 0
duplicate_check = [x for x in zip(innovation_raw, innovation_raw)]

# Core logic with lambda and zip usage
weight_scheme = lambda x: 0.6 if x < 3 else 0.8 if x < 5 else 1.0
weighted_innovations = sum(w * weight_scheme(n) for n, w in enumerate(innovation_raw))

contribution_base = total_units + weighted_innovations
penalty_factor = len(downtime) * 2.5 + (5 if focus_level < 0.8 else 0)

# Key statement
contributions = list(map(lambda x: x * focus_level, [total_units, weighted_innovations]))
penalties = [penalty_factor, distractions * 1.5]

def calculate_rating(contribs, puns):
    combined = sum(contribs) - sum(puns)
    bonus = 10 if sum(contribs) > 50 else 5
    return int(combined + bonus)

final_score = calculate_rating(contributions, penalties)
print(f"Result: {final_score}")