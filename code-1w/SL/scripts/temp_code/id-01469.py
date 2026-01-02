def analyze_feedback(ratings):
    sentiment_score = 0
    for r in ratings:
        if r == 'positive':
            sentiment_score += 1
        elif r == 'negative':
            sentiment_score -= 2
    return sentiment_score

feedback = ['positive', 'neutral', 'positive', 'negative', 'positive']
score_map = {'low': 1, 'medium': 2, 'high': 3}

raw_sentiment = analyze_feedback(feedback)
adjusted_sentiment = abs(raw_sentiment) * 2 if raw_sentiment < 0 else raw_sentiment

# Simulate metric collection from multiple sources
def collect_metrics(data_type):
    if data_type == 'performance':
        return [85, 90, 78, 92]
    elif data_type == 'efficiency':
        return [0.8, 0.91, 0.76]
    return []

metrics = collect_metrics('performance')
efficiency_data = collect_metrics('efficiency')  # Unused but plausible

# Auxiliary transformation with red herring
transformed = [x * 1.1 for x in efficiency_data]
dummy_calc = sum(transformed) / len(transformed) if transformed else 0

threshold = 80
activation_flag = False
buffer_str = "processing_active"

if buffer_str.startswith("proc") and len(metrics) > 0:
    activation_flag = True

rolling_avg = 0
if len(metrics) >= 3:
    rolling_avg = sum(metrics[-3:]) / 3

# Misleading intermediate calculation
shadow_value = (rolling_avg + dummy_calc) * 0.5  # Not used later

# Core logic masked by surrounding noise
valid_count = 0
for val in metrics:
    if val >= threshold:
        valid_count += 1

bonus_awarded = False
if valid_count >= 2 and adjusted_sentiment > 3:
    bonus_awarded = True

contribution = 0
for i, m in enumerate(metrics):
    contribution += m // (i + 1) if i > 0 else m  # Avoid division by zero

penalty = 0
if 'negative' in feedback:
    penalty = 5

# Final processing with string method distraction
status_tag = "final_review_complete"
if status_tag.upper().replace("_", ",").split(",")[0] == "FINAL":
    penalty -= 1

final_score = 0
def process_performance(data, limit):
    base = sum(data) // len(data)
    above_threshold = [x for x in data if x >= limit]
    quality_bonus = len(above_threshold) * 3
    return base + quality_bonus - penalty + (10 if bonus_awarded else 0)

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")