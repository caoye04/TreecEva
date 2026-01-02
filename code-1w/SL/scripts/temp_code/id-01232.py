def main():
    # Simulating force vectors in a mechanical system
    axial_forces = [12, -8, 6, -15]
    radial_forces = [7, 3, -4, 2]
    
    # Combine forces into tuples of (axial, radial)
    forces = list(zip(axial_forces, radial_forces))
    
    # Irrelevant auxiliary variable (minor distraction, intervention level 4)
    peak_load = max([abs(f[0]) + abs(f[1]) for f in forces])
    
    # Dampening factor based on conditional expression
    dampen = lambda x: 0.9 if sum(x[0] for x in forces) > 0 else 0.95
    
    # Calculation using lambda and tuple unpacking
    def calculate_balance(components, factor):
        total = 0
        for ax, rd in components:
            if ax * rd < 0:
                total += (ax - rd) * 1.1
            else:
                total += (ax + rd)
        return round(total * factor(), 3)
    
    equilibrium = calculate_balance(forces, dampen)
    
    # Print result in required format
    print(f"Result: {equilibrium}")

if __name__ == "__main__":
    main()