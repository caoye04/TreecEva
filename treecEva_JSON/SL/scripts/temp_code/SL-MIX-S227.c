#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

struct ConfigRegister {
    uint8_t mode : 3;
    uint8_t enabled : 1;
    uint8_t reserved : 4;
};

int main() {
    volatile uint8_t system_flags = 0b10110010;
    uint8_t final_status_mask = 0;
    struct ConfigRegister reg = {0};
    
    for (int i = 0; i < 4; i++) {
        reg.mode = i + 1;
        reg.enabled = (i % 2);
        
        for (int j = 0; j < 2; j++) {
            if ((reg.mode & 0x01) == j) {
                system_flags ^= (0x10 << j);
            }
        }
        
        if (reg.enabled) {
            final_status_mask |= (reg.mode << (i * 2));
        } else {
            final_status_mask &= ~(reg.mode << (i * 2));
        }
    }
    
    printf("Result: %d\n", final_status_mask);
    return 0;
}