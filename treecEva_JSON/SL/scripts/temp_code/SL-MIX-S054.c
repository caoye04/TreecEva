#define _USE_MATH_DEFINES
#include <stdio.h>

#define PERIPH_UART_MASK    0x01
#define PERIPH_SPI_MASK     0x02
#define PERIPH_I2C_MASK     0x04
#define PERIPH_ADC_MASK     0x08

int main() {
    volatile unsigned char periph_config = 0x0F;  // All peripherals initially enabled
    
    // Disable UART and SPI
    periph_config &= ~(PERIPH_UART_MASK | PERIPH_SPI_MASK);
    
    // Toggle I2C (if enabled, disable; if disabled, enable)
    periph_config ^= PERIPH_I2C_MASK;
    
    // Enable ADC if not already enabled
    periph_config |= PERIPH_ADC_MASK;
    
    printf("Result: %d\n", periph_config);
    return 0;
}