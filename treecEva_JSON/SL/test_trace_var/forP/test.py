import heapq
from functools import reduce
from collections import namedtuple

task_tuple = namedtuple('Task', ['id', 'priority', 'dependencies', 'execution_time'])

# Task scheduler with priority queue and dependency tracking
class TaskScheduler:
    def __init__(self):
        self.task_queue = []
        self.completed = {}
        self.failure_log = set()
    
    def add_task(self, task):
        heapq.heappush(self.task_queue, (task.priority, task))
    
    def process_tasks(self):
        completed_count = 0
        while self.task_queue:
            _, task = heapq.heappop(self.task_queue)
            # Short-circuit: skip if any dependency failed
            if any(dep in self.failure_log for dep in task.dependencies):
                continue
            # Simulate task execution with potential failure
            success = task.execution_time % 3 != 0
            if success:
                self.completed[task.id] = True
                completed_count += 1
            else:
                self.failure_log.add(task.id)
        return completed_count

# Initialize scheduler with tasks
scheduler = TaskScheduler()
tasks_data = [
    task_tuple('render_engine', 2, [], 5),
    task_tuple('texture_loader', 1, ['render_engine'], 3),
    task_tuple('physics_sim', 3, ['render_engine'], 4),
    task_tuple('ai_behavior', 4, ['physics_sim'], 6),
    task_tuple('audio_mixer', 2, ['texture_loader'], 9),
    task_tuple('network_sync', 5, ['ai_behavior', 'audio_mixer'], 2)
]

# Add tasks using functional approach
list(map(scheduler.add_task, tasks_data))

# Process all tasks and count completions
completed_task_count = scheduler.process_tasks()
print(f"Result: {completed_task_count}")