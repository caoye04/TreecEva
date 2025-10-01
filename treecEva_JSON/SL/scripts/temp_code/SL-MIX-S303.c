#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Nested structure definition
    struct Inner {
        int vals[3];
        double factor;
    };
    
    struct Outer {
        struct Inner inner;
        char tag[10];
        int flags;
    } data[2];
    
    // Initialize first structure
    data[0].inner.vals[0] = 5;
    data[0].inner.vals[1] = 12;
    data[0].inner.vals[2] = 8;
    data[0].inner.factor = 1.5;
    strcpy(data[0].tag, "alpha");
    data[0].flags = 0b11001010;  // 202 in decimal
    
    // Initialize second structure
    data[1].inner.vals[0] = 3;
    data[1].inner.vals[1] = 7;
    data[1].inner.vals[2] = 11;
    data[1].inner.factor = 2.0;
    strcpy(data[1].tag, "beta");
    data[1].flags = 0b10110101;  // 181 in decimal
    
    // Complex calculation chain
    int sum1 = data[0].inner.vals[0] + data[0].inner.vals[1] * data[0].inner.vals[2];
    int sum2 = data[1].inner.vals[0] * data[1].inner.vals[1] + data[1].inner.vals[2];
    
    // Bitwise operations
    int bitwise_and = data[0].flags & data[1].flags;
    int bitwise_or = data[0].flags | data[1].flags;
    int bitwise_xor = data[0].flags ^ data[1].flags;
    
    // Mathematical operations
    double power_result = pow((double)sum1, 0.5);
    double log_result = log(sum2);
    
    // String length calculation
    int len_alpha = strlen(data[0].tag);
    int len_beta = strlen(data[1].tag);
    
    // Final complex expression combining all previous calculations
    int intermediate = (int)(power_result * data[0].inner.factor) + (int)(log_result * data[1].inner.factor);
    int combined_flags = (bitwise_and << 2) ^ (bitwise_or >> 1) | bitwise_xor;
    
    // Final result calculation
    int result = ((intermediate + len_alpha * len_beta) & 0xFF) ^ (combined_flags % 100);
    
    printf("Result: %d\n", result);
    return 0;
}