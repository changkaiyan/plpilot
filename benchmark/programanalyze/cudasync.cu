#include <cuda_runtime.h>

__global__ void kernel1() {
    printf("Kernel 1 launching\n");
}

__global__ void kernel2() {
    printf("Kernel 2 launching\n");
}

int main() {
    kernel1<<<1, 1>>>();
    
    // Launch kernel2 without synchronizing from kernel1 - error!
    kernel2<<<1, 1>>>();
    
    cudaDeviceSynchronize(); 
}