def analyze_feedback(texts, min_length=5):
    stats = {}
    long_count = 0
    vowel_ratio_sum = 0.0
    for t in texts:
        clean = t.strip().lower()
        if len(clean) > min_length:
            long_count += 1
            vowels = sum(1 for c in clean if c in 'aeiou')
            vowel_ratio_sum += vowels / len(clean)
    avg_vowel_ratio = vowel_ratio_sum / long_count if long_count > 0 else 0
    return long_count, avg_vowel_ratio

feedback = [
    "Excellent work on the project!",
    "needs improvement in communication",
    "Outstanding presentation skills",
    "  unclear and disorganized approach  ",
    "good but late submission"
]

# Irrelevant preprocessing - distractor
processed = [f.upper().replace('!', '').replace('.', '') for f in feedback]
duplicate_check = {p: processed.count(p) for p in processed}

# Character counting and filtering - semi-relevant
char_freq = {}
for p in processed:
    for c in p:
        char_freq[c] = char_freq.get(c, 0) + 1

# Misleading analysis branch (dead-end)
if len(processed) > 10:
    rare_chars = [c for c, cnt in char_freq.items() if cnt < 2]
else:
    rare_chars = []  # This path doesn't contribute

# Actual logic begins here
count_long, avg_vowels = analyze_feedback(feedback, min_length=20)

# Simulate performance metrics
threshold = 0.15
weight_a = 0.6 if avg_vowels > 0.1 else 0.3
weight_b = 0.4

# Secondary metric based on string methods
exclamation_count = sum(1 for f in feedback if f.strip().endswith('!'))
engagement_score = exclamation_count * 10

# Dummy state tracking - distractor
state_log = []
for i, f in enumerate(feedback):
    if i % 2 == 0:
        state_log.append(f"reviewed_{i}")
    else:
        state_log.append(f"skipped_{i}")

# Core evaluation logic
base_score = count_long * 25
adjustment = (avg_vowels * 100) if count_long > 0 else 0
final_score = base_score + adjustment

# Additional irrelevant transformation
normalized = final_score / (len(state_log) or 1)
squared_error = (threshold - avg_vowels)**2  # Unused

# Output target result
print(f"Result: {final_score}")