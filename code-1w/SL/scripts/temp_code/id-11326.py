def process_efficiency(data_set, filter_func):
    filtered = {x for x in data_set if filter_func(x)}
    anomalies = set()
    baseline = sum(filtered) // len(filtered) if filtered else 0
    for x in data_set:
        if abs(x - baseline) > 15:
            anomalies.add(x)
    clean_data = data_set - anomalies
    return sum(clean_data) - len(anomalies)

set_data = {12, 15, 18, 22, 47, 8, 10, 14, 20}

threshold_func = lambda x: x > 9

# Irrelevant auxiliary variable (minimal distraction)
baseline_diagnostic = [x for x in set_data if x % 3 == 0]

filtration_score = process_efficiency(set_data, threshold_func)
print(f"Result: {filtration_score}")