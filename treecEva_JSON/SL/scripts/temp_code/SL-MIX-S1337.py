import math
from itertools import combinations

# Login attempt data: [hour_of_day, username_complexity, ip_diversity, session_duration_minutes]
login_attempts = [
    [3, 8, 2, 15],
    [17, 5, 1, 3],
    [22, 12, 3, 45],
    [6, 7, 1, 2],
    [14, 9, 2, 20]
]

# Initialize scoring components
hour_risk_factors = {h: math.sin(h * math.pi / 12) for h in range(24)}
credential_variety_bonus = {}
session_anomaly_flags = []

# Process login attempts
for attempt in login_attempts:
    hour, complexity, diversity, duration = attempt
    
    # Hour-based risk calculation with short-circuit evaluation
    time_risk = hour_risk_factors[hour] if hour_risk_factors[hour] > 0 else 0
    
    # Credential variety tracking
    if complexity > 7 and diversity > 1:
        credential_variety_bonus[complexity] = credential_variety_bonus.get(complexity, 0) + diversity
    
    # Session anomaly detection
    session_anomaly_flags.append(duration < 5 or (duration > 60 and complexity < 10))

# Calculate behavioral pattern scores using combinatorics
pairwise_complexity_scores = [
    abs(a - b) for a, b in combinations(
        [attempt[1] for attempt in login_attempts], 2)
]

# Compute aggregate metrics
average_pairwise_score = sum(pairwise_complexity_scores) / len(pairwise_complexity_scores) if pairwise_complexity_scores else 0
high_risk_sessions = sum(session_anomaly_flags)
cred_bonus_total = sum(v * k for k, v in credential_variety_bonus.items())

# Final suspicion index calculation
aggregate_suspicion_index = (
    round(sum(hour_risk_factors[h] for h, _, _, _ in login_attempts) * 100) +
    int(average_pairwise_score * 10) +
    high_risk_sessions * 15 -
    cred_bonus_total // 2
)

print(f"Result: {aggregate_suspicion_index}")