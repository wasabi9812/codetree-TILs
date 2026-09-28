#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a;
    cin>>a;
    if (a<1000){
        cout<<"no";
    }
    else if(3000>a && a>=1000){
        cout<<"mask";
    }
    else if(a>=3000){
        cout<<"book";
    }


    return 0;
}