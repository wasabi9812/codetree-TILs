#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    int q;

    cin >> str >> q;

    for(int i=0; i<q; i++){

        string temp[3];
        for(int j=0; j<3; j++){
            cin >> temp[j];
        }

        if(temp[0] == "1"){
            int a = stoi(temp[1])-1;
            int b = stoi(temp[2])-1;

            char temp2;
            temp2 = str[a];
            str[a] = str[b];
            str[b] = temp2;

            cout << str << endl;
        }
        else if(temp[0] == "2"){
            for(int k=0; k<str.size(); k++){
                if(str[k] == temp[1][0]){
                    str[k] = temp[2][0];
                }
            }
            cout << str << endl;
        }
    }

    return 0;
}