#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct PriorityPacket {
    unsigned int flag : 4;
    unsigned int priority : 3;
    unsigned int reserved : 1;
};

typedef int (*Comparator)(const void*, const void*);

int compare_packets(const void* a, const void* b) {
    struct PriorityPacket* pa = (struct PriorityPacket*)a;
    struct PriorityPacket* pb = (struct PriorityPacket*)b;
    return (pb->priority << 4 | pb->flag) - (pa->priority << 4 | pa->flag);
}

int main() {
    struct PriorityPacket packets[4] = {
        {0x7, 0x3, 0},
        {0x2, 0x5, 0},
        {0xE, 0x1, 0},
        {0x5, 0x4, 0}
    };
    
    // Apply mask and modify flags
    for(int i=0; i<4; i++) {
        packets[i].flag &= 0x7;
    }
    
    // Sort packets based on custom comparator
    qsort(packets, 4, sizeof(struct PriorityPacket), compare_packets);
    
    int dp_table[4];
    dp_table[0] = packets[0].priority * 10 + packets[0].flag;
    
    for(int j=1; j<4; j++) {
        int current_val = packets[j].priority * 10 + packets[j].flag;
        switch(j) {
            case 1:
                dp_table[j] = (current_val > dp_table[j-1]) ? current_val : dp_table[j-1];
                break;
            case 2:
                if(current_val % 2 == 0) {
                    dp_table[j] = dp_table[j-1] + (current_val >> 1);
                } else {
                    dp_table[j] = dp_table[j-1] - (current_val & 0x3);
                }
                break;
            case 3:
                dp_table[j] = dp_table[j-1] ^ current_val;
                break;
            default:
                dp_table[j] = dp_table[j-1];
        }
    }
    
    int control_output = dp_table[3] & 0xFF;
    printf("Result: %d\n", control_output);
    return 0;
}