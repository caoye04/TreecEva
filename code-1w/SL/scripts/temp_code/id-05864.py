from itertools import combinations
from collections import defaultdict

# Simulate a code quality assessment system with multiple metrics

def analyze_complexity(tokens):
    # Irrelevant helper function for distraction
    return sum(1 for t in tokens if len(t) > 3)

def generate_token_set(code_lines):
    # Another distracting preprocessing step
    tokens = []
    for line in code_lines:
        tokens.extend(line.split())
    return set(tokens)

def evaluate_consistency(metrics):
    # Semi-relevant: used in intermediate steps but not final
    base = sum(metrics) / len(metrics)
    deviation = sum(abs(m - base) for m in metrics)
    return base - (deviation * 0.1)

def calculate_final_score(evaluation_sets):
    # Core logic hidden among distractions
    raw_scores = []
    adjustments = []
    
    for idx, s in enumerate(evaluation_sets):
        size_metric = len(s['tokens'])
        unique_ratio = len(s['symbols']) / (len(s['tokens']) + 1)
        
        # Distracting computation - looks important but unused
        temp_weight = (size_metric * 0.7) + (unique_ratio * 1.3)
        adjustment_factor = 0.85 if idx % 2 == 0 else 1.15
        adjustments.append(adjustment_factor)
        
        # Actual contribution to result
        score_component = size_metric * unique_ratio * adjustment_factor
        raw_scores.append(score_component)
    
    # Real answer depends only on aggregated pattern across sets
    total_pairs = 0
    for i in range(len(evaluation_sets)):
        for j in range(i+1, len(evaluation_sets)):
            common_syms = evaluation_sets[i]['symbols'] & evaluation_sets[j]['symbols']
            total_pairs += len(common_syms)
    
    # Final computation chain
    base_final = sum(raw_scores)
    penalty = total_pairs * 0.5
    bonus = evaluate_consistency([len(s['tokens']) for s in evaluation_sets]) * 0.3
    
    # Dead code path - never executed, adds confusion
    if False:
        fallback = base_final - penalty + 100
        return int(fallback)
    
    # Key statement: this determines the actual answer
    final_score = int(base_final - penalty + bonus)
    return final_score

# Simulated multi-file code analysis input
code_files = [
    "def compute(x): return x ** 2 + 3*x",
    "class Processor:\n  def run(self): return True",
    "import math\nresult = math.sin(0.5)"
]

tokens_1 = generate_token_set([code_files[0]])
symbols_1 = {c for c in code_files[0] if c in '+-*/()'}

tokens_2 = generate_token_set([code_files[1]])
symbols_2 = {c for c in code_files[1] if c in '+-*/()'}

tokens_3 = generate_token_set([code_files[2]])
symbols_3 = {c for c in code_files[2] if c in '+-*/()'}

evaluation_sets = [
    {'tokens': tokens_1, 'symbols': symbols_1},
    {'tokens': tokens_2, 'symbols': symbols_2},
    {'tokens': tokens_3, 'symbols': symbols_3}
]

# Intermediate irrelevant tracking
total_chars = sum(len(f) for f in code_files)
analysis_report = defaultdict(int)
for f in code_files:
    analysis_report['lines'] += f.count('\n') + 1
    analysis_report['functions'] += f.count('def ')

# Critical execution point
final_score = calculate_final_score(evaluation_sets)
print(f"Target result: {final_score}")