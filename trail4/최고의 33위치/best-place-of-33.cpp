#include <iostream>

using namespace std;

int N;
int grid[20][20];

int calbox(int i, int j){
    int cnt=0;
    for(int t=i-1; t<i+2; t++){
        for(int k=j-1; k<j+2; k++){
            if(grid[t][k]==1){
                cnt++;    
            }
        }
    }
    return cnt;
}


int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    int max = 0;

    // Please write your code here.
    for(int i=1; i<N-1; i++){
        for(int j=1; j<N-1; j++){
            int temp = calbox(i,j);
            if(max<=temp){
                max = temp;
            }
        }
    }

    cout<<max;

    return 0;
}
