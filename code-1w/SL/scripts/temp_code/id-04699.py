def analyze_efficiency(metrics):
    adjusted = []
    for val in metrics:
        if val > 50:
            adjusted.append(val * 0.9)
        else:
            adjusted.append(val * 1.1)
    return sum(adjusted) / len(adjusted)

productivity = [85, 90, 78, 65, 92]
baseline = [70, 75, 80, 68, 85]

# Irrelevant transformation chain (distractor)
temp_data = ''.join([chr(65 + (x % 26)) for x in baseline])
encoded = temp_data.lower().replace('a', 'z').upper()
checksum = sum(ord(c) for c in encoded) // len(encoded)

# Semi-relevant preprocessing
normalized = [round((x - min(productivity)) / (max(productivity) - min(productivity)) * 100) for x in productivity]
scaled_metrics = [x + 10 for x in normalized if x > 30]  # Some filtering

# Dummy risk calculation with red herring variables
volatility = sum((a - b) ** 2 for a, b in zip(productivity, baseline)) ** 0.5
inflation_adjustment = 1.02  # Unused but plausible
risk_factor = volatility * 0.3 if volatility > 20 else volatility * 0.1

# Core logic obscured by multiple layers
aggregate = analyze_efficiency(scaled_metrics)
penalty_rate = 0.05 if len(scaled_metrics) > 4 else 0.1
raw_score = aggregate * (1 - penalty_rate)

# Final evaluation with string-based switch (using string method)
def evaluate_performance(efficiency_list, risk):
    category = "high" if sum(efficiency_list) > 300 else "low"
    modifier = 1.2 if "high" in category.upper() else 0.8  # Use of string method
    base = sum(efficiency_list) / len(efficiency_list)
    return int(base * modifier - risk)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")