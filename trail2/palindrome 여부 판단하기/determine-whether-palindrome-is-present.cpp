#include <iostream>
#include <string>

using namespace std;

string A;

bool isPalindrome(string &str){
    bool yes = true;
    for(int i=0; i<str.size()/2; i++){
        if(str[i]!=str[str.size()-1-i]){
            yes = false;
        }
    }
    if(yes){
        return true;
    }
    else{
        return false;
    }
}

int main() {
    cin >> A;

    // Please write your code here.
    if(isPalindrome(A)){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }

    return 0;
}