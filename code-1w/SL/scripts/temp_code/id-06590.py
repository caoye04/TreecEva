def analyze_productivity(logs):
    total_chars = sum(len(entry) for entry in logs)
    entry_count = len(logs)
    avg_length = total_chars / entry_count if entry_count else 0

    # Irrelevant statistics (distractors)
    uppercase_ratio = sum(c.isupper() for entry in logs for c in entry) / total_chars if total_chars else 0
    digit_percentage = sum(c.isdigit() for entry in logs for c in entry) / total_chars * 100 if total_chars else 0

    return avg_length, entry_count

# Simulated contribution logs
team_logs = [
    "Completed task: Data validation and sanitization",
    "Fixed critical bug in payment processing module",
    "Refactored legacy codebase for improved readability",
    "Added unit tests for authentication layer",
    "Optimized database queries reducing latency by 40%"
]

# Extract key metrics
avg_len, entries = analyze_productivity(team_logs)

# Core productivity signal
contribution_weight = sum(len(s.split()) for s in team_logs)  # Word count across logs

# Secondary metric with partial relevance
char_sum = sum(ord(s[0]) for s in team_logs if len(s) > 0) % 100

# Complex but mostly irrelevant transformation chain
transformed = list(map(lambda x: x ** 2 % 17, [len(s) for s in team_logs]))
aggregated = sum(transformed[i] * (i + 1) for i in range(len(transformed)))
scaled_noise = round(aggregated / 10.0, 3)

# Real calculation begins here
base_score = contribution_weight * 2.5
penalty_factor = min(entries, 10) * 0.1  # Max penalty from size

# Destructuring assignment (relevant)
bonus_multiplier, adjustment = (1.2, 0.8) if avg_len > 40 else (1.0, 1.0)

# Actual scoring logic buried among distractions
def calculate_rating(contribs, penalty):
    raw = base_score - (penalty * 100)
    if contribs > 30:
        raw += 25
    return int(raw * bonus_multiplier + adjustment)

# Critical statement
final_score = calculate_rating(contribution_weight, penalty_factor)

# Print result as required
print(f"Result: {final_score}")