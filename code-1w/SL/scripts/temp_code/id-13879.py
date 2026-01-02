def analyze_feedback(ratings):
    avg_rating = sum(ratings) / len(ratings)
    positive_ratio = len([r for r in ratings if r > 3]) / len(ratings)
    return avg_rating * 10 + positive_ratio * 100

feedback_scores = [4.2, 3.8, 4.5, 4.0, 3.9]
adjusted_ratings = [int(r * 2) / 2 for r in feedback_scores]
eval_metric = analyze_feedback(adjusted_ratings)

# Simulate user engagement log parsing
timestamp_log = "2023-09-10|login,2023-09-10|view,2023-09-11|click,2023-09-12|login"
log_entries = timestamp_log.split(',')
days_active = set()
for entry in log_entries:
    date = entry.split('|')[0]
    days_active.add(date)
engagement_days = len(days_active)

# Extract performance metrics from string data
raw_metrics = "errors:12|requests:150|timeout:5"
pairs = raw_metrics.split('|')
metrics_dict = {}
for pair in pairs:
    key, value = pair.split(':')
    metrics_dict[key] = int(value)

error_rate = metrics_dict['errors'] / metrics_dict['requests']
request_volume = metrics_dict['requests']

# Auxiliary calculation with distractor variables
baseline_penalty = 0
if error_rate > 0.05:
    baseline_penalty = 10
elif metrics_dict['timeout'] > 3:
    baseline_penalty = 5
else:
    temp_adjustment = 2.5  # dead code path, never used

# Core logic with meaningful computation chain
status_flags = ['high' if request_volume > 100 else 'low', 'stable' if error_rate < 0.1 else 'unstable']
performance_index = request_volume * (1 - error_rate)
scaled_index = performance_index / 10

# Secondary metric processing
threshold = 12.5
if scaled_index > threshold:
    category = 'A'
elif scaled_index > 8.0:
    category = 'B'
else:
    category = 'C'

# Distractor: irrelevant list manipulation using string methods
sample_texts = ["User report", "System log", "Error dump"]
cleaned_texts = [t.strip().lower().replace(' ', '_') for t in sample_texts]
text_lengths = [len(t) for t in cleaned_texts]
mean_length = sum(text_lengths) / len(text_lengths)

# Final processing function with nested logic and intermediate steps
def process_performance(data, limit):
    base = data.get('requests', 0) - data.get('errors', 0)
    timeout_factor = 1 - (data.get('timeout', 0) / data.get('requests', 1))
    score = base * timeout_factor
    
    if score > limit:
        bonus = 15
    else:
        bonus = 5
    
    adjustment = 0
    if 'high' in status_flags:
        adjustment += 10
    if error_rate < 0.08:
        adjustment += 7
    
    final = score + bonus + adjustment
    
    # Red herring: unused variable from string operation
    metadata_tag = f"PERF-{int(final)}".upper().replace('-', '_')
    
    return int(final)

final_score = process_performance(metrics_dict, threshold)
print(f"Target result: {final_score}")