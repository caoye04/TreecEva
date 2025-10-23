#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <optional>
#include <vector>
#include <algorithm>

int main() {
    std::string config = "1010101011110000";
    std::vector<int> tokens;
    
    // Parse binary string into integers
    for (size_t i = 0; i < config.length(); i += 4) {
        std::string chunk = config.substr(i, 4);
        int val = 0;
        for (char c : chunk) {
            val = (val << 1) | (c - '0');
        }
        tokens.push_back(val);
    }
    
    std::optional<int> signal_state;
    int xor_mask = 0b1100;
    int and_mask = 0b1010;
    
    for (int token : tokens) {
        if (!signal_state.has_value()) {
            signal_state = token;
        } else {
            // Apply XOR operation
            signal_state = signal_state.value() ^ token;
        }
        
        // Apply mask operations
        signal_state = signal_state.value() & and_mask;
        signal_state = signal_state.value() ^ xor_mask;
        
        // Right shift by 1
        signal_state = signal_state.value() >> 1;
    }
    
    int propagated_signal = signal_state.value_or(0);
    
    // Final adjustment
    if ((propagated_signal & 0b1) == 0) {
        propagated_signal = (propagated_signal << 2) | 0b11;
    } else {
        propagated_signal = propagated_signal ^ 0b1010;
    }
    
    std::cout << "Result: " << propagated_signal << std::endl;
    return 0;
}