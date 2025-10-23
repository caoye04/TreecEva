#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <optional>

constexpr double calculate_mean(const std::vector<double>& values) {
    double sum = 0.0;
    for (const auto& val : values) {
        sum += val;
    }
    return sum / values.size();
}

int main() {
    std::priority_queue<double> task_priorities;
    
    // Initial task priorities
    task_priorities.push(8.5);
    task_priorities.push(12.3);
    task_priorities.push(7.2);
    task_priorities.push(15.6);
    task_priorities.push(9.8);
    task_priorities.push(11.4);
    
    // Process two highest priority tasks
    task_priorities.pop();
    task_priorities.pop();
    
    // Add new tasks
    task_priorities.push(13.7);
    task_priorities.push(6.9);
    
    // Extract top 3 priorities for variance calculation
    std::vector<double> top_priorities;
    for (int i = 0; i < 3 && !task_priorities.empty(); ++i) {
        top_priorities.push_back(task_priorities.top());
        task_priorities.pop();
    }
    
    // Calculate mean of top priorities
    double mean = calculate_mean(top_priorities);
    
    // Calculate variance using lambda expression
    auto calc_variance = [mean](const std::vector<double>& values) -> double {
        double variance = 0.0;
        for (const auto& val : values) {
            variance += std::pow(val - mean, 2);
        }
        return variance / values.size();
    };
    
    double priority_variance = calc_variance(top_priorities);
    
    // Adjust variance based on priority threshold
    priority_variance = (mean > 10.0) ? priority_variance * 1.2 : priority_variance * 0.8;
    
    std::cout << "Result: " << priority_variance << std::endl;
    
    return 0;
}