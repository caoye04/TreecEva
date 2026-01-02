def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) / len(adjusted) if adjusted else 0

productivity = [45, 70, 60, 80, 55]
baseline = sum([p // 10 for p in productivity])

# Distractor: Irrelevant trend analysis
trend_weights = [1.05, 0.98, 1.02]
predicted_trend = [baseline * w for w in trend_weights]
smoothed_trend = sum(predicted_trend) / len(predicted_trend)

threshold = 65
exceedance_count = len([p for p in productivity if p >= threshold])
penalty_rate = 0.1 if exceedance_count > 3 else 0.2

# Simulate risk adjustment based on volatility
volatility = max(productivity) - min(productivity)
risk_factor = volatility * 0.05 if volatility > 25 else 10

# Auxiliary computation - partially relevant but overcomplicated
efficiency_score = analyze_efficiency(productivity)
base_performance = efficiency_score * 0.7 + (sum(productivity) / len(productivity)) * 0.3

# Introduce red herring with unused helper
def calculate_synergy(a, b):
    return (a + b) * 0.5  # Never called

# Another distraction: dead code path
if False:
    backup_metric = baseline ** 2
    risk_factor += backup_metric

# Core logic embedded in noise
def evaluate_performance(p, r):
    raw_score = sum(p) / len(p)
    adjustment = 1 - (r / 100)
    temp_result = raw_score * adjustment
    
    # Additional step to increase inference depth
    if temp_result > 60:
        temp_result *= 0.95
    else:
        temp_result *= 1.05
    
    return round(temp_result, 2)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")