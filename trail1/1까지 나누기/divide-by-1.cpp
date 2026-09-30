#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a,cnt;
    cin>>a;

    cnt =0;
    for (int i=1;; i++){
        a = a/i;
        cnt+=1;
        if(a<=1){
            break;
        }
        
    }

    cout<<cnt;

    return 0;
}