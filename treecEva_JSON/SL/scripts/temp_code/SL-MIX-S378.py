from collections import Counter

def simulate_rabbit_population(months):
    if months <= 0:
        return []
    elif months == 1:
        return [1]
    elif months == 2:
        return [1, 1]
    
    population = [1, 1]
    for i in range(2, months):
        next_count = population[i-1] + population[i-2]
        population.append(next_count)
    return population

months = 8
rabbit_population = simulate_rabbit_population(months)
tagged_indices = list(range(2, len(rabbit_population), 3))
tagged_rabbit_pairs = sum(rabbit_population[i] for i in tagged_indices)

print(f"Result: {tagged_rabbit_pairs}")