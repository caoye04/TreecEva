def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class SignalLogger:
    def __enter__(self):
        self.log = []
        return self.log
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def modified_fibonacci(n, log):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        a, b = modified_fibonacci(n-2, log), modified_fibonacci(n-1, log)
        adjustment = 3 if is_prime(n) else 1
        result = (a + b + adjustment) % 100
        log.append(result)
        return result

with SignalLogger() as logger:
    target_term = 12
    signal_strength = modified_fibonacci(target_term, logger)
    
print(f"Result: {signal_strength}")