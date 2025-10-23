#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <optional>

constexpr int BASE_CYCLE = 30;

// State machine states
enum class TrafficState { LOW, MODERATE, HIGH };

// Divide and conquer function to calculate load factor
int calculateLoadFactor(const std::vector<int>& densities, int start, int end) {
    if (start == end) return densities[start];
    if (start + 1 == end) return (densities[start] + densities[end]) / 2;
    
    int mid = (start + end) / 2;
    int left = calculateLoadFactor(densities, start, mid);
    int right = calculateLoadFactor(densities, mid + 1, end);
    return (left + right) / 2;
}

int main() {
    std::vector<int> sensor_readings = {25, 30, 35, 40, 45, 50};
    
    // Lambda to determine traffic state
    auto determineState = [](int load_factor) -> TrafficState {
        if (load_factor < 30) return TrafficState::LOW;
        else if (load_factor < 40) return TrafficState::MODERATE;
        else return TrafficState::HIGH;
    };
    
    int load_factor = calculateLoadFactor(sensor_readings, 0, sensor_readings.size() - 1);
    TrafficState current_state = determineState(load_factor);
    
    std::optional<int> adaptive_cycle_duration;
    
    switch (current_state) {
        case TrafficState::LOW:
            adaptive_cycle_duration = BASE_CYCLE - 5;
            break;
        case TrafficState::MODERATE: {
            // Nested lambda capture demonstration
            auto modifier = [load_factor]() { return load_factor / 10; };
            adaptive_cycle_duration = BASE_CYCLE + modifier();
            break;
        }
        case TrafficState::HIGH:
            adaptive_cycle_duration = BASE_CYCLE + 10;
            break;
    }
    
    std::cout << "Result: " << *adaptive_cycle_duration << std::endl;
    return 0;
}