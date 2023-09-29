#include <cuda_runtime.h>

__global__ void kernel() {
    // Grid has only 100 blocks, but each block has 1024 threads!
    // This leads to thread overflow as 104,400 threads are launched
    printf("Thread %d in block %d\n", threadIdx.x, blockIdx.x);
}

int main() {
    const int num_blocks = 100;
    const int threads_per_block = 1024;
    const int num_threads = num_blocks * threads_per_block;
    
    kernel<<<num_blocks, threads_per_block>>>(); 
    
    cudaDeviceSynchronize(); 
}