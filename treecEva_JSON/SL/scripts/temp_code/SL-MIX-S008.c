#include <stdio.h>
#include <math.h>
#include <string.h>

struct InnerData {
    int values[3];
    char tag[8];
};

struct OuterData {
    struct InnerData inner;
    double factor;
    int flags;
};

int main() {
    struct OuterData data = {
        .inner.values = {12, 25, 9},
        .inner.tag = "RESULT",
        .factor = 2.5,
        .flags = 0b11010010
    };

    // Step 1: Bitwise manipulation
    int mask = 0xF0;
    int masked_flags = data.flags & mask;
    int shifted_flags = masked_flags >> 4;

    // Step 2: Mathematical operations
    double sqrt_val = sqrt((double)data.inner.values[1]);
    double power_val = pow((double)data.inner.values[0], 2.0);
    double trig_val = sin(M_PI / 6); // 30 degrees

    // Step 3: String operations
    int tag_len = strlen(data.inner.tag);
    char last_char = data.inner.tag[tag_len - 1];
    int char_code = (int)last_char;

    // Step 4: Complex calculation chain
    double intermediate = (power_val * data.factor) + (trig_val * 100);
    int result = (int)(intermediate) ^ shifted_flags;
    result = result + (char_code * 2) - (int)sqrt_val;

    // Step 5: Final adjustment using all components
    if ((data.flags & 0x01) == 1) {
        result = result << 1;
    } else {
        result = result >> 1;
    }

    result = result + (data.inner.values[2] * 3);

    printf("%d\n", result);
    return 0;
}