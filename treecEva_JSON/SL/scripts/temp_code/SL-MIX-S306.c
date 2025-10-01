#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_SIZE 5

struct DataPoint {
    double values[3];
    int flags;
};

struct ComputationUnit {
    struct DataPoint points[MAX_SIZE];
    int count;
};

int main() {
    struct ComputationUnit unit = {
        .points = {
            {.values = {1.5, 2.0, 3.5}, .flags = 3},
            {.values = {4.0, 5.5, 6.0}, .flags = 5},
            {.values = {7.5, 8.0, 9.5}, .flags = 7},
            {.values = {10.0, 11.5, 12.0}, .flags = 9},
            {.values = {13.5, 14.0, 15.5}, .flags = 11}
        },
        .count = MAX_SIZE
    };

    double accumulator = 0.0;
    double result = 0.0;

    for(int i=0; i<unit.count; i++) {
        struct DataPoint *p = &unit.points[i];
        for(int j=0; j<3; j++) {
            if(p->flags & (1<<j)) {
                double temp = pow(p->values[j], 2);
                accumulator += sqrt(temp) * ((p->flags >> j) & 1 ? 1 : -1);
            }
        }
        result = accumulator / (i+1) + sin(accumulator) * cos(i);
    }

    printf("Result: %.6f\n", result);
    return 0;
}