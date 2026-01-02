def analyze_sentiment(log):
    normalized = log.lower().replace('.', '').strip()
    words = normalized.split()
    positive = ['gain', 'up', 'rise', 'strong']
    negative = ['loss', 'down', 'fall', 'weak']
    score = 0
    for word in words:
        if word in positive:
            score += 2
        elif word in negative:
            score -= 3
    return score

raw_input = "Market showed a slight gain today. No major loss reported."
trend_log = raw_input.capitalize()
balance_score = analyze_sentiment(trend_log)
print(f"Result: {balance_score}")