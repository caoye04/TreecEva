def process_sequence(seq):
    seq = seq[1:-1]  # Remove first and last elements
    filtered = [x for x in seq if x % 2 == 0]
    transformed = [x // 2 for x in filtered]
    running_total = 0
    for val in transformed:
        running_total += val
    return running_total

# Irrelevant auxiliary data (mild distraction)
data_backup = [1, 3, 5, 7]
temp_log = {'status': 'active', 'count': 0}

# Main data input
data = [10, 14, 15, 16, 17, 18, 20]
result = process_sequence(data)
print(f"Target result: {result}")