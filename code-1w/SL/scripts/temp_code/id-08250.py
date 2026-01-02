from itertools import compress, count

# Simulate developer contribution analysis with noise filtering
def analyze_contributions(log_data, threshold=5):
    lines = [len(entry.split()) for entry in log_data]
    valid_entries = list(compress(log_data, (line >= threshold for line in lines)))
    
    # Irrelevant transformation
    case_transformed = [entry.upper().swapcase() for entry in valid_entries]
    token_count = sum(len(item.split()) for item in case_transformed)

    # Relevant metric: number of high-activity entries
    activity_level = len(valid_entries)
    return activity_level, token_count

# Main processing pipeline
def calculate_rating(contribs, penalty):
    base = sum(len(c) for c in contribs)
    adjustments = []
    
    for i, c in enumerate(contribs):
        if i % 2 == 0:
            adjustments.append(len(c) * 0.1)
        else:
            adjustments.append(-len(c) * 0.05)
    
    adjustment_sum = sum(adjustments)
    temp_result = base + adjustment_sum  # Intermediate state

    # Dummy filtering (no effect on result)
    filter_fn = lambda x: x.startswith('feat')
    filtered = list(filter(filter_fn, contribs))
    dummy_metric = len(filtered) * 0.3  # Unused distraction

    final_rating = temp_result - penalty * 2
    return int(final_rating)

# Input data
log_entries = [
    'fix bug in authentication module',
    'add new feature for user profile',
    'update documentation and tests',
    'refactor core utilities for performance',
    'chore: clean up deprecated code'
]

# Extract meaningful metrics
contribution_metrics, extra_info = analyze_contributions(log_entries, threshold=4)

# Generate derived inputs
contributions = [f'item_{i}' for i in range(contribution_metrics)]
penalty_factor = len([x for x in log_entries if 'chore' in x]) + 1

# Key statement
final_score = calculate_rating(contributions, penalty_factor)

print(f"Result: {final_score}")