#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a,b,s;
    cin>>a>>b;
    s=1;
    for (int i=a; i<=b; i++){
        if (i%a==0){
            s = s*i;
        }
    }
    cout<<s;
    return 0;
}