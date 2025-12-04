def min_max_avg_lambda(data):
    get_average = lambda x: sum(x) / len(x) if len(x) > 0 else 0
    max_val = max(data)
    min_val = min(data)
    avg_val = get_average(data)
    return (max_val - min_val) + avg_val

measurements = [45.7, 52.3, 48.9, 56.1, 43.5]
final_distance = min_max_avg_lambda(measurements)
print(f"Result: {final_distance}")