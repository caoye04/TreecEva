from collections import deque

def process_scheduling_cycle(tasks, quantum):
    ready_queue = deque(tasks)
    elapsed_time = 0
    total_cycles = 0
    
    while ready_queue:
        current_task = ready_queue.popleft()
        if current_task > quantum:
            # Task requires more time, re-enqueue remaining work
            ready_queue.append(current_task - quantum)
            elapsed_time += quantum
        else:
            # Task completes in this cycle
            elapsed_time += current_task
        
        # Count full cycles (each iteration counts as one scheduling cycle)
        total_cycles += 1
        
        # Irrelevant counter for context (minimal interference)
        dummy_counter = elapsed_time % 7
    
    return total_cycles

# Simulate round-robin scheduling with time slice 3
task_load = [5, 3, 8, 2]
quantum_setting = 3
queue = task_load.copy()

total_cycles = process_scheduling_cycle(queue, quantum_setting)
print(f"Result: {total_cycles}")