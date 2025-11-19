from collections import deque

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def calculate_harmonic_score(note_durations, interval_sequence):
    duration_queue = deque(note_durations)
    interval_stack = []
    harmonic_complexity_score = 0
    
    # Process note durations and build interval stack
    while duration_queue:
        duration = duration_queue.popleft()
        if duration > 0:
            # Calculate interval based on duration
            interval = (duration * 3) % 7 + 1
            interval_stack.append(interval)
    
    # Calculate harmonic complexity using Fibonacci weights
    position = 1
    while interval_stack:
        interval = interval_stack.pop()
        fib_weight = fibonacci(position)
        harmonic_complexity_score += interval * fib_weight
        position += 1
    
    return harmonic_complexity_score

# Musical composition data
note_durations = [4, 2, 8, 1, 6, 3]
interval_sequence = [2, 5, 1, 4, 3]

# Calculate the harmonic complexity score
harmonic_complexity_score = calculate_harmonic_score(note_durations, interval_sequence)
print(f"Result: {harmonic_complexity_score}")