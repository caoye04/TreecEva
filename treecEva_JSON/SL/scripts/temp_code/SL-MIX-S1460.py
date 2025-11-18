from itertools import combinations
from collections import namedtuple
from contextlib import contextmanager

class TaskNode:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None
    
    def append(self, task_id, priority):
        new_node = TaskNode(task_id, priority)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_priorities(self):
        priorities = []
        current = self.head
        while current:
            priorities.append(current.priority)
            current = current.next
        return priorities

@contextmanager
def priority_tracker():
    changes = []
    try:
        yield changes
    finally:
        pass

scheduler = TaskScheduler()
scheduler.append('T1', 10)
scheduler.append('T2', 20)
scheduler.append('T3', 15)
scheduler.append('T4', 25)

priorities_list = scheduler.get_priorities()

with priority_tracker() as log:
    adjusted_priorities = []
    for p in priorities_list:
        if p > 15:
            adjusted = p - 5
        else:
            adjusted = p + 3
        adjusted_priorities.append(adjusted)
        log.append(adjusted)
    
    max_combo_sum = 0
    for combo in combinations(adjusted_priorities, 3):
        combo_sum = sum(combo)
        if combo_sum > max_combo_sum:
            max_combo_sum = combo_sum
    
    # Simulate switch-case logic for final adjustment
    if max_combo_sum >= 60:
        final_priority_score = max_combo_sum * 2
    elif max_combo_sum >= 50:
        final_priority_score = max_combo_sum + 10
    else:
        final_priority_score = max_combo_sum

print(f"Result: {final_priority_score}")