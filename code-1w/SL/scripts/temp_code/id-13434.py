def find_balance(masses, torques):
    total_mass = sum(masses)
    total_torque = sum(torques)
    
    # Compute center of mass as weighted equilibrium
    if total_mass == 0:
        return 0.0
    
    equilibrium = total_torque / total_mass
    
    # Apply safety threshold clamp using conditional expression
    clamped_equilibrium = equilibrium if abs(equilibrium) <= 100 else (100 if equilibrium > 0 else -100)
    
    # Minor irrelevant calculation (distractor at intervention level 4)
    max_moment = max(torques, default=0)
    avg_inertia = sum([m**2 for m in masses]) / len(masses) if masses else 0
    
    return clamped_equilibrium

# Physical system parameters
weights = [10, 20, 30, 40]
moments = [100, 300, 600, 1000]  # torque = force * distance

# Key assignment statement
equilibrium_point = find_balance(weights, moments)

# Print result in required format
print(f"Target result: {equilibrium_point}")