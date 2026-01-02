def analyze_metrics(values):
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg, variance

config = {'mode': 'strict', 'limit': 85}

# Irrelevant utility (minimal distraction)
delay_compensation = lambda offset: offset * 0.9

raw_data = [78, 82, 88, 91, 75]
processed_data = [x + 2 for x in raw_data if x >= 75]

avg_val, var_val = analyze_metrics(processed_data)

normalizer = lambda x: x * 1.05 if x < 85 else x

eval_fn = lambda a, v: a - v ** 0.5

interim_score = eval_fn(avg_val, var_val)

temp_result = normalizer(interim_score)

threshold_score = max(temp_result, config['limit'])

# Final decision logic
def determine_outcome(data):
    base = sum(data) / len(data)
    if base > threshold_score:
        return "pass"
    return "review"

final_evaluation = determine_outcome(processed_data)

print(f"Result: {threshold_score}")