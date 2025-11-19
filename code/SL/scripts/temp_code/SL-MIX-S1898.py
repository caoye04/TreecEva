from collections import deque
from contextlib import contextmanager
class TaskScheduler:
    def __init__(self):
        self.processed_count = 0
        self.state_stack = []
        self.current_priority = 0
    
    @contextmanager
    def save_state(self):
        saved_state = (self.processed_count, self.current_priority)
        self.state_stack.append(saved_state)
        try:
            yield
        finally:
            pass  # State is restored only on failure
    
    def restore_last_state(self):
        if self.state_stack:
            self.processed_count, self.current_priority = self.state_stack.pop()
    
    def process_task(self, priority, fails):
        with self.save_state():
            if priority > self.current_priority:
                self.current_priority = priority
            self.processed_count += 1
            if fails:
                self.restore_last_state()
                return False
            return True

def execute_maintenance_sequence():
    scheduler = TaskScheduler()
    task_queue = deque([
        (3, False),  # Priority 3, doesn't fail
        (5, True),   # Priority 5, fails
        (2, False),  # Priority 2, doesn't fail
        (7, False),  # Priority 7, doesn't fail
        (4, True),   # Priority 4, fails
        (6, False)   # Priority 6, doesn't fail
    ])
    
    while task_queue:
        priority, fails = task_queue.popleft()
        scheduler.process_task(priority, fails)
    
    return scheduler.processed_count

final_processed_count = execute_maintenance_sequence()
print(f"Result: {final_processed_count}")