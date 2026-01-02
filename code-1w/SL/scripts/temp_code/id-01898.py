def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted_metrics = [x * 1.1 for x in metrics if x > baseline]
    return set(adjusted_metrics)

productivity = [85, 90, 78, 92, 88, 76, 95]

# Irrelevant computation on a subset
filtered_data = [x for x in productivity if x >= 80]
buffer_value = sum(filtered_data[::2]) * 0.5  # Slicing and partial use

threshold = 85
exceedance_count = 0
for i in range(len(productivity)):
    if productivity[i] > threshold:
        exceedance_count += 1

# Create a risk profile using set operations
risk_candidates = {x + 1 for x in productivity}
risk_adjustments = {x - 2 for x in productivity if x % 2 == 0}
risk_set = risk_candidates.intersection(risk_adjustments)

staging_score = len(risk_set) * 3.5
offset_correction = buffer_value / (exceedance_count + 1)

def evaluate_performance(efficiency, risk_profile):
    raw_score = sum(efficiency) / 10
    penalty = len(risk_profile) * 0.8
    bonus = 5 if len(efficiency) > 6 else 0
    return raw_score - penalty + bonus + 2  # Final formula includes constant

# Key execution point
final_score = evaluate_performance(productivity, risk_set)
print(f"Target result: {final_score}")