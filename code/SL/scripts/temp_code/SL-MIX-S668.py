from functools import wraps

def state_machine_tracker(state_transitions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            current_state = 'START'
            for item in result:
                if isinstance(item, str) and item.isdigit():
                    current_state = state_transitions.get((current_state, 'DIGIT'), current_state)
                elif isinstance(item, str) and item.isalpha():
                    current_state = state_transitions.get((current_state, 'ALPHA'), current_state)
                else:
                    current_state = state_transitions.get((current_state, 'OTHER'), current_state)
            wrapper.final_state = current_state
            return result
        return wrapper
    return decorator

def hex_to_binary_sum(hex_char):
    return sum(int(b) for b in bin(int(hex_char, 16))[2:])

state_rules = {
    ('START', 'ALPHA'): 'ALPHA_SEEN',
    ('START', 'DIGIT'): 'DIGIT_SEEN',
    ('ALPHA_SEEN', 'DIGIT'): 'MIXED',
    ('DIGIT_SEEN', 'ALPHA'): 'MIXED',
    ('MIXED', 'ALPHA'): 'MIXED',
    ('MIXED', 'DIGIT'): 'MIXED'
}

@state_machine_tracker(state_rules)
def process_markers(markers):
    processed = []
    for m in markers:
        val = int(m, 16) if m.isdigit() else ord(m.upper()) - ord('A') + 10
        # Ternary operator to decide transformation
        transformed = val >> 1 if val % 2 == 0 else (val << 1) & 0xF
        processed.append(transformed)
    return processed

# Initial genetic markers
initial_markers = ['A', '3', 'F', '1', 'B']
transformed_values = list(process_markers(initial_markers))

# Greedy selection of values that maximize sum without exceeding 20
transformed_values.sort(reverse=True)
selected_sum = 0
for val in transformed_values:
    selected_sum = selected_sum + val if selected_sum + val <= 20 else selected_sum

# Final code calculation using state machine result
state_factor = 2 if hasattr(process_markers, 'final_state') and process_markers.final_state == 'MIXED' else 1
final_code = selected_sum * state_factor + (hex_to_binary_sum(initial_markers[0]) if initial_markers[0].isalpha() else int(initial_markers[0]))

print(f"Result: {final_code}")