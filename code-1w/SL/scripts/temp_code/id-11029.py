from itertools import cycle, islice

def simulate_reaction_chain(initial_state):
    state = initial_state.copy()
    history = []
    temp_buffer = 0
    
    for step in range(3):
        shifted = [state[i] - state[(i+1)%len(state)] for i in range(len(state))]
        state = [(x + 1) * 2 for x in shifted]
        history.append(sum(state) / len(state))
        
    # Distractor: irrelevant transformation
    normalized = [round(x / max(history), 3) for x in history] if max(history) != 0 else history
    
    return history[-1]

# Irrelevant helper function (dead code path)
def estimate_pressure(altitude):
    base = 101.325
    return base * (1 - altitude / 44330) ** 5.255

# Real computation chain
def calculate_thermal_output(sequence):
    base_values = [ord(c) % 10 for c in sequence]
    expanded = []
    
    # Use itertools to create extended pattern
    cyc = cycle(base_values)
    for val in islice(cyc, len(base_values) * 2):
        expanded.append(val ** 2)
    
    # Intermediate distractor variables
    checksum = sum(expanded) % 97
    scaling_factor = len(sequence) * 0.5
    
    # Actual relevant logic
    filtered = [x for x in expanded if x > 3]
    processed = []
    for i, v in enumerate(filtered):
        if i % 2 == 0:
            processed.append(v + i)
        else:
            processed.append(v - (i % 4))
    
    # Another layer of distraction
    dummy_stats = {
        'peak': max(processed) if processed else 0,
        'variance': sum((x - sum(processed)/len(processed))**2 for x in processed)/len(processed) if processed else 0
    }
    
    final_score = sum(processed) // len(processed) if processed else 0
    return final_score

# Main execution flow
initial_conditions = [21.5, 18.3, 25.7, 19.1]
process_tag = "RXA-887"

# Simulate but don't use result (red herring)
reaction_result = simulate_reaction_chain(initial_conditions)

# Unused metadata generation
metadata_log = f"Run_{process_tag}_T{int(sum(initial_conditions))}"
status_flags = [False, True, False]

# Key data structure
process_sequence = "CH4N2O"

# Critical assignment with hidden logic
thermal_capacity = calculate_thermal_output(process_sequence)

# Final output
print(f"Result: {thermal_capacity}")