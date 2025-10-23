#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <stack>
#include <functional>

int main() {
    std::queue<int> process_queue;
    std::stack<int> temp_stack;
    
    // Initialize queue with process priorities
    process_queue.push(5);
    process_queue.push(3);
    process_queue.push(8);
    process_queue.push(1);
    
    int priority_modifier = 2;
    int workload_metric = 0;
    
    // Process queue with priority reevaluation
    while (!process_queue.empty()) {
        int current_priority = process_queue.front();
        process_queue.pop();
        
        // Short-circuit evaluation for priority adjustment
        if (current_priority > 4 && (current_priority += priority_modifier)) {
            temp_stack.push(current_priority);
        } else {
            temp_stack.push(current_priority - 1);
        }
    }
    
    // Reevaluate priorities using switch statement
    std::queue<int> reevaluated_queue;
    while (!temp_stack.empty()) {
        int priority = temp_stack.top();
        temp_stack.pop();
        
        switch (priority % 3) {
            case 0:
                reevaluated_queue.push(priority * 2);
                break;
            case 1:
                reevaluated_queue.push(priority + 5);
                break;
            case 2:
                reevaluated_queue.push(priority - 3);
                break;
            default:
                reevaluated_queue.push(priority);
        }
    }
    
    // Lambda to calculate final workload metric
    auto calculate_metric = [&reevaluated_queue, &workload_metric]() {
        while (!reevaluated_queue.empty()) {
            workload_metric += reevaluated_queue.front();
            reevaluated_queue.pop();
        }
    };
    
    calculate_metric();
    
    std::cout << "Result: " << workload_metric << std::endl;
    return 0;
}