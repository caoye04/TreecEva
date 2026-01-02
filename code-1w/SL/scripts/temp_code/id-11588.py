def analyze_sequence(data):
    # Irrelevant transformation: bit manipulation red herring
    magic_offset = 0
    for i in range(len(data)):
        magic_offset ^= (data[i] << 2) | (data[i] >> 1)
    
    # Distractor: unused recursive function
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    
    # Dead code path: never executed due to condition
    temp_result = 0
    if len(data) > 1000:
        for x in data:
            temp_result += x * x

    # Actual relevant logic begins here
    stats = {}
    stats['sum'] = sum(data)
    stats['count'] = len([x for x in data if x > 0])
    stats['negatives'] = len([x for x in data if x < 0])

    # Conditional branching with modular arithmetic
    adjustment = 0
    if stats['sum'] % 7 == 0:
        adjustment = 5
    elif stats['sum'] % 3 == 0:
        adjustment = -3
    else:
        adjustment = 2

    # Tuple unpacking and set operations (partially irrelevant)
    key_values = (stats['sum'], stats['count'], adjustment)
    unique_flags = set([x % 4 for x in data if x > 0])

    # Dictionary-based processing - core relevant component
    metrics_log = {
        'base': stats['sum'] // (stats['count'] + 1),
        'penalty': stats['negatives'] * 2,
        'bonus': len(unique_flags) if len(unique_flags) > 2 else 0,
        'adj': adjustment
    }

    # Unused dictionary entries - misleading complexity
    metrics_log['debug_01'] = magic_offset % 97
    metrics_log['trace'] = [fib(6)] if len(data) > 50 else []
    metrics_log['aux'] = (key_values[0] * key_values[2]) % 1000

    # Core evaluation function (simple but obscured)
    def evaluate_performance(log, threshold):
        score = log['base']
        score -= log['penalty']
        score += log['bonus']
        if log['adj'] > 0:
            score += log['adj']
        # Final conditional twist
        if score > threshold and log['bonus'] > 0:
            score *= 2
        return score

    base_threshold = 15
    
    # Key statement
    final_score = evaluate_performance(metrics_log, base_threshold)
    
    # Print result as required
    print(f"Result: {final_score}")

# Input data with deliberate properties
input_data = [4, -1, 8, 3, -2, 4, 7, 1]
analyze_sequence(input_data)