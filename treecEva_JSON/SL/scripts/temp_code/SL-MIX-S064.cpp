#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <functional>

int main() {
    // Packet priorities in a min-heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> packet_queue;
    packet_queue.push(0b101010);
    packet_queue.push(0b111000);
    packet_queue.push(0b001100);
    
    // Filter rule lookup table
    std::unordered_map<int, bool> filter_rules = {{42, true}, {56, false}, {12, true}};
    
    int accumulator = 0;
    int processed_packets = 0;
    
    while (!packet_queue.empty() && processed_packets < 2) {
        int packet = packet_queue.top();
        packet_queue.pop();
        
        // Bitmask filter: check if bits 2 and 3 are set (0-indexed from right)
        bool bitmask_pass = (packet & 0b1100) == 0b1100;
        
        // Hash lookup filter
        bool hash_rule = filter_rules.count(packet) ? filter_rules[packet] : false;
        
        // Short-circuit logical evaluation: pass if bitmask passes OR (hash rule exists AND is true)
        bool packet_passes = bitmask_pass || (filter_rules.count(packet) && filter_rules[packet]);
        
        if (packet_passes) {
            // Apply bitwise transformation: XOR with 0xF and add to accumulator
            accumulator += (packet ^ 0xF);
        }
        
        processed_packets++;
    }
    
    // Final result combines accumulator with a bitwise operation
    int final_filter_result = (accumulator << 1) | 0b1;
    
    std::cout << "Result: " << final_filter_result << std::endl;
    return 0;
}