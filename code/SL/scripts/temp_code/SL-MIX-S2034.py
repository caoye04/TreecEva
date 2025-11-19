import statistics

def find_stable_intervals(temperatures, threshold=1.5):
    n = len(temperatures)
    if n <= 1:
        return 1 if n == 1 and abs(temperatures[0]) < threshold else 0
    
    mid = n // 2
    left_count = find_stable_intervals(temperatures[:mid], threshold)
    right_count = find_stable_intervals(temperatures[mid:], threshold)
    
    cross_count = 0
    for i in range(mid):
        for j in range(mid, n):
            segment = temperatures[i:j+1]
            if len(segment) > 1 and statistics.stdev(segment) < threshold:
                cross_count += 1
    
    return left_count + right_count + cross_count

anomaly_readings = [0.8, -1.2, 0.5, 2.1, -0.9, 0.3, -0.7, 1.4]
stable_intervals = find_stable_intervals(anomaly_readings)
print(f'Result: {stable_intervals}')