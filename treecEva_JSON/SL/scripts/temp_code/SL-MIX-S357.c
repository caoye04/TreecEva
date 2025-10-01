#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize a complex nested data structure
    struct InnerData {
        int values[3];
        double factor;
    };
    
    struct OuterData {
        struct InnerData inner[2];
        char label[20];
    };
    
    struct OuterData data = {
        .inner = {
            {{10, 20, 30}, 1.5},
            {{40, 50, 60}, 2.0}
        },
        .label = "Test Data"
    };
    
    // Perform calculations using the data structure
    int sum1 = data.inner[0].values[0] + data.inner[0].values[1] + data.inner[0].values[2];
    int sum2 = data.inner[1].values[0] + data.inner[1].values[1] + data.inner[1].values[2];
    
    // Apply mathematical operations
    double sqrt_sum1 = sqrt(sum1);
    double pow_sum2 = pow(sum2, data.inner[1].factor);
    
    // Perform bitwise operations
    int bitwise_result = (int)(sqrt_sum1) & (int)(pow_sum2);
    
    // Perform logical operations
    int logical_result = (sum1 > sum2) ? (bitwise_result | 0xF0) : (bitwise_result & 0x0F);
    
    // String manipulation
    int label_len = strlen(data.label);
    
    // Complex calculation combining all results
    int final_result = (logical_result ^ label_len) + (int)(data.inner[0].factor * data.inner[1].factor);
    
    // Print the result
    printf("Result: %d\n", final_result);
    
    return 0;
}