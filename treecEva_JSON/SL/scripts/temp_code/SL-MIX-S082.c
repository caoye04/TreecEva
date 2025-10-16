#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int numCoeffs;
    double coeffs[];  // flexible array member
} DigitalFilter;

// Function pointer type for coefficient processing
typedef double (*CoeffProcessor)(double);

// Coefficient processing functions
double amplify(double x) { return x * 1.5; }
double attenuate(double x) { return x * 0.7; }
double invert(double x) { return -x; }

// Custom memory management function
DigitalFilter* createFilter(int size) {
    DigitalFilter* filter = malloc(sizeof(DigitalFilter) + size * sizeof(double));
    filter->numCoeffs = size;
    return filter;
}

int main() {
    // Create filter with 4 coefficients
    DigitalFilter* filter = createFilter(4);
    
    // Initialize coefficients
    filter->coeffs[0] = 2.0;
    filter->coeffs[1] = -1.5;
    filter->coeffs[2] = 3.2;
    filter->coeffs[3] = -0.8;
    
    // Function pointer array for processing
    CoeffProcessor processors[3] = {amplify, attenuate, invert};
    
    double processedSignal = 0.0;
    int processorIndex = 0;
    
    // Process coefficients through the pipeline
    for (int i = 0; i < filter->numCoeffs; i++) {
        // Apply processor based on index and coefficient value
        if (filter->coeffs[i] > 0.0 && processorIndex < 3) {
            processedSignal += processors[processorIndex](filter->coeffs[i]);
            processorIndex = (processorIndex + 1) % 3;
        } else if (!(filter->coeffs[i] > 0.0)) {
            processedSignal += fabs(filter->coeffs[i]);
        } else {
            processedSignal += filter->coeffs[i];
        }
    }
    
    // Apply final processing step
    if (processedSignal > 5.0 || processorIndex == 0) {
        processedSignal *= 0.9;
    } else {
        processedSignal += 1.1;
    }
    
    printf("Result: %.6f\n", processedSignal);
    
    // Clean up
    free(filter);
    return 0;
}