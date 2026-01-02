from collections import defaultdict
import math

def analyze_sentiment(texts):
    # Irrelevant helper function (dead code path)
    sentiment_score = 0
    for t in texts:
        if 'good' in t:
            sentiment_score += 1
        elif 'bad' in t:
            sentiment_score -= 1
    return sentiment_score

def preprocess_ratings(raw_ratings):
    # Distractor computation: normalizes ratings but result not fully used
    normalized = []
    max_rating = max(raw_ratings)
    min_rating = min(raw_ratings)
    for r in raw_ratings:
        normalized.append((r - min_rating) / (max_rating - min_rating + 1e-8))
    return [round(n * 10) for n in normalized]

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    # Only some values are actually filtered; this is slightly misleading
    return [x for x in data if abs(x - mean_val) / std_dev <= threshold]

def aggregate_performance(feedback, base):
    # Core logic begins
    stats = defaultdict(int)
    total_entries = 0
    
    for category, records in feedback.items():
        stats['categories_seen'] += 1
        for val in records:
            stats['total_feedback'] += 1
            if val > 7:
                stats['high'] += 1
            elif val < 4:
                stats['low'] += 1
            else:
                stats['medium'] += 1
            total_entries += 1
    
    # Semi-relevant transformation
    ratio_high = stats['high'] / (total_entries + 1e-8)
    ratio_low = stats['low'] / (total_entries + 1e-8)
    
    adjustment_factor = (ratio_high * 1.5) - (ratio_low * 0.8)
    
    # Multiple assignment that looks important but only one is used
    final_score, temp_cap, floor_limit = int(base + adjustment_factor * 10), 100, 10
    
    # Red herring: complex calculation that doesn't affect output
    decayed_score = 0
    for i in range(len(feedback)):
        decayed_score += final_score / (i + 1)
    decayed_score = int(decayed_score % 100)
    
    # Additional distraction: unused min/max tracking
    debug_min, debug_max = float('inf'), float('-inf')
    for vals in feedback.values():
        debug_min = min(debug_min, min(vals))
        debug_max = max(debug_max, max(vals))
    
    return final_score

# Main execution
base_rating = 50
raw_feedback = [7, 3, 9, 2, 8, 1, 7, 6]
feedback_data = {
    'usability': [7, 8, 6, 9],
    'performance': [5, 3, 2, 4, 7],
    'design': [8, 8, 6, 7, 9],
    'reliability': [6, 4, 7, 3, 2]
}

# Preprocessing that seems important but only affects flow
processed_raw = preprocess_ratings(raw_feedback)
denoised_data = {}
for k, v in feedback_data.items():
    denoised_data[k] = filter_outliers(v)

# Key statement
final_score = aggregate_performance(feedback_data, base_rating)

# Print result
print(f"Result: {final_score}")