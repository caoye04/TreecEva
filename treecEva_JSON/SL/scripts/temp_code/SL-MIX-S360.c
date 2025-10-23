#define _USE_MATH_DEFINES
#include <stdio.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    unsigned short config_register = 0x1234;  // Initial register value
    unsigned short mask = 0x00F0;              // Mask to apply
    int a = 48, b = 18;                        // Values for GCD calculation
    
    // Short-circuit evaluation: only calculate GCD if both values are non-zero
    int gcd_result = (a && b) ? gcd(a, b) : 0;
    
    // Apply mask only if GCD result is greater than 5
    unsigned short final_register_value = (gcd_result > 5) ? 
        (config_register | mask) : config_register;
    
    printf("Result: %hu\n", final_register_value);
    return 0;
}