def analyze_pattern(seq):
    """Irrelevant helper function for signal processing (dead code path)"""
    return [x * 2 for x in seq if x > 5]


def validate_checksum(data):
    """Unused validation function — red herring"""
    return sum(data) % 7 == 0

# Simulated sensor readings over time (irrelevant data)
sensor_log = [15, 23, 18, 47, 9, 12, 31, 44, 52, 63, 29, 33]

# Misleading intermediate computation (distractor)
total_power_draw = sum([x ** 2 for x in sensor_log if x % 3 == 0])

# Actual relevant data: patient health metrics across 7 days
health_data = [0.81, 0.74, 0.92, 0.68, 0.79, 0.83, 0.77]

# Thresholds for warning levels (used in final computation)
thresholds = {
    'warning_low': 0.75,
    'critical_low': 0.65,
    'optimal_high': 0.85
}

# Irrelevant set operations (distraction with meaningful syntax)
day_indices = set(range(len(health_data)))
weekend_days = {5, 6}
high_risk_days = day_indices - weekend_days  # Unused

# Auxiliary transformation (partially relevant but misleading)
normalized_offsets = [round(abs(x - 0.75), 3) for x in health_data]

# Bitwise decoy: simulates low-level check (never used)
status_flag = 0b1010
mask = 0b1100
masked_status = status_flag & mask  # Distractor variable

# Conditional logic with red herring branches
alert_level = "green"
if len(health_data) > 10:
    alert_level = "caution"  # Dead branch
elif sum(health_data) / len(health_data) < thresholds['warning_low']:
    alert_level = "elevated"  # Not triggered
else:
    alert_level = "stable"  # This executes

# Key data transformation: find days below warning threshold
low_days = [i for i, val in enumerate(health_data) if val < thresholds['warning_low']]

# Compute rolling 3-day average (partially irrelevant)
rolling_avgs = []
for i in range(2, len(health_data)):
    avg = sum(health_data[i-2:i+1]) / 3
    rolling_avgs.append(round(avg, 3))

# Unused sorting operation (distractor)
sorted_rolling = sorted(rolling_avgs, reverse=True)

# Critical computation begins here — real logic chain
baseline_ref = thresholds['warning_low']
effective_deviation = 0

for i, measurement in enumerate(health_data):
    if measurement < baseline_ref:
        # Accumulate weighted deviation only on low days
        effective_deviation += (baseline_ref - measurement) * (i + 1)  # Weight by day index

# Secondary metric: count of improving trends
improvement_count = 0
for i in range(1, len(health_data)):
    if health_data[i] > health_data[i-1]:
        improvement_count += 1

# Tertiary: use slicing to analyze last half of week
recent_trend = health_data[4:]
strong_days = len([x for x in recent_trend if thresholds['warning_low'] <= x <= thresholds['optimal_high']])

# Complex conditional expression with tuple unpacking (actual key logic)
primary_score = effective_deviation * 100
adjustment_factor = improvement_count if strong_days >= 2 else -improvement_count

# Use of zip and enumerate together — actual relevant step
weekly_analysis = []
for idx, (day_val, roll_val) in enumerate(zip(health_data, [0] + rolling_avgs)):\n    weekly_analysis.append((idx, round(day_val * roll_val, 4) if idx > 0 else 0))

# Final aggregation using set and slicing (real usage)
analysis_sum = sum([val for _, val in weekly_analysis[1::2]])  # Every other analysis result

# Core formula: combines arithmetic, conditional logic, and prior metrics
diagnostic_base = primary_score + (adjustment_factor * 10) + analysis_sum

# Final adjustment based on optimal range inclusion
optimal_inclusion = len([x for x in health_data if x > thresholds['optimal_high']])
bonus = 25 if optimal_inclusion >= 2 else (10 if optimal_inclusion == 1 else 0)

# Key statement containing answer
final_diagnostic = int(diagnostic_base + bonus)

print(f"Result: {final_diagnostic}")