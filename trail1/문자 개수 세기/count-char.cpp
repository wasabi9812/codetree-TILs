#include <iostream>
using namespace std;

int main() {
    string str;
    int idx =0;
    getline(cin,str);
    char c;
    cin>>c;
    bool toggle = false;
    for (int i=0; i<str.length(); i++){        
        if(str[i]==c){
            idx++;
        }
    }
    cout<<idx;
    return 0;
}