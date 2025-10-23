#define _USE_MATH_DEFINES
#include <stdio.h>

int main() {
    volatile unsigned char device_status[4] = {0x00, 0x00, 0x00, 0x00};
    volatile unsigned char *status_ptr = device_status;
    unsigned int interrupt_mask = 0xF0;
    unsigned int active_interrupts = 0;
    
    // Simulate device 1 setting interrupt flag
    *(status_ptr + 1) |= 0x10;  // Set bit 4
    
    // Simulate device 2 setting interrupt flag
    *(status_ptr + 2) |= 0x20;  // Set bit 5
    
    // Clear device 1 interrupt if device 2 is active (conditional)
    if (*(status_ptr + 2) & 0x20) {
        *(status_ptr + 1) &= ~0x10;
    }
    
    // Combine status registers with mask
    active_interrupts = (*(status_ptr + 1) & interrupt_mask) | 
                       (*(status_ptr + 2) & interrupt_mask);
    
    // Apply ternary operation to handle special case
    active_interrupts = (active_interrupts > 0x20) ? 
                        (active_interrupts | 0x80) : 
                        (active_interrupts & 0x7F);
    
    // Final adjustment based on combined conditions
    active_interrupts = (active_interrupts & 0x80) ? 
                        (active_interrupts ^ 0xAA) : 
                        (active_interrupts | 0x55);
    
    printf("Result: %u\n", active_interrupts);
    return 0;
}