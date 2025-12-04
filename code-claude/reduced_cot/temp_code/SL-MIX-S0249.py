import itertools

def analyze_survey_data(responses):
    # Count frequency of each response
    response_counts = {}
    for response in responses:
        if response in response_counts:
            response_counts[response] += 1
        else:
            response_counts[response] = 1
    
    # Find most common response (not used in final calculation)
    most_common = max(response_counts.items(), key=lambda x: x[1])[0]
    
    return response_counts

# Survey responses from two different groups
group_a = ['yes', 'no', 'yes', 'maybe', 'yes', 'no', 'yes']
group_b = ['no', 'yes', 'no', 'no', 'maybe', 'maybe', 'no']

# Analyze each group
result_a = analyze_survey_data(group_a)
result_b = analyze_survey_data(group_b)

# Extract unique responses from each group
set1 = set(result_a.keys())
set2 = set(result_b.keys())

# Possible combinations of responses (not used in final answer)
possible_pairs = list(itertools.product(set1, set2))
filtered_pairs = [pair for pair in possible_pairs if pair[0] != pair[1]]

# Calculate symmetric difference (elements in either set but not both)
sym_diff = set1.symmetric_difference(set2)

# Calculate intersection (elements common to both sets)
common_elements = len(set1.intersection(set2))

# Calculate union size (all unique elements)
union_size = len(set1.union(set2))

# Calculate a similarity ratio (not used in final calculation)
similarity = common_elements / union_size if union_size > 0 else 0

print(f"Result: {common_elements}")