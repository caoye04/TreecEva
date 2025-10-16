#define _USE_MATH_DEFINES
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <functional>

template<int N>
struct Power {
    static constexpr int value = N * Power<N-1>::value;
};

template<>
struct Power<0> {
    static constexpr int value = 1;
};

int main() {
    std::stack<int> operation_stack;
    std::queue<int> sensor_queue;
    
    // Initialize sensor readings
    for (int i = 1; i <= 5; ++i) {
        sensor_queue.push(i * 2);
    }
    
    // Push operations
    for (int i = 0; i < 3; ++i) {
        operation_stack.push(Power<3>::value - i);
    }
    
    int state = 0;
    int accumulator = 0;
    int final_adjustment = 0;
    
    // State machine with nested processing
    while (!sensor_queue.empty()) {
        int sensor_value = sensor_queue.front();
        sensor_queue.pop();
        
        // State 0: Baseline measurement
        if (state == 0) {
            accumulator += sensor_value;
            state = 1;
        }
        // State 1: Adjustment calculation
        else if (state == 1) {
            auto adjustment = [sensor_value, &accumulator](int op) {
                return (accumulator + sensor_value) % op;
            };
            
            if (!operation_stack.empty()) {
                int op = operation_stack.top();
                operation_stack.pop();
                final_adjustment += adjustment(op);
            }
            
            // Transition logic
            if (sensor_value > 5) {
                state = 2;
            } else {
                state = 0;
            }
        }
        // State 2: Finalization
        else if (state == 2) {
            final_adjustment *= 2;
            state = 0;
        }
    }
    
    std::cout << "Result: " << final_adjustment << std::endl;
    return 0;
}