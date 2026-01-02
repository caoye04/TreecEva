from itertools import combinations

def analyze_overlap(seg1, seg2):
    start = max(seg1[0], seg2[0])
    end = min(seg1[1], seg2[1])
    return max(0, end - start)

def process_segments(segments, limit):
    total_overlap = 0
    for pair in combinations(segments, 2):
        overlap = analyze_overlap(pair[0], pair[1])
        if overlap > 0:
            total_overlap += overlap % 7  # modular arithmetic contribution
    return total_overlap + (limit % 5)

# Input data
segments = [(2, 8), (5, 9), (6, 12), (10, 15)]
threshold = 23

result = process_segments(segments, threshold)
print(f"Target result: {result}")