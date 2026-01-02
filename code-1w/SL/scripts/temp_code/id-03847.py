from collections import defaultdict

# Simulate user interaction logs with various actions and outcomes
tally = [3, 5, 2, 8, 5, 3, 7]
feedback_log = ['+', '+', '-', '*', '/', '+', '-']

# Irrelevant tracking variables (distractors)
action_counter = defaultdict(int)
for action in feedback_log:
    action_counter[action] += 1

snapshot_buffer = []
for i in range(len(tally)):
    if feedback_log[i] == '*':
        snapshot_buffer.append(tally[i] ** 2)
    elif feedback_log[i] == '/':
        snapshot_buffer.append(tally[i] // 2)

# Misleading transformation using lambda (not used in final result)
compress_data = lambda x: sum([v ** (i % 3 + 1) for i, v in enumerate(x)]) // len(x)
shadow_value = compress_data(tally)

# Core processing logic with moderate nesting and conditional rules
def process_results(counts, log):
    base = 100
    penalty = 0
    bonus = 0
    
    for i in range(len(counts)):
        event = counts[i]
        action = log[i]
        
        if action == '+':
            if event > 4:
                bonus += event // 2
            else:
                base -= 1  # minor penalty for low-value positive actions
        elif action == '-':
            penalty += event // 3
        elif action == '*':
            base += event % 7
        elif action == '/' and event > 0:
            base -= (event % 4)
    
    # Final adjustment based on distribution characteristics
    unique_count = len(set(counts))
    if unique_count >= 5:
        bonus += 5
    
    intermediate = base - penalty + bonus
    
    # Dead code path (never executed under current input)
    if False:
        intermediate = compress_data([base, penalty, bonus])
    
    return intermediate

# Execute main computation
final_score = process_results(tally, feedback_log)

# Print result as required
print(f"Result: {final_score}")