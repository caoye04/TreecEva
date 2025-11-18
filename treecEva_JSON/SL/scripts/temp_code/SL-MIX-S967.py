from collections import deque

task_scores = [15, 3, 9, 9, 22, 7, 11, 5]
scheduler_stack = []

for idx, score in enumerate(task_scores):
    while scheduler_stack and scheduler_stack[-1] < score:
        scheduler_stack.pop()
    if not scheduler_stack or scheduler_stack[-1] >= score:
        scheduler_stack.append(score)

final_stack_depth = len(scheduler_stack)
print(f'Result: {final_stack_depth}')