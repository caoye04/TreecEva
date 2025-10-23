#define _USE_MATH_DEFINES
#include <stdio.h>

union config_register {
    unsigned char byte;
    struct {
        unsigned int flag_a : 1;
        unsigned int flag_b : 1;
        unsigned int flag_c : 1;
        unsigned int flag_d : 1;
        unsigned int reserved : 4;
    } bits;
};

int main() {
    union config_register reg;
    
    reg.bits.flag_a = 1;
    reg.bits.flag_b = 0;
    reg.bits.flag_c = 1;
    reg.bits.flag_d = 1;
    
    // Execution point Y
    unsigned char control_byte = reg.byte;
    
    printf("Result: %d\n", control_byte);
    return 0;
}