from itertools import permutations

def is_valid_structure(bond_sequence):
    # State machine to validate molecular structure
    state = 'initial'
    for bond in bond_sequence:
        if state == 'initial':
            if bond in [1, 2]:
                state = 'first_bond'
            else:
                return False
        elif state == 'first_bond':
            if bond in [3, 4]:
                state = 'second_bond'
            else:
                return False
        elif state == 'second_bond':
            if bond in [5, 6]:
                state = 'terminal'
            else:
                return False
        elif state == 'terminal':
            return False
    return state == 'terminal'

# Molecular bond types represented as integers
bond_types = [1, 2, 3, 4, 5, 6]

# Generate all possible permutations of bond sequences
all_permutations = list(permutations(bond_types))

# Count valid molecular configurations
valid_configurations = sum(1 for perm in all_permutations if is_valid_structure(perm))

print(f"Result: {valid_configurations}")