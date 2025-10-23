#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

#define NUM_CHUNKS 32

unsigned int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int is_prime(int num) {
    if (num < 2) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

unsigned int hash_string(const char* str) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash;
}

int main() {
    unsigned int allocation_mask = 0x00000000;
    
    // Allocate chunks for Fibonacci-sized requests (indices 1 to 10)
    for (int i = 1; i <= 10; i++) {
        int fib_size = fibonacci(i);
        int chunk_index = fib_size % NUM_CHUNKS;
        allocation_mask |= (1U << chunk_index);
    }
    
    // Deallocate prime-numbered chunks (0 to 31)
    for (int i = 0; i < NUM_CHUNKS; i++) {
        if (is_prime(i)) {
            allocation_mask &= ~(1U << i);
        }
    }
    
    // XOR with hash of a specific string
    const char* secret_key = "dealloc_complete";
    unsigned int hash_mask = hash_string(secret_key) & 0xFFFFFFFF;
    allocation_mask ^= hash_mask;
    
    printf("Result: %u\n", allocation_mask);
    return 0;
}