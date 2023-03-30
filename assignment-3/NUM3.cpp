#include <iostream>

using namespace std;

int main()
{
    int N = 100;
    double arr[N][4] = {0};
    double vec_B[N];
    double vec_Y[N];
    double Det = 1;
    
    cout.precision(16);

    for(int j = 0; j < N; j++)
	{
        arr[j][1] = 1.2;

        if(j < N - 1)
		{
            arr[j][0] = 0.2;
            arr[j][2] = 0.1 / (j+1);
        }
        if(j < N - 2)
		{
            arr[j][3] = 0.4 / ((j + 1) * (j + 1));
        }
		      
    }
    
    arr[0][0] = arr[0][0] / arr[0][1];
    for(int j = 1; j < N; j++)
	{
        arr[j][1] = arr[j][1] - arr[j - 1][0] * arr[j - 1][2];

        if(j < N - 1)
		{
            arr[j][0] = arr[j][0] / arr[j][1];
            arr[j][2] = arr[j][2] - arr[j - 1][0] * arr[j - 1][3];
        }                
    }

    vec_B[0] = 1;
    for(int j = 1; j < N; j++)
	{
        vec_B[j] = (j + 1) - arr[j-1][0] * vec_B[j - 1];
    }

    vec_Y[N - 1] = vec_B[N - 1] / arr[N - 1][1];
    vec_Y[N - 2] = (vec_B[N - 2] - arr[N - 2][2] * vec_Y[N - 1]) / arr[N - 2][1];
    
    for(int j = N - 3; j >= 0; j--) 
	{
        vec_Y[j] = (vec_B[j] - arr[j][2] * vec_Y[j + 1] - arr[j][3] * vec_Y[j + 2]) / arr[j][1];
    }

    for(int j = 0; j < N; j++)
	{
        Det *= arr[j][1];
    }
    cout << "wyznacznik macierzy A: " << Det << endl;
    
    cout << "wektor y: " << endl;
    for(int j = 0; j < N; j++)
    {
        cout << vec_Y[j] << endl;
    }
}
