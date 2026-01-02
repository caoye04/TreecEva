def analyze_sentiment(text):
    if not text:
        return 0
    positive_words = ['good', 'excellent', 'great', 'outstanding']
    negative_words = ['poor', 'bad', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        cleaned = word.strip('.,!?")')
        if cleaned in positive_words:
            score += 1
        elif cleaned in negative_words:
            score -= 2
    return score


def normalize_value(val, min_val, max_val):
    # Irrelevant normalization function (not used in final path)
    return (val - min_val) / (max_val - min_val) if max_val != min_val else 0


def transform_data(data_list):
    # Dead code path — never called
    return [x ** 2 for x in data_list if x > 0]

# Base metrics from system logs
timestamps = [1680, 1720, 1750, 1790]
durations = [45, 52, 38, 61]
base_metrics = {
    'avg_duration': sum(durations) // len(durations),
    'total_entries': len(timestamps),
    'peak_load': max(durations) > 60
}

# Simulated user feedback string
raw_feedback = "The performance was excellent but response time was poor, overall great experience."
feedback_clean = raw_feedback.replace('response time', 'latency')
feedback_parsed = feedback_clean.split('.')
feedback_str = feedback_parsed[0].strip() + '.'  # Only use first sentence

# Auxiliary computation — misleading intermediate
sentiment_proxy = len(raw_feedback) % 7
offset_adjustment = (sentiment_proxy * 2) - 3

# Core evaluation logic
def evaluate_performance(feedback, metrics):
    sentiment = analyze_sentiment(feedback)
    
    # Bitwise fusion of control flags (real contribution)
    flag_state = 0
    if metrics['peak_load']:
        flag_state |= 4
    if metrics['avg_duration'] < 50:
        flag_state |= 2
    if sentiment > 0:
        flag_state |= 1
    
    # Secondary adjustment using string length (semi-relevant)
    length_bonus = len(feedback.split()) // 10
    
    # Dummy sort — looks important but only for distraction
    sorted_durations = sorted(durations, reverse=True)
    duration_rank = [i for i, d in enumerate(sorted_durations) if d == metrics['avg_duration']]
    rank_bonus = duration_rank[0] if duration_rank else 0
    
    # Final score calculation — only sentiment, flag_state, and length_bonus matter
    temp_score = (sentiment * 8) + (flag_state * 5) + (length_bonus * 3)
    
    # Red herring: unused rounding branch
    if temp_score > 100:
        temp_score = round(temp_score / 10) * 10
    
    return temp_score

# Key execution point
current_mode = 'diagnostic'
baseline_cycle = True
final_score = evaluate_performance(feedback_str, base_metrics)
print(f"Result: {final_score}")