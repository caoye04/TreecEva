from collections import deque
import re

def calculate_session_score(activities):
    activity_stack = deque()
    session_score = 0
    
    # Process activities into stack with pattern matching
    for activity in activities:
        if re.match(r'^login.*', activity):
            activity_stack.append(hash(activity) % 100)
        elif re.match(r'^view_.*', activity):
            if activity_stack:
                activity_stack[-1] += len(activity)
        elif re.match(r'^purchase_.*', activity):
            if activity_stack:
                top_val = activity_stack.pop()
                activity_stack.append(top_val * 2)
        else:
            activity_stack.append(hash(activity) % 50)
    
    # Calculate final score using conditional branching
    while activity_stack:
        val = activity_stack.popleft()
        if val > 50:
            session_score += val // 3
        elif val > 25:
            session_score += val // 2
        else:
            session_score += val
    
    return session_score

# Execution point Y
user_activities = ['login_start', 'view_product_page', 'purchase_item_123', 'logout']
session_score = calculate_session_score(user_activities)
print(f'Result: {session_score}')