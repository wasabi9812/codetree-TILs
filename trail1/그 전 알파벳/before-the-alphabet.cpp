#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char a;
    cin>>a;
    char answer;
    if(a=='a'){
        answer = 'z';
    }
    else{
        int t = (int)a;
        t -=1;
        char c =(char)t;
        answer =c;
    }

    cout<<answer;
    return 0;
}