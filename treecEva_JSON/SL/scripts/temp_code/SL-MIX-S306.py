def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def switch_case(value, cases):
    return cases.get(value, 0)

@call_counter
def amplify_signal(x):
    return x * 2

@call_counter
def filter_signal(x):
    return x if x > 10 else 0

@call_counter
def normalize_signal(x):
    return x // 3

sensor_readings = [5, 12, 7, 15, 9, 20]
transformed_readings = [amplify_signal(x) for x in sensor_readings]
filtered_readings = [filter_signal(x) for x in transformed_readings]

operation_selector = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x // y if y != 0 else 0
}

combined_value = switch_case('add', operation_selector)(filtered_readings[1], filtered_readings[3])
processed_signal = normalize_signal(combined_value)

print(f"Result: {processed_signal}")