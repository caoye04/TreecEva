from collections import deque
import functools

call_counter = 0
def track_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global call_counter
        call_counter += 1
        return func(*args, **kwargs)
    return wrapper

@track_calls
def process_stage(value, stage_id):
    if stage_id == 1:
        return value * 2
    elif stage_id == 2:
        return value + 5
    elif stage_id == 3:
        return value ^ 3
    return value

@track_calls
def validate_output(stack):
    total = 0
    while stack:
        item = stack.pop()
        if item and (item > 10 or not stack):
            total += item
    return total

# Main processing pipeline
sensor_buffer = deque([7, 3, 9, 1, 4])
processing_stack = []

while sensor_buffer and call_counter < 10:
    data = sensor_buffer.popleft()
    if data and (data < 5 or not sensor_buffer):
        processed = process_stage(data, 1)
        if processed > 10:
            processing_stack.append(processed)
        else:
            processing_stack.append(process_stage(processed, 2))
    else:
        processing_stack.append(process_stage(data, 3))

final_output = validate_output(processing_stack) + call_counter
print(f"Result: {final_output}")