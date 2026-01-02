def analyze_feedback(ratings):
    avg_rating = sum(ratings) / len(ratings)
    adjusted = [r * 1.1 if r >= 4 else r * 0.9 for r in ratings]
    return sum(adjusted) / len(adjusted)

# Irrelevant function - decoy
def compute_network_latency(packets, distance):
    base = 0.05
    penalty = 0 if distance < 1000 else (distance - 1000) * 0.001
    return base + penalty

# Unused helper
def normalize_string(s):
    return s.strip().lower().replace('_', ' ').title()

# Main data processing chain
def transform_metrics(data_str):
    parts = data_str.split(',')
    values = [float(x.strip()) for x in parts]
    squared = [v ** 2 for v in values]
    filtered = [s for s in squared if s > 10]
    return filtered

# Simulate system health score (distractor)
system_health = 0
for i in range(5):
    system_health += (i * 2.5) % 3
system_health = round(system_health, 2)

# Real computation begins
raw_input = "3.2, 4.1, 2.8, 5.0, 3.9"
tokenized = raw_input.split(',')
initial_scores = [float(x) for x in tokenized]

# Apply weighting based on recency (older = less weight)
weights = [0.7, 0.8, 0.9, 1.0, 0.95]
weighted_scores = [score * weights[i] for i, score in enumerate(initial_scores)]

# Boost high performers
boosted = [s * 1.2 if s >= 4.5 else s * 1.05 for s in weighted_scores]

# Normalize using min-max scaling
min_val, max_val = min(boosted), max(boosted)
normalized = [(x - min_val) / (max_val - min_val) * 100 for x in boosted]

# Aggregate via harmonic mean (more sensitive to low values)
def harmonic_mean(values):
    if 0 in values:
        return 0
    return len(values) / sum(1/v for v in values)

aggregated = harmonic_mean(normalized)

# Feedback loop adjustment
feedback_ratings = [4, 5, 3, 4, 4]
external_adjustment = analyze_feedback(feedback_ratings)

# Final transformation with conditional logic
dynamic_modifier = 1.15 if external_adjustment > 4.0 else 0.95
interim_result = aggregated * dynamic_modifier

# Secondary adjustment based on string analysis (uses string method)
status_tag = "PERFORMANCE_EXCELLENT"
correction_factor = 0.98 if "EXCELLENT" in status_tag else 1.02

# Critical execution point
final_score = interim_result * correction_factor

# Dead code path (never executed)
if False:
    backup_system = [1, 2, 3]
    for x in backup_system:
        final_score -= x

# Print result as required
print(f"Result: {final_score}")