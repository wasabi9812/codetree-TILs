#include <iostream>
#include <vector>
using namespace std;

int n;
int arr[100000];

void merge(int left, int mid, int right){
    vector<int> temp;

    int i = left;
    int j = mid + 1;

    while(i <= mid && j <= right){
        if(arr[i] <= arr[j]){
            temp.push_back(arr[i]);
            i++;
        }
        else{
            temp.push_back(arr[j]);
            j++;
        }
    }
    while(i<=mid){
        temp.push_back(arr[i]);
        i++;
    }
    while(j<=right){
        temp.push_back(arr[j]);
        j++;
    }

    for(int i=0; i<temp.size(); i++){
        arr[left+i]=temp[i];
    }

}


void mergeSort(int left, int right){

    if(left>= right){
        return;
    }

    int mid = left+(right-left)/2;

    mergeSort(left, mid);
    mergeSort(mid+1, right);
    merge(left, mid, right);

}


int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.

    mergeSort(0,n-1);
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}
