from collections import defaultdict

# Simulate student response frequencies in a classroom assessment
def analyze_responses(responses):
    counts = defaultdict(int)
    for response in responses:
        counts[response] += 1
    return counts

# Weighting correct reasoning patterns more heavily
def calculate_final_score(counts, weights):
    total = 0
    for key in counts:
        if key in weights:
            total += counts[key] * weights[key]
    return total

responses = ['correct', 'partial', 'correct', 'incorrect', 'partial', 'correct']
base_weights = {'correct': 3, 'partial': 1, 'incorrect': -1}

# Analyze frequency of each response type
response_counts = analyze_responses(responses)

# Apply scoring rubric based on importance of each category
temp_adjustment = sum(response_counts.values())  # auxiliary variable for normalization (not used in final score)
final_score = calculate_final_score(response_counts, base_weights)

print(f"Result: {final_score}")