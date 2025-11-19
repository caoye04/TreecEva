def amplification_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.5 if result > 0 else result * 0.5
    return wrapper

@amplification_decorator
def signal_transform(value, depth=3):
    if depth <= 0:
        return value
    elif value % 2 == 0:
        return signal_transform(value // 2, depth - 1)
    else:
        return signal_transform(3 * value + 1, depth - 1)

incoming_packets = [5, 12, 7]
processed_signal = sum(signal_transform(packet) for packet in incoming_packets if packet > 3)
print(f"Result: {processed_signal}")