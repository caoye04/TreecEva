from collections import deque

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

class GenomicAccumulator:
    def __init__(self):
        self.total = 0
    
    def add(self, value):
        self.total += value
        return self.total

# DNA sequence encodings
nucleotide_sequence = [9, 2, 8, 1, 7, 3, 6, 4]
window_size = 4

# Initialize sliding window and accumulator
window = deque()
accumulator = GenomicAccumulator()

# Process sliding windows
for i, nucleotide in enumerate(nucleotide_sequence):
    window.append(nucleotide)
    if len(window) > window_size:
        window.popleft()
    if len(window) == window_size:
        window_max = max(window)
        window_min = min(window)
        score = window_max * window_min
        accumulator.add(score)

# Apply transformation
dna_scores = [digital_root(accumulator.total)]
final_genomic_score = dna_scores[0]
print(f"Result: {final_genomic_score}")