import heapq

class JobScheduler:
    def __init__(self):
        self.job_heap = []
        heapq.heapify(self.job_heap)
    
    def add_job(self, priority):
        heapq.heappush(self.job_heap, -priority)  # Negative for max-heap behavior
    
    def cancel_if_high_priority(self, threshold):
        # Short-circuit evaluation: only check heap if it's not empty
        if self.job_heap and -self.job_heap[0] > threshold:
            heapq.heappop(self.job_heap)
    
    def get_next_priority(self):
        return -self.job_heap[0] if self.job_heap else 0

# Initialize scheduler
scheduler = JobScheduler()

# Add initial jobs
scheduler.add_job(3)
scheduler.add_job(7)
scheduler.add_job(1)
scheduler.add_job(9)

# Cancel high-priority jobs (threshold 5)
scheduler.cancel_if_high_priority(5)

# Add more jobs
scheduler.add_job(4)
scheduler.add_job(6)

# Check next job priority
next_priority = scheduler.get_next_priority()
print(f'Result: {next_priority}')