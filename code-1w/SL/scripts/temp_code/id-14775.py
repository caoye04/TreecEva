from collections import defaultdict
import math

def analyze_performance(feedback_logs, baseline):
    # Irrelevant preprocessing: case normalization (distractor)
    normalized_logs = [entry.lower() for entry in feedback_logs if len(entry) > 2]
    
    # Semi-relevant: character frequency analysis (partially misleading)
    char_freq = defaultdict(int)
    for log in normalized_logs:
        for char in log:
            if char.isalpha():
                char_freq[char] += 1
    
    # Key logic begins: count positive/negative keywords
    positive_keywords = {'good', 'great', 'excellent', 'improving', 'well'}
    negative_keywords = {'poor', 'bad', 'decline', 'worse', 'error'}
    
    pos_count = neg_count = 0
    for log in feedback_logs:
        words = log.split()
        for word in words:
            cleaned = word.strip('.,!?:;').lower()
            if cleaned in positive_keywords:
                pos_count += 1
            elif cleaned in negative_keywords:
                neg_count += 1
    
    # Distraction: unused statistical calculation
    total_chars = sum(len(log) for log in feedback_logs)
    avg_length = total_chars / len(feedback_logs) if feedback_logs else 0
    length_penalty = math.sqrt(avg_length) if avg_length > 10 else 0  # Not used
    
    # Distractor: dead code path with fake adjustment
    adjustment = 0
    if len(char_freq) > 15:  # Rarely true, not triggered here
        adjustment = -5 if 'x' in char_freq else 5
    
    # Core scoring logic
    raw_score = pos_count * 3 - neg_count * 2
    volatility_index = abs(pos_count - neg_count) / (pos_count + neg_count + 1)  # Smoothing
    stability_bonus = 10 if volatility_index < 0.3 else -5
    
    # Final computation
    final_score = int(raw_score + stability_bonus - baseline)
    
    return final_score

# Input data
feedback_entries = [
    "Good progress overall, excellent improvement",
    "Poor results in testing, worse performance",
    "Great job on the last update, very good work",
    "Error detected, bad execution flow",
    "Well handled, excellent attention to detail"
]
baseline_value = 7

# Execution point
final_score = analyze_performance(feedback_entries, baseline_value)
print(f"Result: {final_score}")