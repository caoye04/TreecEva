from itertools import accumulate

def calculate_phase_contributions(phases):
    # Compute weighted contributions using alternating signs for oscillation effect
    adjusted_phases = [phase * (-1)**i for i, phase in enumerate(phases)]
    return list(accumulate(adjusted_phases))

def calculate_equilibrium(phases):
    if not phases:
        return 0
    contributions = calculate_phase_contributions(phases)
    final_contribution = contributions[-1]
    normalized = final_contribution / (len(phases) or 1)
    return abs(round(normalized, 2))

# Experimental thermal phase readings from quantum lattice
thermal_phases = [17, -23, 31, -14, 9, -6]

# Irrelevant auxiliary variable (minimal distraction)
dummy_counter = 0

# Key computation: determine system equilibrium score
equilibrium_score = calculate_equilibrium(thermal_phases)

Result: equilibrium_score