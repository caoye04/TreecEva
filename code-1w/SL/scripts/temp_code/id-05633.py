def analyze_feedback(reviews):
    sentiment_score = 0
    for i, review in enumerate(reviews):
        if len(review) > 10:
            sentiment_score += 1 if 'good' in review else (-1 if 'poor' in review else 0)
    return sentiment_score

reviews = ['very good service', 'poor response time', 'excellent staff', 'average experience', 'good effort']
sentiment = analyze_feedback(reviews)

# Irrelevant preprocessing block (dead path)
def normalize_data(data):
    max_val = max(data)
    return [x / max_val for x in data]

temp_readings = [23.5, 24.1, 22.8, 25.0]
normalized_temps = normalize_data(temp_readings)  # Unused

# Core metric computation with distractions
base_metrics = [85, 76, 92, 68, 77]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distractor: unused transformation
shifted_metrics = [x + 5 for x in base_metrics if x < 70]
expanded_weights = [w * 2 for w in weights][::2]  # Not used

# Misleading intermediate calculation
aggregate = sum([m * w for m, w in zip(base_metrics, weights)]) / len(weights)
penalty_factor = 0.9 if sentiment < 0 else 1.0
adjusted_aggregate = aggregate * penalty_factor  # Looks important, but not final

# Another red herring: conditional expression with no impact
status = 'passing' if adjusted_aggregate >= 75 else 'failing'
diagnostic_log = f'Student performance is {status}'  # Dead variable

# Real logic begins here — nested and obscured
secondary_bonus = 0
for idx, (metric, weight) in enumerate(zip(base_metrics, weights)):
    if idx % 2 == 0 and metric > 80:
        secondary_bonus += weight * 3

# Simulate complex weighting adjustment (actually unused)
counterfactual_weights = [w + 0.05 * (idx % 2) for idx, w in enumerate(weights)]

# Actual key function with embedded logic
metrics = [b + (5 if b < 70 else 0) for b in base_metrics]  # Boost low performers

def evaluate_performance(mets, wts):
    total = 0.0
    bonus_applied = False
    for i, (m, w) in enumerate(zip(mets, wts)):
        contribution = m * w
        total += contribution
        
        # Conditional expression usage
        adjustment = 2.5 if (i % 3 == 0 and contribution > 20) else 0
        total += adjustment
        
        if m > 90 and not bonus_applied:
            total += 10
            bonus_applied = True  # Only once
            
        # Bit manipulation distraction
        flag = (i << 2) ^ 5
        if flag > 10:  # Always true for i >= 1, but irrelevant
            total -= 0.5  # Cancelled out later

    # Final correction: neutralize bit manipulation side effect
    total += 0.5 * (len(mets) - 1)  # Compensates previous subtraction
    return total

# Critical statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")