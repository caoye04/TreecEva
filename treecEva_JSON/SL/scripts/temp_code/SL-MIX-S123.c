#define _USE_MATH_DEFINES
#include <stdio.h>

struct AudioConfig {
    unsigned int eq_enabled : 1;
    unsigned int compressor_active : 1;
    unsigned int stereo_mode : 2;
    unsigned int sample_rate : 4;
};

int main() {
    struct AudioConfig processor;
    
    processor.eq_enabled = 1;
    processor.compressor_active = 0;
    processor.stereo_mode = 2;
    processor.sample_rate = 9;
    
    if (processor.stereo_mode > 1) {
        processor.compressor_active = 1;
    }
    
    if (processor.sample_rate >= 8) {
        processor.eq_enabled = 0;
    }
    
    unsigned int audio_flags = *((unsigned int*)&processor);
    printf("Result: %u\n", audio_flags);
    return 0;
}