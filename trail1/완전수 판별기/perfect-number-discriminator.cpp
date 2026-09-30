#include <iostream>
using namespace std;

int main() {
    int a,sum;
    cin>>a;
    sum =0;
    for (int i=1; i<a; i++){
        if(a%i ==0){
            sum+=i;
        }
    }
    if (sum==a){
        cout<<"P";
    }
    else{
        cout<<"N";
    }
    return 0;
}