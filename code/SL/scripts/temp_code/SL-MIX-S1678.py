from collections import deque

# Pie contribution values
pie_weights = {'apple': 2.5, 'blueberry': 3.0, 'cherry': 1.75}

# Stack of pies sold today (top of stack is most recent)
pie_stack = deque(['apple', 'cherry', 'blueberry', 'apple', 'cherry'])

# Initialize score
final_score = 0.0

# Process stack from top to bottom
while pie_stack:
    pie_type = pie_stack.pop()
    final_score += pie_weights[pie_type]

print(f"Result: {final_score}")