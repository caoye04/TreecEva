import collections

class TaskScheduler:
    def __init__(self):
        self.state = 'PENDING'
        self.interrupt_stack = []
        self.task_queue = collections.deque()
        self.interrupt_count = 0
    
    def digit_square_sum(self, n):
        return sum(int(digit) ** 2 for digit in str(n))
    
    def process_tasks(self, task_ids):
        # Initialize queue with task IDs
        for tid in task_ids:
            self.task_queue.append(tid)
        
        while self.task_queue:
            current_task = self.task_queue.popleft()
            priority = self.digit_square_sum(current_task)
            
            if priority > 50:
                # Interrupt all pending tasks
                self.interrupt_count += len(self.task_queue)
                # Clear queue
                self.task_queue.clear()
                # Push interrupt to stack
                self.interrupt_stack.append(current_task)
                self.state = 'RUNNING'
                break
            else:
                # Process normally
                if self.state == 'PENDING':
                    self.state = 'RUNNING'
                elif self.state == 'RUNNING':
                    self.state = 'COMPLETED'
                # Re-queue for next cycle if not completed
                if self.state != 'COMPLETED':
                    self.task_queue.append(current_task)
                else:
                    # Reset state for next task
                    self.state = 'PENDING'
        
        # Process any remaining interrupts
        while self.interrupt_stack:
            task = self.interrupt_stack.pop()
            if self.digit_square_sum(task) > 100:
                self.interrupt_count += 1
        
        return self.interrupt_count

# Initialize scheduler
scheduler = TaskScheduler()
tasks = [123, 99, 45, 88, 12, 77]

# Process tasks
interrupt_count = scheduler.process_tasks(tasks)
print(f"Result: {interrupt_count}")