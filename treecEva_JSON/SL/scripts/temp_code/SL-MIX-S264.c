#define _USE_MATH_DEFINES
#include <stdio.h>

struct ConfigRegister {
    unsigned int adc_enabled : 1;
    unsigned int dac_enabled : 1;
    unsigned int spi_mode : 2;
    unsigned int reserved : 4;
};

int main() {
    struct ConfigRegister reg;
    reg.adc_enabled = 1;
    reg.dac_enabled = 0;
    reg.spi_mode = 2;
    reg.reserved = 0;
    
    int operational_mode = 0;
    if (reg.adc_enabled == 1 && reg.dac_enabled == 0) {
        operational_mode = reg.spi_mode * 2 + 1;
    } else {
        operational_mode = -1;
    }
    
    printf("Result: %d\n", operational_mode);
    return 0;
}