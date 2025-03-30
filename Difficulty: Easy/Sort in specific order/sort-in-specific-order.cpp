//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    void sortIt(vector<long long>& arr) {
vector<long long> odd, even;  
  for (long long x : arr) {  
    if (x % 2 == 0) {  
      even.push_back(x);  
    } else {  
      odd.push_back(x);  
    }  
  }  

  sort(odd.begin(), odd.end(), greater<long long>());  
  sort(even.begin(), even.end());  

  arr.clear();  
  arr.insert(arr.end(), odd.begin(), odd.end());  
  arr.insert(arr.end(), even.begin(), even.end());  
    }
};


//{ Driver Code Starts.
int main() {
    long long t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<long long> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        long long number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        ob.sortIt(arr);

        for (int i = 0; i < arr.size(); i++)
            cout << arr[i] << " ";
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends