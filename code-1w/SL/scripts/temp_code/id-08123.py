def analyze_sentiment(texts):
    sentiment_scores = {}
    for text in texts:
        words = text.lower().split()
        positive = len([w for w in words if w in ['excellent', 'great', 'good', 'improved']])
        negative = len([w for w in words if w in ['poor', 'bad', 'worse', 'declined']])
        sentiment_scores[text[:10]] = positive - negative
    return sentiment_scores

feedback = [
    "Student performance has been excellent this term with great improvement",
    "Poor effort shown, worse than last term",
    "Good progress and improved participation",
    "No change observed, not good nor bad"
]

# Irrelevant preprocessing step (distractor)
word_count_map = {f"snippet_{i}": len(feedback[i].split()) for i in range(len(feedback))}
total_words = sum(word_count_map.values())

sentiments = analyze_sentiment(feedback)

# Simulate confidence weighting (partially relevant)
def compute_confidence(score, base=0.95):
    return round(base ** abs(score), 2)

confidence_weights = {k: compute_confidence(v) for k, v in sentiments.items()}

# Aggregation pipeline with red herring variables
temp_aggregate = 0
weight_sum = 0
for key in sentiments:
    temp_aggregate += sentiments[key] * confidence_weights[key]
    weight_sum += confidence_weights[key]

normalized_total = temp_aggregate / weight_sum if weight_sum else 0

# Dummy transformation chain (distractor)
offset_adjustment = sum([len(s) % 7 for s in feedback]) // 4
scale_factor = 1.5 + (total_words % 5) * 0.1  # Unused in final logic

# Real evaluation logic
summary_stats = {
    'positive_entries': len([v for v in sentiments.values() if v > 0]),
    'negative_entries': len([v for v in sentiments.values() if v < 0]),
    'neutral_balance': len([v for v in sentiments.values() if v == 0])
}

baseline_shift = summary_stats['positive_entries'] - summary_stats['negative_entries']

feedback_summary = {
    'net_trend': round(normalized_total, 2),
    'balance_shift': baseline_shift,
    'volume_index': total_words // 10
}

def evaluate_performance(report):
    trend = report['net_trend']
    shift = report['balance_shift']
    # Core formula: combines normalized sentiment and balance shift
    score_components = [
        trend * 20,
        shift * 15,
        report.get('volume_index', 0) * 2
    ]
    # Misleading component that looks important but isn't used
    dummy_risk_factor = max(score_components) * 0.1
    final_score = sum(score_components)  # This is the actual result
    return int(round(final_score))

final_score = evaluate_performance(feedback_summary)
print(f"Target result: {final_score}")