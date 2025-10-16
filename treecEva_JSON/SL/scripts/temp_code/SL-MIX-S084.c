#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

// Function pointer type for signal processing callbacks
typedef double (*signal_processor)(double, double);

// Signal processing functions
double amplify(double signal, double gain) {
    return signal * gain;
}

double filter(double signal, double threshold) {
    return (signal > threshold) ? signal : 0.0;
}

// Union for type punning between float and int representations
union signal_representation {
    float amplitude;
    int encoded_value;
};

int main() {
    // Volatile variables for signal processing parameters
    volatile double frequencies[] = {120.5, 60.0, 240.0, 300.0, 180.0};
    volatile double amplitudes[] = {0.3, 0.9, 0.6, 0.2, 0.75};
    volatile int num_components = 5;
    
    // Processing function pointers
    signal_processor processors[2] = {amplify, filter};
    
    // Greedy selection of dominant frequency
    double max_weighted_value = -1.0;
    int dominant_index = -1;
    
    for (int i = 0; i < num_components; i++) {
        // Apply signal processing pipeline
        double processed = processors[0](amplitudes[i], 2.0); // Amplify
        processed = processors[1](processed, 1.0);            // Filter
        
        // Calculate weighted value for dominance selection
        double weighted_value = processed * frequencies[i];
        
        // Short-circuit evaluation in conditional
        if (weighted_value > max_weighted_value && processed > 0.0) {
            max_weighted_value = weighted_value;
            dominant_index = i;
        }
    }
    
    // Early return if no dominant frequency found
    if (dominant_index == -1) {
        printf("Result: 0\n");
        return 0;
    }
    
    // Type punning to encode the dominant frequency
    union signal_representation encoded;
    encoded.amplitude = (float)frequencies[dominant_index];
    
    // Final calculation using the encoded value
    int dominant_frequency = encoded.encoded_value & 0xFFFF; // Mask to lower 16 bits
    
    // Apply correction factor based on comparison
    if (dominant_frequency > 16000) {
        dominant_frequency /= 2;
    } else {
        dominant_frequency *= 3;
    }
    
    printf("Result: %d\n", dominant_frequency);
    return 0;
}