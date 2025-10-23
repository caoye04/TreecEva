#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>

int main() {
    std::unordered_map<char, int> hexMap = {
        {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
        {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7},
        {'8', 8}, {'9', 9}, {'A', 10}, {'B', 11},
        {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15}
    };
    
    std::queue<std::string> packetQueue;
    packetQueue.push("A5");
    packetQueue.push("3C");
    packetQueue.push("F1");
    packetQueue.push("B2");
    
    std::stack<int> valueStack;
    int threatScore = 0;
    
    while (!packetQueue.empty()) {
        std::string packet = packetQueue.front();
        packetQueue.pop();
        
        int highNibble = hexMap[packet[0]];
        int lowNibble = hexMap[packet[1]];
        
        // Bitwise operations with short-circuit evaluation
        if ((highNibble & 0x8) && (lowNibble | 0x2)) {
            int combined = (highNibble << 4) | lowNibble;
            valueStack.push(combined);
        } else if ((highNibble ^ lowNibble) > 0x5) {
            valueStack.push(highNibble * lowNibble);
        }
    }
    
    // Process the stack with lambda and arithmetic
    auto transform = [](int x) -> int {
        return (x % 7 == 0) ? (x >> 1) : (x * 3 + 1);
    };
    
    while (!valueStack.empty()) {
        int val = valueStack.top();
        valueStack.pop();
        
        int transformed = transform(val);
        threatScore += (transformed & 0xF) ? (transformed ^ 0xFF) : (transformed | 0x10);
    }
    
    // Final adjustment
    threatScore = (threatScore > 100) ? (threatScore / 2) : (threatScore * 2);
    
    std::cout << "Result: " << threatScore << std::endl;
    return 0;
}