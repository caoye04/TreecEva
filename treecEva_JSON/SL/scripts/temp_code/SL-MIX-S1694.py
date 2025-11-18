import math

def recursive_filter(packet_values):
    stack = []
    def accumulate(value):
        if not stack:
            stack.append(value)
        else:
            prev = stack.pop()
            combined = (prev + value) * 0.5
            stack.append(combined)
            stack.append(value)
    
    for val in packet_values:
        transformed = math.log(val + 1) if val > 0 else 0
        accumulate(transformed)
    
    return sum(stack)

packets = [1, 2, 3, 4]
final_output = recursive_filter(packets)
print(f'Result: {final_output}')