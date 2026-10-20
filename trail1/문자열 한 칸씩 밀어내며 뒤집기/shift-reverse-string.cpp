#include <iostream>
#include <string>
using namespace std;

string input_str;
int q;

void first(string &str){
    int len = str.size();
    str = str.substr(1,len-1) + str.substr(0,1);
}

void second(string &str){
    int len = str.size();
    str = str.substr(len-1,1) + str.substr(0,len-1);
}

void third(string &str){
    int len = str.size();

    for(int i=0; i<len/2; i++){
        char ch;
        ch = str[i];
        str[i] = str[len-1-i];
        str[len-1-i] = ch;
    }
}

int main() {
    cin >> input_str >> q;

    for(int i=0; i<q; i++){
        int query_type;
        cin >> query_type;

        if(query_type == 1){
            first(input_str);
            cout << input_str << endl;
        }
        else if(query_type == 2){
            second(input_str);
            cout << input_str << endl;
        }
        else if(query_type == 3){
            third(input_str);
            cout << input_str << endl;
        }
    }

    return 0;
}