#include <iostream>
using namespace std;

int N;
int x1[100], x2[100];

bool isCross(int x1t, int x2t, int x1p, int x2p){

    if((x1t < x1p && x2t > x2p) ||
       (x1t > x1p && x2t < x2p)){
        return true;
    }
    return false;
}

int main() {
    cin >> N;

    for(int i=0; i<N; i++){
        cin >> x1[i] >> x2[i];
    }

    bool meet[100] = {};
    int answer = 0;

    for(int i=0; i<N; i++){
        int x1t = x1[i];
        int x2t = x2[i];

        for(int j=i+1; j<N; j++){
            int x1p = x1[j];
            int x2p = x2[j];

            if(isCross(x1t, x2t, x1p, x2p)){
                meet[i] = true;
                meet[j] = true;
            }
        }
    }

    for(int i=0; i<N; i++){
        if(meet[i] == false){
            answer++;
        }
    }

    cout << answer;
    return 0;
}