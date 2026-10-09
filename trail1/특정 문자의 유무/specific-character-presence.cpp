#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    bool ee = false;
    bool ab = false;

    string str;
    cin>>str;

    ee = str.find("ee") != string::npos;
    ab = str.find("ab") != string::npos;
    if(ee){
        cout<<"Yes ";
    }
    else{
        cout<<"No ";
    }
    if(ab){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }
    return 0;
}