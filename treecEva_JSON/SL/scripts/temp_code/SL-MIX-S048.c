#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct DataPoint {
    int values[5];
    double weight;
    char label[20];
};

struct ComplexData {
    struct DataPoint points[3];
    int count;
    unsigned int flags;
};

int main() {
    struct ComplexData data = {
        {
            {{10, 20, 30, 40, 50}, 1.5, "alpha"},
            {{5, 15, 25, 35, 45}, 2.0, "beta"},
            {{2, 4, 6, 8, 10}, 0.5, "gamma"}
        },
        3,
        0xF0F0
    };

    int intermediate_sum = 0;
    double weighted_avg = 0.0;
    unsigned int mask = 0x0F0F;
    char buffer[MAX_LEN];
    int final_result = 0;

    // Stage 1: Calculate intermediate sum
    for (int i = 0; i < data.count; i++) {
        for (int j = 0; j < 5; j++) {
            if (data.points[i].values[j] % 2 == 0) {
                intermediate_sum += data.points[i].values[j];
            }
        }
    }

    // Stage 2: Apply bitwise operations
    data.flags = data.flags & mask;
    data.flags = data.flags << 2;
    
    // Stage 3: Calculate weighted average
    for (int i = 0; i < data.count; i++) {
        double sum = 0;
        for (int j = 0; j < 5; j++) {
            sum += data.points[i].values[j];
        }
        weighted_avg += (sum / 5) * data.points[i].weight;
    }
    weighted_avg /= data.count;

    // Stage 4: String manipulation
    strcpy(buffer, "Result: ");
    sprintf(buffer + strlen(buffer), "%d", (int)weighted_avg);
    strcat(buffer, " - ");
    sprintf(buffer + strlen(buffer), "%u", data.flags);

    // Stage 5: Final calculation
    final_result = (intermediate_sum >> 2) ^ (int)floor(weighted_avg);
    final_result += strlen(buffer);
    
    // Apply final bitwise operation
    final_result = (final_result & 0xFF) | ((data.flags >> 8) & 0xFF);

    printf("Result: %d\n", final_result);
    return 0;
}