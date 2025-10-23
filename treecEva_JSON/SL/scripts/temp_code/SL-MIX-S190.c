#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_FIB 20

unsigned long long fibonacci(int n) {
    if (n <= 1) return n;
    unsigned long long a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int is_prime(int num) {
    if (num <= 1) return 0;
    if (num <= 3) return 1;
    if (num % 2 == 0 || num % 3 == 0) return 0;
    for (int i = 5; i * i <= num; i += 6)
        if (num % i == 0 || num % (i + 2) == 0)
            return 0;
    return 1;
}

int main() {
    volatile int message_counter = 0;
    unsigned int auth_code = 0x12345678;
    
    // Process first set of messages
    for (int i = 3; i <= 12; i++) {
        if (is_prime(i)) {
            unsigned long long fib_val = fibonacci(i);
            unsigned int fib_mask = (unsigned int)(fib_val & 0xFFFFFFFF);
            auth_code ^= fib_mask;
            message_counter++;
        }
    }
    
    // Apply bit shifting based on counter
    if (message_counter > 5) {
        auth_code = (auth_code << 3) | (auth_code >> 29);
    } else {
        auth_code = (auth_code >> 2) | (auth_code << 30);
    }
    
    // Final transformation using floating point
    double sqrt_val = sqrt((double)auth_code);
    unsigned int truncated = (unsigned int)sqrt_val;
    auth_code = (auth_code & 0xFFFF0000) | (truncated & 0x0000FFFF);
    
    printf("Result: %u\n", auth_code);
    return 0;
}