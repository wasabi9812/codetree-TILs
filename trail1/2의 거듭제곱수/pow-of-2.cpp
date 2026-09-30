#include <iostream>
using namespace std;

int main() {
    int a;
    cin>>a;
    int b = 1;
    int cnt = 0;
    while(1){
        
        if(b==a){
            break;
        }
        b = b*2;
        cnt+=1;
    }

    cout<<cnt;
    return 0;
}