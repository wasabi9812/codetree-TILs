#include <iostream>
using namespace std;

int N;
int x[100], y[100];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x[i] >> y[i];
    }

    int answer = 2000000000;  // 추가

    for(int q=0; q<N; q++){

        // 여기로 이동
        int max_x = -400001;
        int min_x = 400001;
        int max_y = -400001;
        int min_y = 400001;

        for(int i=0; i<N; i++){
            if(i==q){
                continue;
            }

            if(x[i]>=max_x){
                max_x=x[i];
            }
            if(x[i]<=min_x){
                min_x=x[i];
            }
            if(y[i]>=max_y){
                max_y=y[i];
            }
            if(y[i]<=min_y){
                min_y=y[i];
            }
        }

        // for문 안으로 이동
        int width = max_x-min_x;
        int height = max_y-min_y;

        if(width*height < answer){
            answer = width*height;
        }
    }

    cout << answer;

    return 0;
}