#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

class SecurePacket {
private:
    int payload;
    int timestamp;

public:
    constexpr SecurePacket(int p, int t) : payload(p), timestamp(t) {}
    
    constexpr int getPayload() const { return payload; }
    constexpr int getTimestamp() const { return timestamp; }
    
    constexpr bool operator==(const SecurePacket& other) const {
        return (payload == other.payload) && (timestamp == other.timestamp);
    }
    
    constexpr bool operator!=(const SecurePacket& other) const {
        return !(*this == other);
    }
};

constexpr int mod_exp(int base, int exp, int mod) {
    int result = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % mod;
        exp = exp >> 1;
        base = (base * base) % mod;
    }
    return result;
}

int main() {
    constexpr SecurePacket test_packet(123, 456);
    constexpr int prime_modulus = 1009;
    
    int auth_checksum = 0;
    
    // Stage 1: Payload transformation
    int transformed_payload = mod_exp(test_packet.getPayload(), 3, prime_modulus);
    
    // Stage 2: Timestamp encoding
    int encoded_timestamp = (test_packet.getTimestamp() << 2) ^ 0x1F3;
    
    // Stage 3: Checksum computation
    bool valid_range = (transformed_payload > 100) && (encoded_timestamp < 2000);
    
    if (valid_range || (test_packet.getPayload() % 7 == 4)) {
        auth_checksum = (transformed_payload + encoded_timestamp) % prime_modulus;
    } else {
        auth_checksum = abs(transformed_payload - encoded_timestamp) % prime_modulus;
    }
    
    // Stage 4: Final adjustment
    if (!(auth_checksum & 1)) {  // If even
        auth_checksum = (auth_checksum * 3 + 7) % prime_modulus;
    }
    
    std::cout << "Result: " << auth_checksum << std::endl;
    return 0;
}