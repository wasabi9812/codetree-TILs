#include <iostream>
using namespace std;

int N;
int x[100];
int y[100];

int makePositive(int a){
    if(a < 0){
        return a * (-1);
    }
    else{
        return a;
    }
}

int main() {
    cin >> N;

    for(int i=0; i<N; i++){
        cin >> x[i] >> y[i];
    }

    int answer = 0;

    for(int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            for(int k=j+1; k<N; k++){

                int x1=x[i], x2=x[j], x3=x[k];
                int y1=y[i], y2=y[j], y3=y[k];

                int tempx=0, tempy=0;
                bool checkX=false, checkY=false;

                if(x1==x2){
                    tempx = makePositive(x1-x3);
                    checkX = true;
                }
                else if(x2==x3){
                    tempx = makePositive(x2-x1);
                    checkX = true;
                }
                else if(x3==x1){
                    tempx = makePositive(x3-x2);
                    checkX = true;
                }

                if(y1==y2){
                    tempy = makePositive(y1-y3);
                    checkY = true;
                }
                else if(y2==y3){
                    tempy = makePositive(y2-y1);
                    checkY = true;
                }
                else if(y3==y1){
                    tempy = makePositive(y3-y2);
                    checkY = true;
                }

                if(checkX && checkY){
                    int area = tempx * tempy;

                    if(area > answer){
                        answer = area;
                    }
                }
            }
        }
    }

    cout << answer;
    return 0;
}