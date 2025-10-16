#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <memory>

class SecureHasher {
private:
    static constexpr int MODULUS = 251;  // Prime number for modular arithmetic
    
    static constexpr int mod_pow(int base, int exp, int mod) {
        int result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
    
public:
    static int compute_authenticator(const int* data, size_t length) {
        int authenticator = 42;  // Initial seed value
        
        for (size_t i = 0; i < length; ++i) {
            int byte_val = data[i] & 0xFF;  // Ensure 8-bit value
            
            // Apply modular exponentiation
            int exp_result = mod_pow(byte_val + 1, 3, MODULUS);
            
            // Combine with current authenticator using XOR
            authenticator ^= exp_result;
            
            // Apply another modular transformation
            authenticator = (authenticator * 17 + 89) % MODULUS;
            
            // Bitwise rotation
            authenticator = ((authenticator << 3) | (authenticator >> 5)) & 0xFF;
        }
        
        return authenticator;
    }
};

int main() {
    // Simulated encrypted message bytes
    const int message_bytes[] = {0xA5, 0x3C, 0xF1, 0x7B, 0x2E, 0x9D, 0x48, 0xC6};
    const size_t msg_length = sizeof(message_bytes) / sizeof(message_bytes[0]);
    
    // Process the message through our secure hasher
    int authenticator = SecureHasher::compute_authenticator(message_bytes, msg_length);
    
    // Final adjustment based on message parity
    int parity_check = 0;
    for (size_t i = 0; i < msg_length; ++i) {
        parity_check ^= message_bytes[i];
    }
    
    // If parity is odd, apply additional transformation
    if (parity_check & 1) {
        authenticator = (authenticator * 73 + 15) % 251;
    }
    
    std::cout << "Result: " << authenticator << std::endl;
    return 0;
}