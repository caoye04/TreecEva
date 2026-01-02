from collections import Counter, defaultdict

def preprocess_text(text):
    words = text.lower().split()
    filtered = [word.strip('.,!?"') for word in words if len(word) > 2]
    return filtered

def analyze_frequency(tokens):
    freq = Counter(tokens)
    top_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return top_words[:5]

def build_context_map(tokens):
    context = defaultdict(list)
    for i, token in enumerate(tokens):
        prefix = f'ctx_{token[-2:]}'
        context[prefix].append(i)
    return context

def calculate_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 4)

def calculate_final_score(data):
    counts = [len(group) for group in data.values()]
    base_score = sum(counts)
    adjustment = len(data.keys())
    entropy_metric = calculate_entropy(counts)
    score = base_score * (1 + adjustment * 0.1) - entropy_metric * 10
    return int(score)

text_input = "The algorithm analyzes complex patterns in distributed systems and evaluates performance under variable loads and network conditions"

tokenized = preprocess_text(text_input)
frequent_terms = analyze_frequency(tokenized)
context_index = build_context_map(tokenized)

# Irrelevant computation - distractor
reversed_tokens = [t[::-1] for t in tokenized]
duplicated = reversed_tokens + reversed_tokens
sorted_dupe = sorted(duplicated, key=len, reverse=True)

# Semi-relevant grouping
grouped_by_length = defaultdict(list)
for t in tokenized:
    grouped_by_length[len(t)].append(t)

processed_data = defaultdict(list)
for k, v in grouped_by_length.items():
    if k % 2 == 1:
        processed_data[f'odd_len_{k}'].extend(v)
    else:
        processed_data[f'even_len_{k}'].extend([w.upper() for w in v])

# Key statement
final_score = calculate_final_score(processed_data)
print(f'Result: {final_score}')