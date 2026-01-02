from itertools import combinations

# Simulate a code analysis scoring system with multiple metrics
def analyze_code_quality(lines, complexity_weight=0.3, comment_ratio_weight=0.2):
    total_lines = len(lines)
    if total_lines == 0:
        return 0

    # Relevant metric: count actual code lines (non-empty and not just comments)
    code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    code_density = len(code_lines) / total_lines

    # Relevant metric: comment ratio
    comment_lines = [line for line in lines if line.strip().startswith('#')]
    comment_ratio = len(comment_lines) / total_lines

    # Distractor computation: counts blank lines but downweights them later
    blank_lines = [line for line in lines if not line.strip()]
    blank_line_penalty = len(blank_lines) * 0.05  # minor penalty

    # Distractor: computes average line length, but only used in debug mode
    avg_line_length = sum(len(line) for line in lines) / total_lines if total_lines > 0 else 0
    debug_info = f"Avg length: {avg_line_length:.2f}"

    # Semi-relevant: cyclomatic complexity proxy (nesting level heuristic)
    max_nesting = max((len(line) - len(line.lstrip())) // 4 for line in lines), 0)
    complexity_score = 1 / (1 + max_nesting)  # higher nesting → lower score

    # Irrelevant: finds all pairs of comment lines (not used in final score)
    comment_pairs = list(combinations(comment_lines, 2))
    pair_count = len(comment_pairs)

    # Dummy state tracking: simulates multi-phase analysis (only phase 3 matters)
    phases = ['init', 'parse', 'score']
    current_phase = None
    phase_results = {}
    for i, phase in enumerate(phases):
        current_phase = phase
        if phase == 'init':
            phase_results[phase] = total_lines * 0.1
        elif phase == 'parse':
            phase_results[phase] = code_density * 0.5
        elif phase == 'score':
            phase_results[phase] = (code_density * complexity_weight + 
                                   comment_ratio * comment_ratio_weight)

    # Core logic: final score based on weighted factors
    base_score = code_density * complexity_weight + comment_ratio * comment_ratio_weight
    time_factor = 1.0  # assumed constant for reproducibility

    # Final adjustment using conditional expression
    final_adjustment = 0.1 if comment_ratio > 0.15 else -0.05

    # Actual result computation
    final_score = (base_score + final_adjustment) * 100

    # Debug print (commented out, dead code)
    # print(f"Debug - {debug_info}, Pairs: {pair_count}")

    return final_score


def calculate_final_score(source_code_snippets):
    aggregate = 0.0
    weights = [0.5, 0.3, 0.2]  # top three snippets matter most

    scores = []
    for snippet in source_code_snippets:
        score = analyze_code_quality(snippet.split('\n'))
        scores.append(score)

    # Sort descending and take top 3 (even if fewer, padding not needed)
    sorted_scores = sorted(scores, reverse=True)[:3]

    # Weighted sum of top scores
    weighted_sum = sum(w * s for w, s in zip(weights, sorted_scores))

    # Normalize to integer scale
    final_result = int(round(weighted_sum))

    # Dead code: unused set operation (distractor)
    unique_score_set = set(scores)
    outlier_count = len(unique_score_set) - len([s for s in scores if s > 50])

    return final_result

# Input data: three code snippets with varying quality
snippet_a = [
    'def quicksort(arr):',
    '    if len(arr) <= 1:',
    '        return arr',
    '    pivot = arr[len(arr)//2]',
    '    left = [x for x in arr if x < pivot]',
    '    middle = [x for x in arr if x == pivot]',
    '    right = [x for x in arr if x > pivot]',
    '    return quicksort(left) + middle + quicksort(right)',
    ''
]

snippet_b = [
    '# Function to compute fibonacci',
    'def fib(n):',
    '    a, b = 0, 1',
    '    for _ in range(n):',
    '        a, b = b, a + b',
    '    return a',
    '',
    '# Example usage',
    '# print(fib(10))'
]

snippet_c = [
    'import os',
    '',
    'print("Hello World")',
    '',
    '# Very low code density',
    '',
    '# Another blank line',
    '',
    'x = 1'
]

source_fragments = ['\n'.join(snippet_a), '\n'.join(snippet_b), '\n'.join(snippet_c)]

# Critical execution point
final_score = calculate_final_score(source_fragments)
print(f"Result: {final_score}")