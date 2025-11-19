import heapq
from collections import deque

def compute_efficiency(task_id, base_cost, adjustment_factor):
    return base_cost * (1 + adjustment_factor / 100.0)

def process_tasks():
    # Initialize task queue and energy heap
    task_queue = deque([101, 102, 103, 104])
    energy_heap = []
    
    # Lambda to update energy balance
    update_balance = lambda current, delta: current + delta
    
    initial_energy_balance = 500
    
    # Add initial tasks with efficiencies
    for i in range(4):
        task = task_queue.popleft()
        cost = 50 + i * 10
        efficiency = compute_efficiency(task, cost, i * 5)
        heapq.heappush(energy_heap, efficiency)
    
    # Process two tasks (lowest energy consumption first)
    first_task_cost = heapq.heappop(energy_heap)
    second_task_cost = heapq.heappop(energy_heap)
    
    intermediate_balance = update_balance(initial_energy_balance, -first_task_cost)
    intermediate_balance = update_balance(intermediate_balance, -second_task_cost)
    
    # Add new tasks with adjusted efficiencies
    new_tasks = [(105, 60, 3), (106, 70, 2)]
    for task_id, base_cost, adj in new_tasks:
        efficiency = compute_efficiency(task_id, base_cost, adj)
        heapq.heappush(energy_heap, efficiency)
    
    # Recalculate balance with remaining tasks
    final_energy_balance = intermediate_balance
    while energy_heap:
        cost = heapq.heappop(energy_heap)
        final_energy_balance = update_balance(final_energy_balance, -cost)
    
    return final_energy_balance

final_energy_balance = process_tasks()
print(f"Result: {final_energy_balance}")