#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>
#include <bitset>

template<int N>
constexpr int factorial() {
    return N <= 1 ? 1 : N * factorial<N - 1>();
}

template<int N, int K>
constexpr int combination() {
    return factorial<N>() / (factorial<K>() * factorial<N - K>());
}

constexpr int rotate_left(int value, int shift, int bits = 8) {
    return ((value << shift) | (value >> (bits - shift))) & ((1 << bits) - 1);
}

int main() {
    std::string message = "SECURE_DATA";
    int bit_mask = 0b10110101;
    int checksum = 0;
    
    for (size_t i = 0; i < message.length(); ++i) {
        int rotated_mask = rotate_left(bit_mask, i % 8);
        int xor_result = static_cast<int>(message[i]) ^ rotated_mask;
        
        if (xor_result % 2 == 0) {
            checksum += xor_result;
        } else {
            checksum -= xor_result;
        }
    }
    
    // Combinatorial adjustment
    int combinatorial_factor = combination<10, 3>();
    int final_checksum = checksum % combinatorial_factor;
    
    // Encoding step
    final_checksum = (final_checksum << 2) | (final_checksum >> 6);
    
    std::cout << "Result: " << final_checksum << std::endl;
    return 0;
}