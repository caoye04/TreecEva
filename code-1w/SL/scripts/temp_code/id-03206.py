def calculate_final_score(raw_marks, extra_bonus):
    base_score = sum([mark for mark in raw_marks if mark >= 50])
    adjustment = 10 if len(raw_marks) > 4 else 5
    bonus_multiplier = 2 if extra_bonus else 1
    scaled_bonus = adjustment * bonus_multiplier
    return base_score + scaled_bonus

# Student exam marks and performance flags
marks = [45, 82, 77, 53, 68, 41]
is_honors_track = True
project_completed = True
bonus_earned = project_completed and is_honors_track

final_score = calculate_final_score(marks, bonus_earned)
print(f"Result: {final_score}")