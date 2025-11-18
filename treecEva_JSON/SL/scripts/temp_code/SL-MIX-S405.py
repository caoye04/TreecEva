def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

processor_load = lambda x, y: (x * 2 + y) % 7

@call_counter
def simulate_processor_signal(processor_id, load):
    delay = (processor_id * 3 + load * 2) % 5
    return delay

total_propagation_delay = 0
network_size = 6

for i in range(1, network_size):
    fib_index = fibonacci(i)
    for j in range(fib_index % 4 + 1):  # Nested loop with dynamic bound
        load = processor_load(i, j)
        delay = simulate_processor_signal(i, load)
        total_propagation_delay += delay

print(f"Result: {total_propagation_delay}")