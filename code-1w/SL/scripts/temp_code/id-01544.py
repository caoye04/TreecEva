def analyze_text(text_data):
    if not text_data.strip():
        return 0
    words = text_data.split()
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    avg_length = char_count / word_count if word_count else 0
    uppercase_ratio = sum(1 for c in text_data if c.isupper()) / len(text_data)
    return avg_length * (1 + uppercase_ratio)


def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True

# Irrelevant helper function (decoy)
def calculate_entropy(data_list):
    from math import log
    freq = {}
    total = len(data_list)
    for item in data_list:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Another decoy: unused complex transformation
def transform_grid(grid):
    n = len(grid)
    rotated = [[grid[n-j-1][i] for j in range(n)] for i in range(n)]
    flipped = [row[::-1] for row in rotated]
    return flipped

# Misleading intermediate computation
def get_decoy_value(x):
    result = 0
    for i in range(1, x + 1):
        if i % 2 == 0:
            result += i ** 2
        else:
            result -= i ** 3
    return result  # Never used

# Core logic disguised among distractors
def compute_baseline(vals):
    base = 0
    for v in vals:
        if v > 0 and v % 2 == 0:
            base += v ** 0.5
    return int(base)

# Key function with embedded logic and distractions
def evaluate_performance(metrics, weights):
    temp_result = 0
    final_score = 0
    adjustment_factor = 1.0
    
    # Distractor: irrelevant conditional block
    if len(metrics) > 5:
        adjustment_factor *= 0.9
    elif len(metrics) == 0:
        return -1
    
    # Real logic begins
    weighted_sum = 0
    weight_total = 0
    
    for i, (m, w) in enumerate(zip(metrics, weights)):
        # Simulate performance decay over time (index)
        decay = 1 / (1 + i * 0.1)
        contribution = m * w * decay
        weighted_sum += contribution
        weight_total += w * decay
    
    if weight_total > 0:
        temp_result = weighted_sum / weight_total
    
    # Additional processing with string-based logic (required feature)
    status_str = "optimal" if temp_result > 75 else "suboptimal"
    bonus_multiplier = 1.2 if 'opt' in status_str else 0.8
    
    # Apply bonus only if certain conditions met (conditional expression)
    final_score = int(temp_result * bonus_multiplier) if temp_result > 50 else int(temp_result)
    
    # Red herring: modify final_score but condition never triggers
    debug_flag = False
    if debug_flag and isinstance(final_score, int):
        final_score -= get_decoy_value(final_score % 10)
    
    return final_score

# Irrelevant data structure
fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34]
valid_fib = validate_sequence(fib_sequence)

# Unused entropy calculation (distractor)
data_sample = [1, 1, 2, 3, 2, 1, 4]
entropy_val = calculate_entropy(data_sample)

# String manipulation decoy
document = "LLM evaluation requires careful design of reasoning tasks."
readability_score = analyze_text(document)

# Grid transformation not used (dead path)
puzzle_grid = [[1,2],[3,4]]
transformed = transform_grid(puzzle_grid)

# Actual input data for core logic
raw_metrics = [88, 92, 76, 81, 95]
importance_weights = [10, 15, 5, 8, 12]

# Critical execution point
final_score = evaluate_performance(raw_metrics, importance_weights)
print(f"Result: {final_score}")