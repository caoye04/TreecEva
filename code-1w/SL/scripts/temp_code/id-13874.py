from collections import Counter, defaultdict
from math import log

# Simulate student responses to a diagnostic test with multiple sections
responses = [
    ('algebra', True), ('algebra', False), ('algebra', True), ('algebra', True),
    ('geometry', True), ('geometry', False), ('geometry', True),
    ('calculus', False), ('calculus', True), ('calculus', True)
]

# Extract section-wise correctness
section_correct = defaultdict(list)
for section, correct in responses:
    section_correct[section].append(correct)

# Calculate accuracy per section
accuracy = {}
total_questions = 0
correct_answers = 0
for sec, results in section_correct.items():
    accuracy[sec] = sum(results) / len(results)
    total_questions += len(results)
    correct_answers += sum(results)

# Baseline metrics (some are distractions)
distraction_ratio = correct_answers / total_questions if total_questions else 0
baseline_avg = sum(accuracy.values()) / len(accuracy)

# Weighted score based on section difficulty (simulated)
section_weights = {'algebra': 1.0, 'geometry': 1.2, 'calculus': 1.5}
weighted_score = sum(accuracy[sec] * section_weights[sec] for sec in accuracy)

# Complexity metric: entropy of response patterns
response_bits = [int(c) for _, c in responses]
bit_counter = Counter(response_bits)
entropy = 0
for count in bit_counter.values():
    p = count / len(response_bits)
    if p > 0:
        entropy -= p * log(p, 2)

# Distraction: analyze run lengths (not used in final score)
run_length = 1
max_run = 1
for i in range(1, len(response_bits)):
    if response_bits[i] == response_bits[i-1]:
        run_length += 1
    else:
        max_run = max(max_run, run_length)
        run_length = 1
max_run = max(max_run, run_length)

# Distractor variables (unused in final logic)
flat_accuracy_trend = [accuracy['algebra'], accuracy['geometry'], accuracy['calculus']]
noise_offset = (entropy * 0.1) ** 2

# Key calculation function
def calculate_final_score(weighted, base_avg, n_sections, total_q):
    # Apply non-linear scaling based on number of sections and total questions
    adjustment_factor = (n_sections / 3) ** 0.5
    raw_score = weighted * adjustment_factor
    
    # Penalize low sample size
    if total_q < 10:
        raw_score *= 0.9
    
    # Normalize to 100-point scale
    return int(raw_score * 100 / max(weighted, 1))

# Compute final score
n_sections = len(section_correct)
final_score = calculate_final_score(weighted_score, baseline_avg, n_sections, total_questions)

# Print result as required
print(f"Result: {final_score}")