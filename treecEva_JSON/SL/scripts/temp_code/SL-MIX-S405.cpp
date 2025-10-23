#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

template<int Modulus>
constexpr int mod_cycle(int value) {
    return value % Modulus;
}

int main() {
    const int EVENT_TYPES = 5;
    const int NUM_EVENTS = 7;
    
    std::priority_queue<int> event_heap;
    int event_ids[] = {12, 23, 34, 45, 56, 67, 78};
    int priorities[NUM_EVENTS];
    int event_type_counters[EVENT_TYPES] = {0};
    
    // State machine states: 0=IDLE, 1=PROCESSING, 2=COMPLETED
    int state = 0;
    int processed_events_count = 0;
    
    // Calculate priorities and populate heap
    for (int i = 0; i < NUM_EVENTS; ++i) {
        int type = mod_cycle<EVENT_TYPES>(event_ids[i]);
        event_type_counters[type]++;
        priorities[i] = static_cast<int>(std::pow(event_ids[i], 0.5)) + (type * 10);
        event_heap.push(priorities[i]);
    }
    
    // Process events using state machine
    while (!event_heap.empty()) {
        int current_priority = event_heap.top();
        event_heap.pop();
        
        switch (state) {
            case 0: // IDLE -> PROCESSING
                if (current_priority > 20) {
                    state = 1;
                }
                break;
            case 1: // PROCESSING
                if (current_priority % 3 == 0) {
                    processed_events_count += 2;
                    state = 2;
                } else {
                    processed_events_count += 1;
                    state = 0;
                }
                break;
            case 2: // COMPLETED -> IDLE
                processed_events_count += 3;
                state = 0;
                break;
        }
    }
    
    // Final state transition if needed
    if (state == 1) {
        processed_events_count += 1;
    }
    
    std::cout << "Result: " << processed_events_count << std::endl;
    return 0;
}