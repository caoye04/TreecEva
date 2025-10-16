
import sys
import json
import traceback

_trace_log = []
_step_counter = [0]

def _record_state(line_num, frame_locals, code_line):
    '''记录执行状态'''
    _step_counter[0] += 1
    
    # 过滤内部变量
    clean_vars = {k: repr(v)[:100] for k, v in frame_locals.items() 
                  if not k.startswith('_') and k not in ['json', 'sys', 'traceback']}
    
    snapshot = {
        'step': _step_counter[0],
        'line': line_num,
        'code': code_line.strip(),
        'vars': clean_vars
    }
    _trace_log.append(snapshot)

# 原始代码包装在函数中
def _traced_main():
        from collections import deque

    class Container:
        def __init__(self, max_capacity):
            self.max_capacity = max_capacity
            self.current_weight = 0
            self.items = []
    
        def add_item(self, item):
            item_id, weight = item
            if self.current_weight + weight <= self.max_capacity:
                self.items.append(item)
                self.current_weight += weight
                return True
            return False

    def process_shipments(incoming_queue, outgoing_queue, container_limit):
        transferred_items = 0
    
        while incoming_queue:
            shipment = incoming_queue.popleft()
            container = Container(container_limit)
        
            for item in shipment:
                if container.add_item(item):
                    outgoing_queue.append(item)
                    transferred_items += 1
    
        return transferred_items

    # Initialize queues
    incoming_shipments = deque([
        [(101, 15), (102, 25), (103, 10)],
        [(201, 30), (202, 20)],
        [(301, 40), (302, 5), (303, 15), (304, 10)]
    ])

    outgoing_deliveries = deque()
    max_container_capacity = 50

    final_transfer_count = process_shipments(incoming_shipments, outgoing_deliveries, max_container_capacity)
    print(f"Result: {final_transfer_count}")

# 执行追踪
try:
    import sys
    import linecache
    
    def trace_calls(frame, event, arg):
        if event == 'line':
            line_num = frame.f_lineno
            code_line = linecache.getline(frame.f_code.co_filename, line_num)
            _record_state(line_num, frame.f_locals, code_line)
        return trace_calls
    
    sys.settrace(trace_calls)
    _traced_main()
    sys.settrace(None)
    
except Exception as e:
    print(f"TRACE_ERROR: {str(e)}", file=sys.stderr)
    traceback.print_exc()

# 输出追踪日志
print("===TRACE_START===")
print(json.dumps(_trace_log, indent=2))
print("===TRACE_END===")
