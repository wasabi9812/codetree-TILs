#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a,cnt;
    cin>>a; 
    int temp = a;
    cnt =0;
    for (int i=1; i<a+1; i++){
        
        temp = temp/i;
        cnt+=1;
        if(temp<=1){
            break;
        }
        
    }

    cout<<cnt;

    return 0;
}