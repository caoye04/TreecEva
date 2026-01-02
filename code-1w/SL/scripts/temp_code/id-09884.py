def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]

# Simulated system metrics (distraction)
system_load = [0.4, 0.6, 0.8, 0.3, 0.9]
decoy_result = analyze_efficiency(system_load)

# Core task: Evaluate algorithmic trading strategy performance
initial_capital = 10000
trades = [(100, 1.05), (200, 0.98), (150, 1.02), (300, 1.01)]
portfolio_values = []

for amount, multiplier in trades:
    portfolio_values.append(initial_capital + amount * multiplier)

# Distractor: unused accumulation
running_total = sum(portfolio_values)
buffer_data = [round(v % 100) for v in portfolio_values]

# Real logic begins: risk-adjusted metric computation
raw_returns = [((v - initial_capital) / initial_capital) for v in portfolio_values]
volatility = sum(abs(r) for r in raw_returns) / len(raw_returns)

# Apply artificial dampening factor (red herring)
dampened_returns = [r * 0.95 for r in raw_returns]
unused_shadow_copy = dampened_returns.copy()

# Weighted scoring using tuples and enumeration (core concept)
metrics = (volatility, raw_returns[-1], len(trades))
weights = (0.3, 0.5, 0.2)

# Misleading intermediate calculation
pseudo_metric = sum(m * w for m, w in zip(metrics, (0.1, 0.1, 0.8)))

# Critical distractor: fake evaluation path
def evaluate_performance_wrong(metrics, weights):
    return sum(m ** 2 for m in metrics) // len(weights)

# Actual evaluation function
def evaluate_performance(metrics, weights):
    score = 0.0
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i == 0:
            # Volatility penalty
            score += (1 - metric) * weight * 100
        elif i == 1:
            # Last return bonus
            score += max(0, metric) * weight * 200
        else:
            # Trade frequency incentive
            adjustment = 10 if metric >= 3 else -5
            score += adjustment * weight
    
    # Hidden correction: offset artificial inflation
    correction_factor = 0.9
    score *= correction_factor
    
    # Decoy mutation
    temp_score = score + 50  # never used
    
    return int(score)

# Unused alternative logic path
if len(portfolio_values) > 5:
    final_score = 0
else:
    final_score = evaluate_performance(metrics, weights)

# Additional red herring: string-based decoy
status_log = "Execution completed: PASS"
log_chars = [c for c in status_log if c.isalpha()]
char_count = len(log_chars)

# Final irrelevant set operation
distinct_letters = set(log_chars)
filtered_letters = {c for c in distinct_letters if c in 'AEIOU'}

# Correct output
print(f"Result: {final_score}")