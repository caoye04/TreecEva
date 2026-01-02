from collections import Counter
def calculate_final_score(outcomes):
    count = Counter(outcomes)
    base_score = count['pass'] * 10
    penalty = count['fail'] * 2
    bonus = 5 if count['pass'] > count['fail'] else 0
    return base_score - penalty + bonus

# Simulated test results
results = ['pass', 'pass', 'fail', 'pass', 'timeout', 'fail', 'pass']
extra_data = [x for x in results if x != 'timeout']
total_score = calculate_final_score(results)
print(f"Result: {total_score}")