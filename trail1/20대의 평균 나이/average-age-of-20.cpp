#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a,sum=0,cnt=0;
    while(1){
        cin>>a;
        if (20<=a && a<30){
            sum+=a;
            cnt+=1;
        }
        else{
            break;
        }
    }
    double result = (double)sum/cnt;
    cout<<fixed;
    cout.precision(2);
    cout<<result;

    return 0;
}