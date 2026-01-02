from collections import Counter

def calculate_final_score(raw_data):
    # Count frequency of each category
    freq = Counter(raw_data)
    
    # Compute weighted score based on frequency and category priority
    weights = {'critical': 5, 'high': 3, 'medium': 2, 'low': 1}
    base_score = sum(freq.get(cat, 0) * weight for cat, weight in weights.items())
    
    # Apply bonus if critical issues exceed threshold
    bonus = 10 if freq.get('critical', 0) > 2 else 0
    
    # Deduct penalty for too many low-priority items
    penalty = -5 if freq.get('low', 0) > 6 else 0
    
    intermediate = base_score + bonus + penalty
    
    # Normalize score using conditional expression
    final_score = intermediate * 1.1 if intermediate > 0 else 0
    
    return final_score

# Simulated input data from system diagnostic
log_entries = ['high', 'medium', 'critical', 'critical', 'low', 'low', 'low', 'critical', 'medium', 'low', 'low']
data = [entry for entry in log_entries if entry in ['critical', 'high', 'medium', 'low']]

final_score = calculate_final_score(data)
print(f"Result: {final_score}")