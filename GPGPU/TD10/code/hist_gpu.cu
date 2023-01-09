
#include <stdio.h>
#include <string.h>
#include "text.h"
#include <iostream>

#define NB_ASCII_CHAR 128
const int threadsPerBlock = 256;


__global__
void histo_kernell( unsigned char *buffer , long size , unsigned int *histo ) {
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    int stride = blockDim.x * gridDim.x;
    while (i < size) {
        atomicAdd(&(histo[buffer[i]]), 1);
        i += stride;
    }

}

__global__
void histo_kernell_private(unsigned char *buffer, long size, unsigned int *histo){
    __shared__ unsigned int histo_private[NB_ASCII_CHAR];

    int i = threadIdx.x + blockIdx.x * blockDim.x;
    int stride = blockDim.x * gridDim.x;
    if (threadIdx.x < NB_ASCII_CHAR) histo_private[buffer[i]] = 0;
    __syncthreads();

    while (i < size) {
        atomicAdd(&(histo_private[buffer[i]]), 1);
        i += stride;
    }
    __syncthreads();

    if (i < NB_ASCII_CHAR)
        atomicAdd(&(histo[threadIdx.x]), histo_private[threadIdx.x]);
    __syncthreads();
}

int main( void ) {
    int len = strlen(h_str);
    printf("len:%d\n", len);
    int size = len*sizeof(char);
    const int blocksPerGrid = (size+threadsPerBlock-1) / threadsPerBlock ;

    // CPU computation
    u_int histo[NB_ASCII_CHAR] = {0};
    for (int i = 0; i < len; i++){
            histo[h_str[i]]++;
    }    
    //for (int bean = 0; bean < NB_ASCII_CHAR; bean++) {
    //    std::cout << (char) bean << " : " << histo[bean] << std::endl;
    //}

    // GPU computation
    u_int histo_gpu[NB_ASCII_CHAR] = {0};
    u_int *d_histo;
    u_char *d_str;
    cudaMalloc( (void**)&d_histo, NB_ASCII_CHAR * sizeof(u_int) );
    cudaMalloc( (void**)&d_str, size );
    cudaMemcpy( d_str, h_str, size, cudaMemcpyHostToDevice );
    cudaMemcpy( d_histo, histo_gpu, NB_ASCII_CHAR * sizeof(u_int), cudaMemcpyHostToDevice );
    histo_kernell_private<<<blocksPerGrid, threadsPerBlock>>>(d_str, size, d_histo);
    cudaMemcpy( histo_gpu, d_histo, NB_ASCII_CHAR*sizeof(u_int), cudaMemcpyDeviceToHost );
    for (int bean = 0; bean < NB_ASCII_CHAR; bean++) {
        std::cout << (char) bean << " : " << histo_gpu[bean] << " / " << histo[bean] << std::endl;
    }
    return 0;
}   
