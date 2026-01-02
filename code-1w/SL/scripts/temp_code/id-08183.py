from itertools import cycle

# Simulate a game round with player actions and dynamic scoring
base_points = [3, 7, 2, 8, 5]
modifiers = [1, -1, 2]
action_names = ['jump', 'dash', 'block', 'attack', 'defend']

# Use enumerate and zip to align actions with base points
action_point_map = {name: base for idx, (name, base) in enumerate(zip(action_names, base_points))}

total_score = 0
modifier_cycle = cycle(modifiers)
penalty_counter = 0  # Irrelevant distractor variable

for i, (action, point) in enumerate(zip(action_names, base_points)):
    modifier = next(modifier_cycle)
    adjusted = point * modifier
    
    # Apply conditional logic based on action type
    if 'attack' in action or 'dash' in action:
        lambda_bonus = (lambda x: x + 2 if x < 5 else x)(adjusted)
        total_score += lambda_bonus
    elif 'defend' in action:
        total_score += max(adjusted, 0)
        break  # Key execution point — what is total_score here?
    else:
        total_score += adjusted

print(f"Result: {total_score}")