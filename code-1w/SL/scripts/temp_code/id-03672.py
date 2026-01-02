def analyze_trend(data):
    positive_changes = 0
    negative_changes = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            positive_changes += 1
        elif data[i] < data[i-1]:
            negative_changes += 1
    return positive_changes - negative_changes

# Simulate system performance metrics over time
trend_data = [120, 135, 130, 140, 145, 138, 150]
phantom_offset = sum(x * 2 for x in trend_data if x % 10 == 0)
baseline_shift = len(trend_data) // 2

net_trend = analyze_trend(trend_data)

# Bonus logic based on pattern length
trend_str = ''.join(['U' if trend_data[i] < trend_data[i-1] else 'D' for i in range(1, len(trend_data))])
streak_count = max(len(seg) for seg in trend_str.split('D') + trend_str.split('U')) if trend_str else 0

adjustment_factor = 1.0
if net_trend > 0 and streak_count >= 3:
    adjustment_factor = 1.5

# Hidden calibration (irrelevant to final result)
calibration_set = {x % 7 for x in trend_data}
dummy_accum = 0
for val in calibration_set:
    dummy_accum += val ** 2

# Core metric processing
metrics = {
    'base': abs(net_trend),
    'volatility': sum(abs(trend_data[i] - trend_data[i-1]) for i in range(1, len(trend_data))),
    'peak_ratio': max(trend_data) / min(trend_data)
}

bonus_multiplier = adjustment_factor * (1 + streak_count * 0.1)

# Unused distraction variables
temp_scale = round(metrics['peak_ratio'] * 100, 2)
duplicate_check = len(trend_data) != len(set(trend_data))
shadow_bonus = phantom_offset * baseline_shift

# Key computation step
def process_performance(metrs, mult):
    score = metrs['base'] * 10
    if metrs['volatility'] > 50:
        score += 5
    if metrs['peak_ratio'] > 1.1:
        score += 10
    return int(score * mult)

final_score = process_performance(metrics, bonus_multiplier)
print(f"Result: {final_score}")