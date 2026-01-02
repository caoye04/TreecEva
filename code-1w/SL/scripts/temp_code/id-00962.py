def analyze_trend(values):
    trend = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
    volatility = sum(abs(values[i] - values[i-1]) for i in range(1, len(values)))
    return trend, volatility

# Simulated system health metrics over time
time_series_data = [85, 87, 83, 90, 92, 88, 95, 96]
base_load = 75
trend_strength, fluctuation = analyze_trend(time_series_data)

# Redundant transformation (distractor)
transformed = [x ** 0.5 for x in time_series_data if x > 80]
decay_factor = sum(transformed) / len(transformed) if transformed else 0

# Core logic with distractors
metrics = {
    'peak': max(time_series_data),
    'stability': len(time_series_data) - fluctuation // 10,
    'consistency': trend_strength * 2,
    'baseline': base_load
}

threshold = 88
penalty_rate = 0.8
bonus_granted = False

# Misleading conditional branch (dead code path)
if decay_factor < 5:
    bonus_granted = True  # Never reached due to data
else:
    adjustment = -5

# Main processing with list comprehension and conditionals
def process_performance(met, thresh):
    score_components = [
        met['peak'] * 0.4,
        met['stability'] * 1.2 if met['peak'] >= thresh else met['stability'] * 0.7,
        met['consistency'] ** 1.1
    ]
    
    # Distractor computation
    overhead = sum(x % 7 for x in range(int(met['baseline']))) % 13
    temp_offset = (overhead * 0.3) if met['baseline'] > 70 else 0
    
    raw_score = sum(score_components) + temp_offset
    
    # Final adjustment independent of temp_offset
    final = int(raw_score - (10 if met['stability'] < 15 else 0))
    
    return final

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")