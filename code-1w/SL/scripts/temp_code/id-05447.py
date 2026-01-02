def calculate_final_score(results):
    total = sum(results['values'])
    count = len([x for x in results['values'] if x > 0])
    bonus = 10 if results['threshold_met'] else 0
    adjustment = -5 if count < 3 else 0
    return total + bonus + adjustment

# Data initialization
raw_data = [4, -1, 6, 0, 9]
discount_factor = 0.9

results = {
    'values': raw_data,
    'threshold_met': len(raw_data) >= 4,
    'version': '2.1'
}

# Key computation step
final_score = calculate_final_score(results)
print(f"Result: {final_score}")