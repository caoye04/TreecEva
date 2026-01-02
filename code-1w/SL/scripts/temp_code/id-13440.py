from collections import defaultdict

def calculate_stability(level):
    history = defaultdict(lambda: 0)
    sequence = [1, 2, 4, 8, 16]
    
    for i in range(level + 1):
        if i < len(sequence):
            history[i] += sequence[i] - (i * 2)
    
    trend = lambda x: x > 2
    filtered = [v for v in history.values() if trend(v)]
    
    return sum(filtered) - len(filtered)

index = 4
backup_flag = True
placeholder_data = [0] * 5

# Key execution point
equilibrium = calculate_stability(index)

print(f"Result: {equilibrium}")