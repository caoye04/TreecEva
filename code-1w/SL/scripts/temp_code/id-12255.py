from collections import Counter

def calculate_final_score(entries):
    # Count frequency of each category
    category_count = Counter([e['category'] for e in entries])
    
    # Determine base score from entry values
    base_score = sum(e['value'] for e in entries)
    
    # Apply bonus if any category appears more than twice
    bonus = 10 if max(category_count.values()) > 2 else 0
    
    # Adjust score based on number of unique categories
    unique_categories = len(category_count)
    adjustment = -5 if unique_categories < 3 else 5
    
    # Final score calculation
    final_score = base_score + bonus + adjustment
    return final_score

# Sample data entries with mixed categories and values
data_entries = [
    {'category': 'A', 'value': 12},
    {'category': 'B', 'value': 8},
    {'category': 'A', 'value': 7},
    {'category': 'C', 'value': 5},
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 3}
]

# Compute final score
final_score = calculate_final_score(data_entries)
print(f"Result: {final_score}")