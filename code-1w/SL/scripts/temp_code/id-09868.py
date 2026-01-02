def analyze_efficiency(metrics):
    adjusted = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)
    return [round(x, 2) for x in adjusted]


def calculate_baseline(data):
    total = sum(data)
    average = total / len(data)
    offset = (data[0] - data[-1]) * 0.3
    baseline = average + offset
    return baseline

# Simulate sensor readings from production line
raw_readings = [88, 92, 76, 81, 94, 85]

# Irrelevant transformation - string simulation for distraction
status_codes = ['OK', 'PASS', 'ACTIVE', 'RUNNING']
status_flag = ''.join([s[0] for s in status_codes]).lower()

# Analyze efficiency with enumeration
processed_metrics = analyze_efficiency(raw_readings)

# Calculate baseline performance
base_perf = calculate_baseline(raw_readings)

# Extract even-indexed values using zip and list comprehension
indices = list(range(len(processed_metrics)))
even_data = [val for idx, val in zip(indices, processed_metrics) if idx % 2 == 0]

# Dummy set operations for interference
unique_values = set(processed_metrics)
expected_range = set(range(70, 100))
deviations = unique_values - expected_range  # Not used later

# Core logic variables
productivity = sum(even_data) / base_perf
risk_factor = len(deviations) * 0.5

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Helper function defined after use (distraction via ordering)
def evaluate_performance(eff, risk):
    if eff < 80:
        penalty = 10
    else:
        penalty = 5
    
    score = (eff - risk * 2) - penalty
    
    # Extra computations that don't affect final result
    normalized = (score + 100) / 2
    confidence = 0.9 if score > 60 else 0.6
    
    return int(round(score))

print(f"Result: {final_score}")