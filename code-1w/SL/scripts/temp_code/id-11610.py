def process_attendance(record):
    # Convert raw string record to structured attendance data
    entries = record.strip().split(',')
    parsed = []
    for entry in entries:
        cleaned = entry.strip().lower()
        if 'late' in cleaned:
            parsed.append(0.5)
        elif 'absent' in cleaned:
            parsed.append(0.0)
        else:
            parsed.append(1.0)  # present
    return parsed

# Base transformation matrix (unused red herring)
transform_matrix = [[1.1, -0.1], [-0.2, 1.2]]
dummy_weight = sum(sum(row) for row in transform_matrix)

base_threshold = 0.75
tolerance_buffer = 0.1  # Not used in final logic

attendance_log = "Present, Late, Present, Present, Absent, Late, Present"

# Preprocess the log
raw_scores = process_attendance(attendance_log)

# Irrelevant statistical tracking (distractor variables)
max_possible = len(raw_scores)
actual_present = sum(1 for s in raw_scores if s == 1.0)
lateness_count = sum(1 for s in raw_scores if s == 0.5)

# Compute adjusted average with hidden rule: only full presence counts fully
adjusted_average = sum(score * 2 if score == 1.0 else score for score in raw_scores) / len(raw_scores)

# Secondary scaling factor based on pattern detection
pattern_flag = False
for i in range(len(raw_scores) - 2):
    if raw_scores[i] == 1.0 and raw_scores[i+1] == 0.5 and raw_scores[i+2] == 0.0:
        pattern_flag = True

bonus_multiplier = 1.2 if pattern_flag else 1.0  # Unused due to override below

# Override mechanism based on string characteristics
log_chars = attendance_log.replace(',', '').replace(' ', '')
vowel_count = sum(1 for c in log_chars if c in 'aeiou')
consonant_ratio = (len(log_chars) - vowel_count) / len(log_chars) if len(log_chars) > 0 else 0

# Critical decision gate
if consonant_ratio > 0.6:
    bonus_multiplier = 1.1
else:
    bonus_multiplier = 1.05

# Additional distraction: recursive smoothing (not affecting final result)
def smooth(values, depth=0):
    if depth >= 2 or len(values) == 0:
        return values[0] if values else 0
    new_vals = [(values[i] + values[(i+1)%len(values)]) / 2 for i in range(len(values))]
    return smooth(new_vals, depth + 1)

smoothed_anchor = smooth(raw_scores)

# Core evaluation logic
penalty_factor = 0.9 if adjusted_average < base_threshold else 1.0

# Final performance function
def evaluate_performance(records, threshold):
    total = sum(records)
    count = len(records)
    avg = total / count
    
    # Hidden weighting: consecutive full attendance gives bonus
    streak_bonus = 0
    current_streak = 0
    for r in records:
        if r == 1.0:
            current_streak += 1
        else:
            if current_streak >= 3:
                streak_bonus += 0.5
            current_streak = 0
    if current_streak >= 3:
        streak_bonus += 0.5
    
    base_score = avg * 100
    applied_bonus = base_score * bonus_multiplier
    after_penalty = applied_bonus * penalty_factor
    final_raw = after_penalty + streak_bonus * 10
    
    # Normalize to integer scale
    return int(final_raw)

# Key execution point
final_score = evaluate_performance(raw_scores, base_threshold)

# Distractor computation: unused complexity
idle_cycles = 0
for i in range(int(smoothed_anchor * 10)):
    idle_cycles += (i % 3) ** 2

Result: {final_score}