#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

template<typename... Args>
void add_jobs(std::priority_queue<int>& job_queue, Args... priorities) {
    (job_queue.push(priorities), ...);
}

int main() {
    std::priority_queue<int> job_priorities;
    add_jobs(job_priorities, 8, 3, 12, 7, 15, 6, 9);
    
    std::vector<int> processing_times = {10, 15, 8, 20, 12, 18, 14};
    int accumulated_performance = 0;
    int current_time = 0;
    int index = 0;
    
    while (!job_priorities.empty()) {
        int priority = job_priorities.top();
        job_priorities.pop();
        
        int process_time = processing_times[index];
        
        switch (priority % 3) {
            case 0:
                if (priority % 2 == 0) {
                    process_time /= 2;
                }
                break;
            case 1:
                process_time = static_cast<int>(std::ceil(process_time * 0.75));
                break;
            case 2:
                if (priority > 10) {
                    process_time -= 3;
                } else {
                    process_time += 2;
                }
                break;
        }
        
        current_time += process_time;
        accumulated_performance += current_time;
        index++;
    }
    
    std::cout << "Result: " << accumulated_performance << std::endl;
    return 0;
}