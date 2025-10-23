#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

typedef struct {
    int num_stages;
    double attenuation_factors[];  // Flexible array member
} FilterChain;

double apply_gain(double input, double gain_factor) {
    return input * log(gain_factor + 1.0);
}

double apply_decay(double input, double decay_rate) {
    return input * exp(-decay_rate);
}

typedef double (*ProcessorFunc)(double, double);

int main() {
    // Initialize filter chain with 3 stages
    FilterChain* chain = malloc(sizeof(FilterChain) + 3 * sizeof(double));
    chain->num_stages = 3;
    chain->attenuation_factors[0] = 2.5;
    chain->attenuation_factors[1] = 1.8;
    chain->attenuation_factors[2] = 3.2;
    
    double base_impedance = 400.0;
    double processed_impedance = base_impedance;
    
    ProcessorFunc processors[2] = {apply_gain, apply_decay};
    int use_gain = 1;
    
    for (int i = 0; i < chain->num_stages; i++) {
        double factor = chain->attenuation_factors[i];
        processed_impedance = processors[use_gain](processed_impedance, factor);
        use_gain = (use_gain == 0) ? 1 : 0;  // Toggle between gain and decay
    }
    
    double final_impedance = (processed_impedance > 300.0) ? 
                             pow(processed_impedance, 0.75) : 
                             processed_impedance * 1.5;
    
    printf("Result: %.6f\n", final_impedance);
    free(chain);
    return 0;
}