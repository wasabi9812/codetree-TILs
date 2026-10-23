#include <iostream>
using namespace std;

int N;
int A[100], B[100];

void work(int t[], int a, int b){
    for(int i=a; i<b; i++){
        t[i]++;
    }
}

int cal(int t[]){
    int cnt=0;
    for(int i=0; i<1001; i++){
        if(t[i]>0){
            cnt++;
        }
    }
    return cnt;
}

int main() {
    cin >> N;
    int max=0;

    for(int i=0; i<N; i++){
        cin >> A[i] >> B[i];
    }

    for(int i=0; i<N; i++){

        int arr[1001] = {};

        for(int j=0; j<N; j++){
            if(j==i){
                continue;
            }

            int a=A[j], b=B[j];
            work(arr, a,b);
        }

        int temp=cal(arr);

        if(temp>=max){
            max=temp;
        }
    }

    cout << max;

    return 0;
}