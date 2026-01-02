from itertools import cycle

def analyze_workload(processes):
    scheduler = cycle([p['priority'] for p in processes])
    total_cycles = 0
    
    # Simulate fixed time-slice scheduling
    time_slice = 3
    execution_log = []
    
    for i, proc in enumerate(processes):
        priority_level = next(scheduler)
        burst_time = proc['burst']
        
        # Compute required scheduling cycles
        cycles_needed = (burst_time + time_slice - 1) // time_slice
        total_cycles += cycles_needed * priority_level
        
        execution_log.append({
            'proc_id': proc['id'],
            'cycles': cycles_needed
        })
    
    return total_cycles

# System process queue
processes = [
    {'id': 'P1', 'burst': 10, 'priority': 2},
    {'id': 'P2', 'burst': 7, 'priority': 3},
    {'id': 'P3', 'burst': 15, 'priority': 1}
]

total_cycles = analyze_workload(processes)
print(f"Result: {total_cycles}")