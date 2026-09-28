#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int h,w,c;
    double b;
    cin>>h>>w;
    
    b = 10000*w/(h*h);
    c = b;
    cout<<c<<endl;
    if (b>=25){
        cout<<"Obesity";
    }


    return 0;
}