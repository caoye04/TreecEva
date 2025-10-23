#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <memory>

template<typename T>
T gcd(T a, T b) {
    while (b != 0) {
        T temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

template<typename T>
T lcm(T a, T b) {
    return (a / gcd(a, b)) * b;
}

int main() {
    std::vector<int> signal_buffer = {12, 18, 24, 30, 36};
    std::unique_ptr<int> checksum = std::make_unique<int>(1);
    int index = 0;
    
    while (index < signal_buffer.size() - 1) {
        int current = signal_buffer[index];
        int next = signal_buffer[index + 1];
        
        bool is_lcm_operation = (index % 2 == 0) ? true : false;
        
        if (is_lcm_operation) {
            *checksum = lcm(*checksum, gcd(current, next));
        } else {
            *checksum = gcd(*checksum, lcm(current, next));
        }
        
        index = index + 1;
    }
    
    std::cout << "Result: " << *checksum << std::endl;
    return 0;
}