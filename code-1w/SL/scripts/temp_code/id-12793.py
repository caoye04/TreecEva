def analyze_efficiency(metrics):
    adjusted = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)
    return [round(x, 2) for x in adjusted]


def compute_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 3)


def extract_peaks(values):
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i-1] < values[i] > values[i+1]:
            peaks.append((i, values[i]))
    return peaks

# Simulated daily productivity scores over a workweek
daily_output = [85, 90, 78, 92, 88]

# Apply efficiency adjustment
efficiency_curve = analyze_efficiency(daily_output)

# Compute volatility as a measure of consistency
consistency_metric = compute_volatility(efficiency_curve)

# Identify peak performance days
peak_days = extract_peaks(efficiency_curve)

# Misleading distraction: unused transformation
temp_transform = [x**2 for x in daily_output if x > 80]
baseline_offset = 5.5
unused_threshold = 75.0

# Risk factors based on inconsistency
risk_factor = 0
if consistency_metric > 5.0:
    risk_factor += 10
elif consistency_metric > 3.0:
    risk_factor += 6
else:
    risk_factor += 3

# Add penalty for low peak frequency
if len(peak_days) < 2:
    risk_factor += 4

# Productivity summary using slicing and zip
recent_three = efficiency_curve[-3:]
projected = [x * 1.05 for x in recent_three]
productivity = sum(projected) / len(projected)

# Combine results using tuple unpacking
data_pair = (productivity, risk_factor)
prod_score, risk_adj = data_pair

# Final performance evaluation
final_score = evaluate_performance(prod_score, risk_adj)

# Dummy function to finalize score
def evaluate_performance(p, r):
    base = p * 0.8
    penalty = r * 1.5
    return int(base - penalty)

# Ensure function is defined before use
Result: final_score