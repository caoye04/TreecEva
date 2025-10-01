#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 10

struct DataPoint {
    int values[3];
    double weight;
};

struct DataGroup {
    struct DataPoint points[2];
    char label[10];
};

int main() {
    struct DataGroup groups[2] = {
        {{ {{1, 2, 3}, 0.5 }, { {4, 5, 6}, 0.7 } }, "GroupA"},
        {{ {{7, 8, 9}, 0.9 }, { {10, 11, 12}, 1.1 } }, "GroupB"}
    };
    
    int i, j, k;
    double sum = 0.0;
    int count = 0;
    double weighted_sum = 0.0;
    
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            for (k = 0; k < 3; k++) {
                sum += sqrt(pow(groups[i].points[j].values[k], 2));
                count += (groups[i].points[j].values[k] % 2 == 0) ? 1 : 0;
            }
            weighted_sum += (sum * groups[i].points[j].weight);
        }
    }
    
    int result = (int)(weighted_sum / count) + ((int)sum & 0xF);
    
    printf("Result: %d\n", result);
    
    return 0;
}