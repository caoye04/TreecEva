from collections import defaultdict

# Simulate a candidate evaluation system with noise filtering and scoring
baseline = 78.5
candidates = [82.1, 75.3, 90.0, 68.7, 79.4]

# Irrelevant tracking variables (distractors)
assessment_log = defaultdict(int)
evaluation_phase = "initial_screening"
threshold_met_count = 0
normalization_factor = 1.05

# Noise simulation (not actually affecting final result)
noisy_readings = [x * normalization_factor for x in candidates if x > 70]
adjusted_candidates = [x * 0.99 for x in candidates]  # Distractor adjustment

# Real processing begins
valid_scores = [score for score in candidates if score >= 70]  # Filter low scores

# Compute relative performance boost over baseline
boosts = []
for s in valid_scores:
    if s > baseline:
        boosts.append((s - baseline) * 1.2)  # Weighted bonus for above-baseline
    else:
        boosts.append(max(0, (s - baseline) * 0.8))  # Penalty reduction

# Scoring logic with conditional expression
raw_total = sum(boosts)
penalty_applied = len(candidates) > 5 else False
adjustment = -5 if penalty_applied else 0

# Secondary distractor: unused loop
debug_stats = {}
for idx, val in enumerate(candidates):
    debug_stats[idx] = {
        "original": val,
        "deviation": abs(val - baseline),
        "flagged": val < 70
    }

# Core calculation
aggregate_boost = raw_total + adjustment

# Determine ranking category (unused path)
category = "A" if aggregate_boost > 20 else "B" if aggregate_boost > 10 else "C"

# Final scoring with fake complexity
scaling_multiplier = 1.1 if category == "A" else 1.0
interim = aggregate_boost * scaling_multiplier

# Actual answer computation
final_score = int(interim + 17)  # Offset added deterministically

print(f"Result: {final_score}")