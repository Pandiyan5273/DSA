//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:
    string findLargest(vector<int> &nums) {
    vector<string> strs;  
    for (int num : nums) {  
        strs.push_back(to_string(num));  
    }  

    sort(strs.begin(), strs.end(), [](const string& a, const string& b) {  
        return a + b > b + a;  
    });  

    string result = "";  
    for (const string& str : strs) {  
        result += str;  
    }  

    // Handle leading zeros case  
    if (result[0] == '0' && result.length() > 1) {  
        return "0";  
    }  

    return result; 
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        string ans = ob.findLargest(arr);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends