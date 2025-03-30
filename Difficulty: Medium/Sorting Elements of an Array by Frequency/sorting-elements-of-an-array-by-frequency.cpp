#include <bits/stdc++.h>
using namespace std;


int a[1000000];
unordered_map<int, int> m;

bool sortByVal(const pair<int, int>& a, const pair<int, int>& b){
    if(a.second == b.second) return a.first < b.first;
    
    return a.second > b.second;
}


void sortByFreq(int n){
    
    vector<pair<int, int>> v;
    
    for(int i = 0;i<n;i++){
        m[a[i]]++;
    }
    
    copy(m.begin(), m.end(), back_inserter(v));
    
    sort(v.begin(), v.end(), sortByVal);
    
    for(int i = 0;i<v.size();i++){
        for(int j = 0;j<v[i].second;j++){
            cout << v[i].first << " ";
        }
    }
    
}

int main() {
	
	
	int t;
	cin >> t;
	
	
	while(t--){
	    m.clear();
	    
	    int n;
	    cin >> n;
	    
	    for(int i = 0;i<n;i++){
	        cin >> a[i];
	    }
	    
	    sortByFreq(n);
	    cout << endl;
	}
	
	return 0;
}