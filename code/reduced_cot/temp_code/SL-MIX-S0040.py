names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
values = [15, 8, 22, 5, 18]
threshold = 10
filtered_count = sum(1 for _, value in zip(names, values) if value >= threshold)
print(f"Result: {filtered_count}")