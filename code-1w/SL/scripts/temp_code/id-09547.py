def analyze_sentiment(text):
    positive_words = ['great', 'excellent', 'good', 'outstanding', 'remarkable']
    negative_words = ['poor', 'bad', 'terrible', 'awful', 'disappointing']
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    return pos_count - neg_count

# Irrelevant helper function (distractor)
def compute_entropy(s):
    from math import log
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    total = len(s)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Another misleading calculation
token_stats = {}
raw_input = "Excellent service and great staff but poor wait times"
processed_tokens = raw_input.strip().lower().replace('!', '').replace('.', '').split()
for token in processed_tokens:
    clean_token = token.strip('.,!?"')
    if clean_token not in token_stats:
        token_stats[clean_token] = 0
    token_stats[clean_token] += 1

# Simulate historical data (dead code path)
historical_scores = []
for year in range(2018, 2023):
    trend_offset = (year - 2020) ** 2
    historical_scores.append(75 - trend_offset)

# Base metric with red herring variables
base_rating = 68
adjustment_factor = 1.0
noise_level = 0.05
sample_size = 42
confidence = 95  # unused

feedback_str = "Outstanding quality excellent work good job great effort"
decay_rate = 0.1  # unused parameter
sentiment_shift = analyze_sentiment(feedback_str)

# Complex conditional adjustment (some branches never taken)
effective_adjustment = 0
if sentiment_shift > 0:
    if sentiment_shift % 2 == 0:
        effective_adjustment = sentiment_shift * 2
    else:
        effective_adjustment = sentiment_shift * 1.8
elif sentiment_shift < 0:
    effective_adjustment = abs(sentiment_shift) * -1.5
else:
    effective_adjustment = 0

# Secondary influence from string characteristics
length_bonus = len(feedback_str.split()) // 4
format_score = feedback_str.count(' ') - feedback_str.count('  ')  # single vs double space

# Dummy list processing (irrelevant)
dummy_data = [f"item_{i}" for i in range(10)]
processed_items = []
for item in dummy_data:
    if 'odd' in item:
        continue
    processed_items.append(item.upper())

# Final scoring logic
baseline = base_rating
boost = effective_adjustment + length_bonus
final_score = baseline + boost

# Extra unrelated computation
total_chars = sum(len(word) for word in feedback_str.split())
avg_word_length = round(total_chars / len(feedback_str.split()), 2)

Result: final_score