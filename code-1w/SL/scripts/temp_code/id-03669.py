def analyze_conditions(temps):
    hot_days = {t for t in temps if t > 30}
    cold_days = {t for t in temps if t < 10}
    return len(hot_days) > len(cold_days)

baseline = [25, 20, 35, 5, 31, 12]
readings = [22, 33, 8, 40, 15, 28, 36]

# Irrelevant transformation
shifted = [x - 1 for x in readings if x % 2 == 0]
dummy_sum = sum(shifted) * 0.5

status_flags = [True if x > 25 else False for x in readings]
active_count = status_flags.count(True)

# Misleading intermediate calculation
temp_variance = (max(readings) - min(readings)) // 2
adjustment_factor = temp_variance if temp_variance > 15 else 10

# Conditional expression with distractor logic
day_type = 'extreme' if analyze_conditions(baseline + readings) else 'normal'
penalty = 5 if day_type == 'extreme' and len(baseline) % 2 == 0 else 0

# Core logic embedded with noise
valid_readings = [r for r in readings if r >= 15]
raw_total = sum(valid_readings)
reading_bonus = 10 if len(valid_readings) >= 4 else 5

# Key function with mixed concerns
def calculate_performance(base, data):
    base_above_avg = len([b for b in base if b > sum(base)/len(base)])
    data_efficiency = len(data) * 2 if raw_total > 100 else len(data)
    # Distractor: unused local
    shadow_value = base_above_avg * 3
    return data_efficiency + reading_bonus - penalty

# Execution point of interest
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")