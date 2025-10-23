#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <stack>
#include <vector>

constexpr double calculate_mean(const std::vector<int>& values) {
    int sum = 0;
    for (const auto& v : values) sum += v;
    return static_cast<double>(sum) / values.size();
}

int main() {
    std::queue<int> inspection_queue;
    std::stack<int> validation_stack;
    
    // Load initial batch
    for (int i = 1; i <= 10; ++i) {
        inspection_queue.push(i * 5);
    }
    
    // Process first stage (75% pass rate)
    int queue_count = 0;
    while (!inspection_queue.empty()) {
        if (inspection_queue.front() % 3 == 0) {
            validation_stack.push(inspection_queue.front());
        }
        inspection_queue.pop();
        queue_count++;
    }
    
    // Count second stage items
    const int stack_count = validation_stack.size();
    
    // Calculate mean items per stage
    const std::vector<int> stage_counts = {queue_count, stack_count};
    const double mean_items_per_stage = calculate_mean(stage_counts);
    
    std::cout << "Result: " << mean_items_per_stage << std::endl;
    return 0;
}