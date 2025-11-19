class EventLogger:
    def __init__(self):
        self.count = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.count += 1
        return False

def fibonacci_sequence(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

fib_nums = fibonacci_sequence(12)
window_size = 4
threshold = 15
trigger_count = 0

for i in range(len(fib_nums) - window_size + 1):
    window = fib_nums[i:i+window_size]
    weighted_sum = sum(val * (idx + 1) for idx, val in enumerate(window))
    if weighted_sum > threshold:
        with EventLogger() as logger:
            pass
        trigger_count += 1

print(f"Result: {trigger_count}")