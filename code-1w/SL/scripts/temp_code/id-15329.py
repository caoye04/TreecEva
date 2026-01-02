def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 0.5
    return trend_score

# Simulate system performance metrics over time
raw_logs = "ERROR|INFO|WARNING|INFO|INFO|ERROR|CRITICAL|INFO"
log_levels = raw_logs.split('|')
error_count = sum(1 for level in log_levels if level in ['ERROR', 'CRITICAL'])
warnings_ignored = len([x for x in log_levels if x == 'WARNING']) * 0.5

# Extract performance snapshots (simulated as numeric values)
performance_data = [95, 88, 92, 87, 90, 85, 88, 84]
smoothed_data = [performance_data[i] for i in range(0, len(performance_data), 2)]  # Every other reading

# Calculate base metrics
trend_analysis = analyze_trend(performance_data)
base_efficiency = sum(smoothed_data) / len(smoothed_data)

# Auxiliary distraction: irrelevant string processing
log_summary = ''.join([level[0] for level in log_levels])
stability_flag = log_summary.find('E') if 'CRITICAL' in log_levels else -1
phantom_cycle = len(log_summary.replace('I', '')) * 2  # Unused computation

# Key metric computation
metrics = {
    'stability': 100 - error_count * 8,
    'consistency': abs(trend_analysis),
    'efficiency': base_efficiency
}

# Bonus logic with conditional modifier
if metrics['consistency'] >= 4:
    bonus_multiplier = 1.2
else:
    bonus_multiplier = 0.9

unused_projection = metrics['efficiency'] * (1 + metrics['consistency'] / 10)  # Dead calculation

# Core transformation function
def process_performance(met, mult):
    score = 0
    score += met['stability'] * 0.5
    score += met['efficiency'] * 0.3
    score += met['consistency'] * 2
    adjusted = score * mult
    
    # Additional logic to increase reasoning depth
    if adjusted > 70:
        adjusted -= 5
    elif adjusted < 50:
        adjusted += 10
    return round(adjusted, 2)

# Final computation
final_score = process_performance(metrics, bonus_multiplier)
print(f"Result: {final_score}")