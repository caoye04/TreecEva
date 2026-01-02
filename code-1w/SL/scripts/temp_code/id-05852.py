def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    for entry in logs:
        if 'status' in entry and entry['status'] == 'active':
            valid_count += 1
            temp_sum += len(entry['data'])
    average_length = temp_sum / valid_count if valid_count else 0
    return average_length

logs_data = [
    {'status': 'active', 'data': 'abcd123'},
    {'status': 'inactive', 'data': 'xyz987'},
    {'status': 'active', 'data': 'efgh456'},
    {'status': 'active', 'data': 'ijkl789'}
]

baseline = analyze_efficiency(logs_data)

productivity = 0
errors = 0
interim_results = []

for i in range(1, 6):
    slice_val = str(i**3).zfill(3)
    if int(slice_val[-1]) % 2 == 0:
        productivity += i * 2
    else:
        errors += i // 2
    
    # Distractor: irrelevant string processing
    padded = f"Item_{i}".rjust(10)
    reversed_padded = padded[::-1]
    interim_results.append(len(reversed_padded))

# More distractors
dummy_list = [x for x in range(10)]
sum_ignore = sum([x**2 for x in dummy_list if x % 3 == 0])

# Actual logic embedded among noise
threshold = baseline * 2.5
if productivity > threshold:
    adjustment = 5
else:
    adjustment = -3

# Key function with mixed operations
def evaluate_performance(p, e):
    raw = p - e * 1.5
    penalty = 0
    if p > 0:
        penalty = (e / p) * 10
    score = raw - penalty + adjustment
    return int(score)

# Critical statement
final_score = evaluate_performance(productivity, errors)

print(f"Result: {final_score}")