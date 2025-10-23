#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MOD_MASK 0xFF
#define TRIG_SCALE 1000.0
#define SIGNAL_COUNT 5

float trig_encoder(float input) {
    return sin(input) * TRIG_SCALE;
}

int modular_reducer(float value) {
    return ((int)value) % MOD_MASK;
}

int bit_scrambler(int value) {
    return (value << 2) ^ (value >> 1);
}

int main() {
    float signal_waveform[SIGNAL_COUNT] = {0.5, 1.2, 0.8, 2.1, 1.7};
    float (*encoder_func)(float) = trig_encoder;
    int (*reducer_func)(float) = modular_reducer;
    int (*scrambler_func)(int) = bit_scrambler;
    
    int encoded_signal = 0;
    
    for (int i = 0; i < SIGNAL_COUNT; i++) {
        float encoded = encoder_func(signal_waveform[i]);
        int reduced = reducer_func(encoded);
        int scrambled = scrambler_func(reduced);
        encoded_signal = (encoded_signal + scrambled) & MOD_MASK;
    }
    
    printf("Result: %d\n", encoded_signal);
    return 0;
}