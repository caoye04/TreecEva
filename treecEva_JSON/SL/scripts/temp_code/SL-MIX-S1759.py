from collections import deque

def recursive_filter(input_samples, weights, delay_line):
    if not input_samples:
        return 0
    
    x = input_samples.popleft()
    y = x * weights[0]
    
    for i in range(1, len(weights)):
        if delay_line:
            y += delay_line[-i] * weights[i]
    
    delay_line.append(y)
    recursive_filter(input_samples, weights, delay_line)
    return y

def main():
    samples = deque([3, -1, 4, -2, 5])
    coefficients = [0.5, 0.3, 0.2]
    memory_taps = deque(maxlen=2)
    
    # Initialize delay line
    memory_taps.append(0)
    memory_taps.append(0)
    
    filtered_signal = recursive_filter(samples, coefficients, memory_taps)
    print(f"Result: {filtered_signal}")

if __name__ == "__main__":
    main()