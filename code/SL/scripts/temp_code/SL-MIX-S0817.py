from functools import reduce
from collections import namedtuple

def compute_exchange_path(preferences, weights):
    ExchangePath = namedtuple('ExchangePath', ['currencies', 'score'])
    paths = []
    
    for base_currency in preferences:
        path_currencies = {base_currency}
        current_score = 0.0
        
        for target_currency in preferences:
            if base_currency != target_currency:
                weight_key = f"{base_currency}-{target_currency}"
                if weight_key in weights:
                    rate = weights[weight_key]
                    # Greedy selection: only add if improves score
                    temp_score = current_score + rate * 0.75
                    if temp_score > current_score:
                        path_currencies.add(target_currency)
                        current_score = temp_score
        
        paths.append(ExchangePath(currencies=path_currencies, score=current_score))
    
    # Find path with maximum score
    return max(paths, key=lambda p: p.score).score

# Define currency preferences as frozenset for immutability
preferred_currencies = frozenset(['USD', 'EUR', 'JPY', 'GBP'])

# Transaction weights dictionary
transaction_weights = {
    'USD-EUR': 0.85,
    'USD-JPY': 110.25,
    'USD-GBP': 0.75,
    'EUR-JPY': 125.50,
    'EUR-GBP': 0.88,
    'JPY-GBP': 0.0067,
    'GBP-EUR': 1.18,
    'GBP-USD': 1.33,
    'JPY-USD': 0.0091,
    'EUR-USD': 1.18
}

# Compute optimal conversion path score
optimal_score = compute_exchange_path(preferred_currencies, transaction_weights)
print(f"Result: {optimal_score}")