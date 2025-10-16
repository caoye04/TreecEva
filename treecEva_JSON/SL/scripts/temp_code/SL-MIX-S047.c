#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define PACKET_COUNT 5
#define EXPONENT_BASE 2.5
#define ROTATION_MASK 0xF0F0F0F0

volatile int packet_headers[PACKET_COUNT] = {0x12345678, 0x9ABCDEF0, 0x11111111, 0x22222222, 0x33333333};

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int compute_combinatorial_coefficient(int n, int k) {
    if (k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (k > n - k) k = n - k;
    int result = 1;
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }
    return result;
}

int main() {
    int validation_signatures[PACKET_COUNT];
    int previous_signature = 0xABCDEF00;
    
    for (int i = 0; i < PACKET_COUNT; i++) {
        // Apply rotating mask with XOR
        int masked_packet = packet_headers[i] ^ (ROTATION_MASK >> (i*4));
        
        // Apply exponential decay to previous signature
        int decayed_signature = (int)(previous_signature / pow(EXPONENT_BASE, i));
        
        // Combine with XOR
        int combined = masked_packet ^ decayed_signature;
        
        // Apply combinatorial coefficient
        int coefficient = compute_combinatorial_coefficient(PACKET_COUNT, i);
        validation_signatures[i] = combined & coefficient;
        
        previous_signature = validation_signatures[i];
    }
    
    // Final verification: compute GCD of all signatures
    int network_integrity_checksum = validation_signatures[0];
    for (int i = 1; i < PACKET_COUNT; i++) {
        network_integrity_checksum = gcd(network_integrity_checksum, validation_signatures[i]);
    }
    
    // Apply final bit manipulation
    network_integrity_checksum = (network_integrity_checksum << 2) | (network_integrity_checksum >> 30);
    
    printf("Result: %d\n", network_integrity_checksum);
    return 0;
}