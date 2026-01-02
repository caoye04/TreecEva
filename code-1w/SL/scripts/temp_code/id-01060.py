from collections import defaultdict, Counter

# Irrelevant helper function (dead code path)
def unused_logger(x):
    return [i**2 for i in range(x) if i % 3 == 0]

# Distractor variables
temp_cache = [0] * 15
dummy_matrix = [[i*j for j in range(5)] for i in range(5)]
useless_counter = Counter('unnecessary')

# Core logic disguised among red herrings
path_traces = defaultdict(list)
traversal_flags = {i: False for i in range(20)}

# Misleading computation chain
event_log = []
for k in range(1, 6):
    if k % 2 == 0:
        event_log.append(k ** 3)
    else:
        event_log.append(-(k ** 2))

# Decoy recursive function (never called in critical path)
def bad_recursion(n):
    if n < 2:
        return n
    return bad_recursion(n-1) + bad_recursion(n-2)

# Actual root finding via digit manipulation
def find_root(n):
    digits = [int(d) for d in str(n)]
    expanded = []
    for d in digits:
        expanded.extend([d] * d)  # e.g., 3 becomes [3,3,3]
    unique_digits = list(set(expanded))
    return sum(d ** 2 for d in unique_digits)  # Sum of squares of unique repeated digits

# Secondary processing with conditional expression
status_map = {}
def process_entry(val):
    status_map[val] = 'valid' if val > 10 else 'pending'
    return val + 5 if val % 4 == 0 else val - 3

# Complex analysis with set operations and nested logic
def analyze_path(root_value):
    base_set = {i for i in range(1, root_value + 1) if root_value % i == 0}
    shifted_set = {i + 2 for i in base_set if i % 2 == 1}  # Only odd divisors get shifted
    intersection = base_set & shifted_set
    
    # Conditional expression determining next phase
    mode = 'strict' if len(intersection) > 1 else 'relaxed'
    
    accumulator = 0
    for x in sorted(base_set | shifted_set):
        if x in intersection:
            accumulator += x * 1.5
        elif x % 2 == 0:
            accumulator -= 2.1
        else:
            accumulator += 0.7
   
    # Real result buried under layers
    final_score = round(accumulator, 6)
    
    # Red herring: fake diagnostic
    fake_diagnostic = sum(shifted_set) * len(intersection)
    
    return final_score

# Dead code assignment (misleads flow interpretation)
placeholder_result = None
for _ in range(3):
    placeholder_result = [x//2 for x in temp_cache if x > 5]

# Key statement
final_diagnostic = analyze_path(find_root(8))

# Output the actual target result
print(f"Result: {final_diagnostic}")