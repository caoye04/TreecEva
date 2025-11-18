import heapq
from collections import defaultdict

def analyze_expression_operators(expr):
    operators = {'+', '-', '*', '/', '^', '!'}
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] in operators:
            tokens.append(expr[i])
        i += 1
    
    bigram_freq = defaultdict(int)
    for j in range(len(tokens) - 1):
        bigram = tokens[j] + tokens[j+1]
        bigram_freq[bigram] += 1
    
    # Convert to max-heap using negative values
    freq_heap = [(-freq, bigram) for bigram, freq in bigram_freq.items()]
    heapq.heapify(freq_heap)
    
    # Extract maximum frequency
    dominant_frequency = -freq_heap[0][0] if freq_heap else 0
    return dominant_frequency

expression = "a+b*c-d/e+f*g-h/i+j*k-l/m+n*o-p/q+r*s-t/u"
dominant_frequency = analyze_expression_operators(expression)
print(f"Result: {dominant_frequency}")