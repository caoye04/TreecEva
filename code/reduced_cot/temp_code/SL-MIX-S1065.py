def calculate_butterfly_population():
    # Initialize the sequence with first two months
    population_sequence = [3, 7]
    environmental_factor = 0
    accumulated_population = population_sequence[0] + population_sequence[1]
    
    # Calculate populations for months 3 through 8
    for month in range(2, 8):
        current_population = population_sequence[month-1] + population_sequence[month-2] + environmental_factor
        population_sequence.append(current_population)
        accumulated_population += current_population
        environmental_factor += 2
    
    return accumulated_population

accumulated_population = calculate_butterfly_population()
print(f"Result: {accumulated_population}")