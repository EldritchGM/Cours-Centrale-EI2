 #include <iostream>
 #include <math.h>
 #include <assert.h>
 
 using namespace std;

 #define N (2048*2048)
 #define THREADS_PER_BLOCK 512

void initMatrix(float *m, int numRows, int numCols);
void computeMatrixMulCPU(float *A, float *B, float *C, int numCRows, int numCColumns, int itd_num);
void compareMatrix(float *A, float *B, int numRows, int numColumns);

int main(int argc, char *argv[])
{
    int numARows = atoi(argv[1]); // number of rows in the matrix A
    int numAColumns = atoi(argv[2]); // number of columns in the matrix A
    int numBRows = atoi(argv[3]); // number of rows in the matrix B
    int numBColumns = atoi(argv[4]); // number of columns in the matrix B
    int numCRows = numARows; // number of rows in the matrix C
    int numCColumns = numBColumns; // number of columns in the matrix C 
    assert(numAColumns == numBRows);

    float *A = (float *)malloc(numARows*numAColumns*sizeof(float));
    float *B = (float *)malloc(numBRows*numBColumns*sizeof(float));
    float *C = (float *)malloc(numCRows*numCColumns*sizeof(float));
    float *D = (float *)malloc(numCRows*numCColumns*sizeof(float));

    float *d_D;
    cudaMalloc(void **) &d_D, numCRows*numCColumns*sizeof(float);

    // Initialize matrices on the host
    initMatrix(A, numARows, numAColumns);
    initMatrix(B, numBRows, numBColumns);

    computeMatrixMulCPU(A, B, C, numCRows, numCColumns, numAColumns);
    
    compareMatrix(C, C, numCRows, numCColumns);

    free(A);
    free(B);
    free(C);
    
    return 0;
}

void initMatrix(float *m, int numRows, int numCols){
    for (int i=0; i<numRows; i++){
        for (int j=0; j<numCols; j++){
            m[i*numCols+j] = sin(i*numCols+j);
        }
    }
}

void computeMatrixMulCPU(float *A, float *B, float *C, int numCRows, int numCColumns, int itd_num){
    // This function must return in C the result of the multiplication of the matrix A by the matrix B
    for (int i = 0; i < numCRows; i++){
        for (int j = 0; j < numCColumns; j++){
            for (int k = 0; k < itd_num; k++) {
                C[i * numCColumns + j] = A[i * itd_num + k] * B[k * numCColumns + j];
            }
        }
    }
}

__global__

void computeMatrixMulGPU(float *A, float *B, float *C, int numCRows, int numCColumns, int itd_num){
    int x = threadIdx.x + blockIdx.x * blockDim.y
    int y = threadIdx.x + blockIdx.y * blockDim.y

    if (x < numColumns && y < numCRows) {
        index_c = y * numCColumns + x
    }

    for (int k; k < itd_num; k++) {
        C[index_c] = A[y * numAColumns + k] * B[k * numCColumns + x]
    }
}

void compareMatrix(float *A, float *B, int numRows, int numColumns){
    for (int row = 0; row < numRows; row++){
        for (int col = 0; col < numColumns; col++){            
            assert(A[row*numColumns+col] == B[row*numColumns+col]);
        }
    }
    cout << "The matrices are identical" << endl;
}