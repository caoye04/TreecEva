from collections import deque

def process_game_actions():
    # Action costs: move=2, attack=5, defend=3, special=8
    action_costs = {'move': 2, 'attack': 5, 'defend': 3, 'special': 8}
    
    # State machine states: ready, processing, cooldown
    state = 'ready'
    total_energy_consumed = 0
    
    # Queue of player actions
    action_queue = deque(['move', 'attack', 'move', 'special', 'defend'])
    
    # Priority stack for special actions
    priority_stack = []
    
    while action_queue or priority_stack:
        if state == 'ready':
            if action_queue:
                action = action_queue.popleft()
                if action == 'special':
                    priority_stack.append(action)
                    state = 'processing'
                else:
                    total_energy_consumed += action_costs[action]
            else:
                state = 'cooldown'
        elif state == 'processing':
            if priority_stack:
                special_action = priority_stack.pop()
                total_energy_consumed += action_costs[special_action] * 2  # Double cost when prioritized
            state = 'ready'
        elif state == 'cooldown':
            # Process any remaining actions with reduced efficiency (1.5x cost)
            if action_queue:
                action = action_queue.popleft()
                total_energy_consumed += int(action_costs[action] * 1.5)
            else:
                break
    
    return total_energy_consumed

# Execute the game action processor
final_energy = process_game_actions()
print(f"Result: {final_energy}")