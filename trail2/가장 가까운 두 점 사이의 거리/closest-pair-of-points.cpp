#include <iostream>

using namespace std;

int n;
int x[100], y[100];
int min1 = 10000000;
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            int x1 = x[i], y1 = y[i];
            int x2 = x[j], y2 = y[j];
        
            int cal = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
            if(cal<=min1){
                min1 = cal;
            }
        }
    }
    // Please write your code here.
    cout<<min1;
    return 0;
}