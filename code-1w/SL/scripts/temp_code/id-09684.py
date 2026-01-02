from collections import defaultdict, Counter

# Simulated user interaction data with noise
data_stream = [
    ('click', 'A', 0.8), ('hover', 'B', 0.5), ('click', 'A', 0.9), 
    ('scroll', 'C', 0.3), ('click', 'B', 0.7), ('hover', 'A', 0.4),
    ('click', 'C', 0.6), ('scroll', 'B', 0.2)
]

# Irrelevant metadata (distractor)
system_uptime = 1274
active_sessions = 3
server_load = [0.45, 0.67, 0.52, 0.71]

# Filter relevant events and aggregate by label
event_weights = defaultdict(float)
event_counts = Counter()

for event_type, label, confidence in data_stream:
    if event_type == 'click':
        event_weights[label] += confidence * 2
        event_counts[label] += 1
    elif event_type == 'hover':
        event_weights[label] += confidence * 0.5
    elif event_type == 'scroll':
        # Scroll events have minimal impact (but still processed)
        event_weights[label] += confidence * 0.1

# Compute average confidence per label (only for labels with clicks)
avg_confidence = {}
for label in event_counts:
    total_weight_from_clicks = sum([c * 2 for t, l, c in data_stream if t == 'click' and l == label])
    avg_confidence[label] = total_weight_from_clicks / (event_counts[label] * 2) if event_counts[label] > 0 else 0

# Normalize weights using min-max scaling (semi-relevant processing)
all_weights = list(event_weights.values())
min_w = min(all_weights)
max_w = max(all_weights)

scaled_scores = {}
for label, weight in event_weights.items():
    scaled_scores[label] = (weight - min_w) / (max_w - min_w) if max_w != min_w else 0.0

# Apply domain-specific boost for labels with high consistency
consistency_bonus = {}
for label in event_weights:
    raw_clicks = [c for t, l, c in data_stream if t == 'click' and l == label]
    if len(raw_clicks) > 1:
        variance = sum((c - sum(raw_clicks)/len(raw_clicks))**2 for c in raw_clicks) / len(raw_clicks)
        consistency_bonus[label] = 0.3 if variance < 0.02 else 0.05
    else:
        consistency_bonus[label] = 0.0

# Combine scaled score with bonus
hybrid_scores = {lbl: scaled_scores[lbl] + consistency_bonus[lbl] for lbl in scaled_scores}

# Misleading transformation (dead-end computation)
duplicate_transformation = {
    k: v ** 2 + 0.1 for k, v in hybrid_scores.items()  # Not used later
}

# Simulate A/B test conversion baseline (irrelevant)
baseline_conversion_rate = 0.124
expected_lift = {'A': 0.08, 'B': 0.05, 'C': 0.03}

# Process data into structured format
processed_data = []
for label in ['A', 'B', 'C']:
    entry = {
        'label': label,
        'raw_weight': event_weights[label],
        'avg_click_conf': avg_confidence.get(label, 0),
        'score': hybrid_scores.get(label, 0),
        'count': event_counts[label]
    }
    processed_data.append(entry)

# Faux machine learning model output (distraction)
predicted_conversion = {}
for item in processed_data:
    pred = item['score'] * 0.4 + item['avg_click_conf'] * 0.3
    predicted_conversion[item['label']] = round(pred, 3)

# Core calculation function
def calculate_final_score(data_entries):
    total = 0.0
    count = 0
    for entry in data_entries:
        if entry['count'] > 0:  # Only consider labels with at least one click
            adjusted = entry['score'] * (1 + entry['avg_click_conf'])
            total += adjusted
            count += 1
    return int(round(total * 100)) if count > 0 else 0

# Execute main logic
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Target result: {final_score}")