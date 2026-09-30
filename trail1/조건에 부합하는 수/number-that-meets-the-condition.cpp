#include <iostream>
using namespace std;

int main() {
    int a;
    cin>>a;

    for (int i=1; i<a+1; i++){
        if (i%2==0 && i%4!=0){
            continue;
        }
        int temp = i/8;
        if (temp%2==0){
            continue;
        }
        int temp2 =i%7;
        if(temp2<4){
            continue;
        }
        cout<<i<<" ";
    }

    return 0;
}