#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

struct ProcessControl {
    unsigned int mode : 3;
    unsigned int enable_stats : 1;
    unsigned int reserved : 4;
};

union DataRegister {
    unsigned int raw;
    struct ProcessControl ctrl;
};

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

double compute_variance(int* samples, int count) {
    double sum = 0, mean = 0;
    for (int i = 0; i < count; i++) sum += samples[i];
    mean = sum / count;
    double variance = 0;
    for (int i = 0; i < count; i++) {
        variance += (samples[i] - mean) * (samples[i] - mean);
    }
    return variance / count;
}

int main() {
    union DataRegister reg;
    reg.raw = 0;
    reg.ctrl.mode = 5;
    reg.ctrl.enable_stats = 1;
    
    int waveformEnergy = 0;
    int sampleBuffer[8];
    int mask = 0xF0;
    
    for (int i = 0; i < 8; i++) {
        sampleBuffer[i] = fibonacci(i) & mask;
    }
    
    switch(reg.ctrl.mode) {
        case 5:
            if (reg.ctrl.enable_stats && (sampleBuffer[3] > 0 || sampleBuffer[4] > 0)) {
                double variance = compute_variance(sampleBuffer, 8);
                waveformEnergy = (int)(variance * 100) & 0xFF;
            } else {
                waveformEnergy = 0;
            }
            break;
        default:
            waveformEnergy = -1;
    }
    
    if ((waveformEnergy & 0x80) && (reg.ctrl.mode == 5)) {
        waveformEnergy ^= 0xAA;
    }
    
    printf("Result: %d\n", waveformEnergy);
    return 0;
}