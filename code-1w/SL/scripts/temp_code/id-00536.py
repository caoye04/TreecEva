def analyze_text(texts):
    char_count = lambda s: sum(1 for c in s if c.isalpha())
    weights = [0.5, 1.0, 1.5]
    scores = []
    for text in texts:
        length = len(text)
        alpha_chars = char_count(text)
        ratio = alpha_chars / length if length > 0 else 0
        score = ratio * 100 * weights[min(len(texts), 2)]
        scores.append(score)
    
    temp_debug = [x * 0.1 for x in scores]  # Irrelevant debugging trace
    return sum(scores)

extra_filter = lambda x: x > 50

data = ["Hello World!", "Python3.9", "AI@2023", ""]
offset = 7
cleanup = [s.replace(" ", "") for s in data]  # Unused preprocessing

processor = analyze_text
result = processor(data)
print(f"Result: {result}")