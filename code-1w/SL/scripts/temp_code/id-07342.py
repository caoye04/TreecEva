def main():
    temperature = 298
    pressure = 101.3
    volume = 22.4
    
    # Basic physical computation
    ideal_gas_constant = 8.314
    energy_level = (temperature * ideal_gas_constant) / pressure
    
    # Irrelevant atmospheric variable (minor distraction)
    humidity = 65
    
    # Conditional expression for dynamic adjustment
    adjustment_factor = 1.5 if volume > 20 else 0.8
    
    # Lambda function to apply correction based on environment
    apply_correction = lambda x: x * adjustment_factor + (volume / 100)
    
    final_adjustment = apply_correction(energy_level)
    
    # Final threshold calculation
    energy_threshold = int(final_adjustment) + 2
    
    # Output result
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()