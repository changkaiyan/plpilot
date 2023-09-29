Here is an example C program that demonstrates integer overflow:
c
#include <stdio.h>

int main() {
    // sizeof(int) is 4 bytes (32 bits)
    int num = 2147483647;  // Max value of signed int
    printf("num = %d\n", num);
    
    num++;
    
    // This overflows and wraps around to the min int value 
    printf("num after increment = %d\n", num);  
    
    // Unsigned int has max value of 4294967295 
    unsigned int unum = 4294967295; 
    printf("unum = %u\n", unum);
    
    unum++;
    
    // This overflows but wraps around properly for unsigned int
    printf("unum after increment = %u\n", unum);
}