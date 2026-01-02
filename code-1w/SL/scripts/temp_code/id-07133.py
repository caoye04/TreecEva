from itertools import combinations

def evaluate_stability(state):
    return sum(state) % 3 == 0

def generate_energy_pairs(elements):
    return list(combinations(elements, 2))

def calculate_equilibrium(states):
    valid_pairs = []
    for pair in generate_energy_pairs(states):
        if evaluate_stability(pair):
            valid_pairs.append(pair)
    
    total = 0
    for a, b in valid_pairs:
        total += (a * b) % 4
    
    multiplier = 2 if len(valid_pairs) > 3 else 1
    offset = 5
    return total * multiplier + offset

def main():
    # Irrelevant distraction: sensor calibration data
    calibration_data = [0.1, 0.3, 0.5]
    temperature_bias = sum(calibration_data)
    
    # Relevant input
    energy_states = [1, 2, 3, 4]
    
    # Computation of interest
    equilibrium_score = calculate_equilibrium(energy_states)
    
    # Print result as required
    print(f"Target result: {equilibrium_score}")

if __name__ == "__main__":
    main()