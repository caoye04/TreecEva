from collections import defaultdict, Counter
import math

# Simulated user interaction analytics for a productivity app
raw_events = [
    'click:sidebar', 'hover:search', 'input:query', 'click:search',
    'hover:result', 'click:result', 'scroll:content', 'input:filter',
    'click:apply', 'hover:export', 'click:export', 'click:sidebar'
]

# Distractor: irrelevant event types and mappings
event_categories = {
    'navigation': ['click:sidebar', 'click:header', 'hover:breadcrumb'],
    'search': ['input:query', 'click:search', 'hover:suggestion'],
    'interaction': ['click:result', 'hover:result', 'scroll:content'],
    'export': ['click:export', 'input:format', 'click:confirm'],
    'filtering': ['input:filter', 'click:apply', 'reset:filters']
}

# Mapping events to categories (some events belong to multiple categories)
event_to_category = {}
for cat, events in event_categories.items():
    for e in events:
        if e not in event_to_category:
            event_to_category[e] = []
        event_to_category[e].append(cat)

# Extract action type from event (e.g., 'click:sidebar' -> 'click')
action_types = [event.split(':')[0] for event in raw_events]
location_types = [event.split(':')[1] for event in raw_events]

# Count frequency of actions and locations
action_freq = Counter(action_types)
location_freq = Counter(location_types)

total_actions = sum(action_freq.values())
dominant_action = action_freq.most_common(1)[0][0]

# Distractor: unused function for sentiment-like scoring (not actually used)
def pseudo_sentiment(text):
    positive_words = ['click', 'input', 'search']
    negative_words = ['hover', 'scroll']
    score = 0
    for word in text.split(':'):
        if word in positive_words:
            score += 0.3
        elif word in negative_words:
            score -= 0.2
    return round(score, 2)

# Real processing begins: categorize raw events
assigned_categories = []
for event in raw_events:
    if event in event_to_category:
        assigned_categories.extend(event_to_category[event])
    else:
        assigned_categories.append('other')

category_counts = Counter(assigned_categories)

# Normalize category counts by total number of events
normalized_counts = {k: v / len(raw_events) for k, v in category_counts.items()}

# Distractor: fake engagement metrics based on irrelevant heuristics
fake_engagement = {}
for loc in set(location_types):
    fake_engagement[loc] = round(math.sin(location_freq[loc]) + 0.5, 3)

# Simulate time-series decay weighting (irrelevant but looks meaningful)
time_weights = [math.exp(-i * 0.1) for i in range(len(raw_events))]
weighted_actions = defaultdict(float)
for i, action in enumerate(action_types):
    weighted_actions[action] += time_weights[i]

# Focus metric: how often primary action repeats consecutively
consecutive_clicks = 0
max_consecutive = 0
for action in action_types:
    if action == 'click':
        consecutive_clicks += 1
        max_consecutive = max(max_consecutive, consecutive_clicks)
    else:
        consecutive_clicks = 0

# Distractor: complex-looking but unused transformation pipeline
decoy_pipeline = [
    [x.upper() for x in raw_events if 'hover' in x],
    ''.join([loc[0] for loc in location_types]),
    {a: math.log(freq + 1) for a, freq in action_freq.items()}
]

# Real signal: calculate depth of interaction using category diversity
diversity_index = len(category_counts) / 10.0  # Max expected ~5-6 categories

# Weighted importance of each category (business logic)
metric_weights = {
    'search': 0.8,
    'interaction': 1.2,
    'export': 2.0,
    'filtering': 1.0,
    'navigation': 0.5
}

# Normalize data includes both count and derived signals
normalized_data = {}
for cat in metric_weights.keys():
    base_count = normalized_counts.get(cat, 0)
    # Add minor adjustment based on action dominance (only if click is dominant)
    adjustment = 0.1 if dominant_action == 'click' and cat in ['interaction', 'export'] else 0
    normalized_data[cat] = base_count + adjustment

# Critical function: evaluates user performance score
# This is where the answer is determined
def evaluate_performance(weights, norm_data):
    score = 0.0
    for cat, weight in weights.items():
        if cat in norm_data:
            contribution = weight * norm_data[cat]
            # Only add contribution if category has been triggered
            if cat in category_counts and category_counts[cat] > 1:
                score += contribution * 1.1  # bonus for repeated engagement
            else:
                score += contribution * 0.9  # penalty for single occurrence
    # Final adjustment based on behavioral diversity
    diversity_bonus = diversity_index * 0.5
    score += diversity_bonus
    return round(score, 6)

# Execute key statement
final_score = evaluate_performance(metric_weights, normalized_data)

# Irrelevant print statements (distractors)
# print(f'Dominant action: {dominant_action}')
# print(f'Fake engagement scores: {fake_engagement}')
# print(f'Time-weighted actions: {dict(weighted_actions)}')

# Output the target result
print(f"Result: {final_score}")