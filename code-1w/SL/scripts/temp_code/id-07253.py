def analyze_trend(data):
    if not data:
        return 0
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    trend_score = avg * (1 - variance / (avg + 1))
    return round(trend_score, 2)

# Simulate employee weekly output over 4 weeks
task_logs = [22, 19, 25, 21]
productivity = analyze_trend(task_logs)

# Irrelevant distraction: simulate unrelated environmental metric
temperature_readings = [23.5, 24.1, 22.9, 25.0]
climate_stability = sum(temperature_readings) / len(temperature_readings)

# Risk assessment based on error rates
error_rates = [0.03, 0.07, 0.02, 0.05]
mean_error = sum(error_rates) / len(error_rates)
risk_factor = mean_error * 100 if mean_error > 0.04 else 0

# Dummy string processing to add interference using string methods
status_flags = ['OK', 'WARNING', 'OK', 'CRITICAL']
flag_summary = ', '.join(status_flags).lower()
alert_count = flag_summary.count('warning') + flag_summary.count('critical')

# Conditional expression and auxiliary logic
base_efficiency = 85 if productivity >= 20 else 70
bonus_eligibility = 'Yes' if alert_count == 0 and risk_factor < 5 else 'No'

# Core computation chain with nested logic
scaling_factor = 1.2 if bonus_eligibility == 'Yes' else 0.8
adjusted_productivity = productivity * scaling_factor
penalty = 10 if risk_factor >= 5 else 0

# Final evaluation incorporating multiple concepts
def evaluate_performance(prod, risk):
    base = prod * 3.5
    risk_penalty = 20 if risk > 4 else 5
    performance_level = 'High' if prod > 20 else 'Medium'
    multiplier = 1.5 if performance_level == 'High' else 1.0
    
    # Additional distraction: unused recursive helper
    def calculate_depth(n):
        return 1 + calculate_depth(n-1) if n > 0 else 0
    
    # Distractor: dead code path
    if False:
        debug_value = base ** 2
        return -1
    
    intermediate = base * multiplier - risk_penalty
    final = max(intermediate, 10)  # Ensure minimum threshold
    return int(final)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")