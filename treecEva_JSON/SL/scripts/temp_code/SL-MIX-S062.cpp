#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdint>

struct SignalNode {
    uint32_t timestamp_hex;
    SignalNode* next;
    
    constexpr SignalNode(uint32_t ts) : timestamp_hex(ts), next(nullptr) {}
};

class SignalPeriod {
public:
    uint32_t period;
    
    constexpr SignalPeriod(uint32_t p) : period(p) {}
    
    SignalPeriod operator+(const SignalPeriod& other) const {
        return SignalPeriod(this->period + other.period);
    }
};

constexpr uint32_t gcd(uint32_t a, uint32_t b) {
    return b == 0 ? a : gcd(b, a % b);
}

constexpr uint32_t lcm(uint32_t a, uint32_t b) {
    return (a / gcd(a, b)) * b;
}

uint32_t parse_hex_to_decimal(uint32_t hex_val) {
    // Simple hexadecimal parsing simulation for timestamps
    return hex_val;  // In a real scenario, this would convert hex to decimal
}

// Variadic template to accumulate LCM
template<typename... Args>
constexpr uint32_t accumulate_lcm(Args... args);

template<>
constexpr uint32_t accumulate_lcm<>() {
    return 1;
}

template<typename T, typename... Args>
constexpr uint32_t accumulate_lcm(T first, Args... rest) {
    return lcm(first, accumulate_lcm(rest...));
}

int main() {
    // Create signal linked list with hexadecimal timestamps
    SignalNode* head = new SignalNode(0x12C);  // 300 in decimal
    head->next = new SignalNode(0x1F4);        // 500 in decimal
    head->next->next = new SignalNode(0x258);  // 600 in decimal
    head->next->next->next = new SignalNode(0x320); // 800 in decimal
    
    // Parse timestamps to get periods
    SignalPeriod p1(parse_hex_to_decimal(head->timestamp_hex));
    SignalPeriod p2(parse_hex_to_decimal(head->next->timestamp_hex));
    SignalPeriod p3(parse_hex_to_decimal(head->next->next->timestamp_hex));
    SignalPeriod p4(parse_hex_to_decimal(head->next->next->next->timestamp_hex));
    
    // Combine some periods using overloaded operator
    SignalPeriod combined_p = p1 + p2;
    
    // Calculate final synchronization point using variadic template
    uint32_t final_sync_point = accumulate_lcm(combined_p.period, p3.period, p4.period);
    
    // Clean up memory
    SignalNode* current = head;
    while (current != nullptr) {
        SignalNode* temp = current;
        current = current->next;
        delete temp;
    }
    
    std::cout << "Result: " << final_sync_point << std::endl;
    return 0;
}