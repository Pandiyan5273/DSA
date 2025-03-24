//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        int maxicurr=arr[0];
        int maxiglobal=arr[0];
        
        for(int i=1;i<arr.size();i++){
            maxicurr=max(maxicurr+arr[i],arr[i]);
            maxiglobal=max(maxiglobal,maxicurr);
        }
        return maxiglobal;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To discard any leftover newline characters
    while (t--)   // while testcases exist
    {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        cout << ob.maxSubarraySum(arr) << endl << "~" << endl;
    }
}
// } Driver Code Ends