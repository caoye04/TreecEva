from functools import lru_cache

ingredient_prices = [2, 7, 8, 3, 1]

@lru_cache(maxsize=None)
def min_ingredient_cost(index):
    if index < 0:
        return 0
    if index == 0:
        return ingredient_prices[0]
    
    # Dynamic programming approach to find minimum cost
    option1 = min_ingredient_cost(index - 1) + ingredient_prices[index]
    option2 = min_ingredient_cost(index - 2) + ingredient_prices[index] if index >= 2 else float('inf')
    
    return min(option1, option2)

# Calculate optimal cost for all ingredients
optimal_cost = min_ingredient_cost(len(ingredient_prices) - 1)

print(f"Result: {optimal_cost}")