#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

constexpr int compute_base_command(int sensor_val) {
    return (sensor_val > 50) ? (sensor_val / 2) : (sensor_val * 2);
}

template <typename T>
T clamp(T value, T min, T max) {
    return (value < min) ? min : ((value > max) ? max : value);
}

int main() {
    std::vector<int> sensor_readings = {40, 60, 75, 30, 85};
    std::priority_queue<int> command_heap;
    int state = 0;
    int adjustment_factor = 3;
    int final_command = 0;

    for (size_t i = 0; i < sensor_readings.size(); ++i) {
        int base_cmd = compute_base_command(sensor_readings[i]);
        
        if (state == 0 && base_cmd >= 60) {
            state = 1;
            command_heap.push(base_cmd + adjustment_factor);
            continue;
        }
        
        if (state == 1) {
            if (base_cmd < 50) {
                state = 2;
                break;
            } else {
                command_heap.push(base_cmd - adjustment_factor);
            }
        }
        
        if (state == 2) {
            command_heap.push(base_cmd * 2);
        }
    }
    
    if (!command_heap.empty()) {
        final_command = clamp(command_heap.top(), 0, 100);
    }
    
    std::cout << "Result: " << final_command << std::endl;
    return 0;
}