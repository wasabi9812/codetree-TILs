#include <iostream>
#include <string>

using namespace std;

string input_str;
string target_str;

int main() {
    cin >> input_str;
    cin >> target_str;

    int idx = -1;
    int n = input_str.size();
    int t = target_str.size();
    for (int i=0; i<=n-t; i++){
        if(input_str.substr(i,t)==target_str){
            idx = i;
            break;
        }
    }

    cout<<idx;

    return 0;
}
