def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted = [x * 1.1 for x in metrics if x < baseline]
    return sum(adjusted) if adjusted else baseline

productivity = [85, 90, 78, 92, 88]

# Distractor: irrelevant historical data
historical_data = [76, 85, 72, 91, 87]
decay_weights = [0.9**i for i in range(len(historical_data))]
historical_trend = sum(historical_data[i] * decay_weights[i] for i in range(len(historical_data)))

# Real computation begins
current_efficiency = analyze_efficiency(productivity)

# Bitwise manipulation as part of risk assessment (semi-relevant)
raw_risk = 0
for val in productivity:
    raw_risk ^= int(val % 7)  # XOR-based accumulation of modulo residues

risk_factor = raw_risk | 3  # Add base risk floor

# String-based validation flag (uses slicing and conditionals)
status_flags = ['HIGH', 'MEDIUM', 'LOW']
performance_status = status_flags[0] if current_efficiency > 85 else status_flags[1]
status_code = f"{performance_status[:3].lower()}_01"

# Conditional expression with distractor variables
threshold = 80 + (5 if 'high' in status_code else -5)
bonus_applied = True if current_efficiency >= threshold else False

# Core evaluation logic
masking_factor = 0.85 if bonus_applied else 1.0
adjusted_productivity = current_efficiency * masking_factor

# Secondary distractor: unused helper calculation
redundant_calc = ''.join([chr(97 + (i % 26)) for i in range(10)])  # generates 'abcdefghij'
char_count = len(redundant_calc.replace('a', '').replace('e', ''))  # just distraction

# Final scoring with tuple unpacking and logical chaining
def evaluate_performance(efficiency, risk):
    scaling = 1.2 if efficiency > 85 else 1.0
    penalty = 2 if risk & 1 else 0  # bitwise check on risk parity
    
    # Multiple assignments to increase cognitive load
    temp_a, temp_b = efficiency * scaling, risk * 10
    intermediate = temp_a - penalty * 5
    
    # More distraction: unused path
    if intermediate < 0:
        fallback = (efficiency, risk)
        temp_b += fallback[1]
    
    # Actual result
    score = int(intermediate - temp_b * 0.1)
    return score

# Key statement
final_score = evaluate_performance(current_efficiency, risk_factor)
print(f"Result: {final_score}")