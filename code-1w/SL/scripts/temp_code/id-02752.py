def analyze_efficiency(logs):
    total_entries = len(logs)
    uppercase_count = 0
    digit_lines = 0
    for log in logs:
        if log.isupper():
            uppercase_count += 1
        if any(char.isdigit() for char in log):
            digit_lines += 1
    efficiency = (uppercase_count + digit_lines) / total_entries if total_entries else 0
    return efficiency

logs = [
    "SYSTEM REBOOT INITIATED",
    "error code 404",
    "DATA STREAM ACTIVE",
    "warning: low memory",
    "BACKUP COMPLETE"
]

raw_data = [l.strip().lower() for l in logs]
decoded = [d.replace(" ", "_").title() for d in raw_data]

# Intermediate metrics with partial relevance
baseline = sum(len(d) for d in decoded) / len(decoded) if decoded else 0
adjusted_baseline = baseline * 0.9 + 0.1

productivity = analyze_efficiency(logs)
risk_factor = len([d for d in decoded if "Error" in d or "Warning" in d])

# Misleading calculation path (not directly used but looks relevant)
temp_analysis = []
for d in decoded:
    score = 0
    if "System" in d:
        score += 10
    if "Backup" in d:
        score += 5
    temp_analysis.append(score)
aggregate_temp = sum(temp_analysis)

# Core logic hidden among distractions
def evaluate_performance(p, r):
    if p > 0.5:
        return int((p * 100) - (r * 5))
    else:
        return int((p * 50) - (r * 10))

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")