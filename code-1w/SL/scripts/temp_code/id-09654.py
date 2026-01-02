from itertools import groupby

def calculate_final_score(entries):
    # Filter valid entries based on length condition
    valid_entries = [e for e in entries if len(e) > 3]
    
    # Group entries by their first character
    sorted_entries = sorted(valid_entries)
    grouped = {k: list(v) for k, v in groupby(sorted_entries, key=lambda x: x[0])}
    
    # Compute score per group: sum of lengths minus number of items
    group_scores = []
    for key in grouped:
        total_length = sum(len(entry) for entry in grouped[key])
        item_count = len(grouped[key])
        group_scores.append(total_length - item_count)
    
    # Final score is the sum of all group scores
    final_score = sum(group_scores)
    return final_score

# Data setup
raw_data = ['test', 'team', 'temp', 'alpha', 'alpine', 'beta', 'beet', 'a', 'bb']
data_entries = [item.upper() for item in raw_data]  # Irrelevant transformation (minimal interference)

# Computation
final_score = calculate_final_score(data_entries)
print(f"Result: {final_score}")