#define _USE_MATH_DEFINES
#include <stdio.h>
#define FLAG_A 0x01
#define FLAG_B 0x02
#define FLAG_C 0x04
#define FLAG_D 0x08

int main() {
    unsigned char reg_status = 0x0A;  // Initial register state
    
    // Apply flag updates
    reg_status |= FLAG_A;              // Set FLAG_A
    reg_status &= ~FLAG_B;             // Clear FLAG_B
    reg_status ^= FLAG_C;              // Toggle FLAG_C
    
    // Check final condition
    if ((reg_status & FLAG_D) && !(reg_status & FLAG_B)) {
        reg_status |= 0x10;            // Set bit 4 if condition met
    }
    
    printf("Result: %d\n", reg_status);
    return 0;
}