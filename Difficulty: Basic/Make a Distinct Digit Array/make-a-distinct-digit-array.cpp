//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution{
	public:
   	vector<int>  common_digits(vector<int>nums){
   	    unordered_set<int> dis;
   	    for(int num:nums){
   	        string str=to_string(num);
   	        for(char c:str){
   	            dis.insert(c-'0');
   	        }
   	    }
   	    vector<int>res(dis.begin(),dis.end());
   	    sort(res.begin(),res.end());
   	    return res;
   	    
   	}    
};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<int>nums(n);
		for(int i = 0; i < nums.size(); i++)cin >> nums[i];
		Solution ob;
		vector<int> ans = ob.common_digits(nums);
		for(auto i: ans)
			cout << i << " ";
		cout << "\n";
	
cout << "~" << "\n";
}  
	return 0;
}
// } Driver Code Ends