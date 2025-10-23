#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SCALE_FACTOR 2.5
#define LOG_BASE_SCALE(x) (log(x) / log(SCALE_FACTOR))

typedef double (*transform_func)(double);

double amplify_signal(double input) {
    return pow(input, 1.5);
}

double attenuate_signal(double input) {
    return LOG_BASE_SCALE(input);
}

int main() {
    double raw_intensity = 16.0;
    transform_func pipeline[2];
    
    pipeline[0] = amplify_signal;
    pipeline[1] = attenuate_signal;
    
    double processed = raw_intensity;
    for(int i = 0; i < 2; i++) {
        processed = pipeline[i](processed);
    }
    
    double final_intensity = processed * 10;
    printf("Result: %.4f\n", final_intensity);
    return 0;
}