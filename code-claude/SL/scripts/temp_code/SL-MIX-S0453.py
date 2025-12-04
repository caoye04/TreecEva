import itertools

# Student test scores processing system
raw_scores = [85, 92, 78, 64, 91, 87, 72]
bonus_points = [2, 0, 5, 3, 1, 0, 4]

# Some metadata about the exams (not directly used for final calculation)
exam_weights = [0.15, 0.25, 0.20, 0.10, 0.30]
exam_dates = ['2023-01-15', '2023-02-10', '2023-03-05', '2023-03-25', '2023-04-15']

# Process scores with bonuses
processed_scores = []
for i, (score, bonus) in enumerate(zip(raw_scores, bonus_points)):
    adjusted = score + bonus
    # Apply scaling factor based on position (not actually used)
    scaling = (i % 3) * 0.05 + 1
    # Track both scaled and unscaled versions
    processed_scores.append((adjusted, adjusted * scaling))

# Filter out scores below threshold
threshold = 75
valid_scores = []
invalid_count = 0

# Track statistics as we go (some are just for monitoring)
total = 0
max_score = 0
min_score = 100

for base_score, scaled_score in processed_scores:
    # We'll use the base_score for our final calculation
    if base_score >= threshold:
        valid_scores.append(base_score)
        total += base_score
        max_score = max(max_score, base_score)
        min_score = min(min_score, base_score)
    else:
        invalid_count += 1
        # Convert to uppercase (unused operation)
        note = f"SCORE {base_score} BELOW THRESHOLD"

# Analyze pairs of consecutive scores (not used in final result)
pair_diffs = []
for s1, s2 in itertools.pairwise(valid_scores):
    pair_diffs.append(abs(s2 - s1))

# Calculate average of valid scores
final_score = round(sum(valid_scores) / len(valid_scores), 2)

# Extra calculations that don't affect the result
range_value = max_score - min_score
median_candidate = sorted(valid_scores)[len(valid_scores) // 2]

print(f"Result: {final_score}")