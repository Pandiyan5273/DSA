class Solution {
public:
    string longestPalindrome(string s) {
            int resi=0;
    int resl=0;
    int n=s.size();
    string res="";
    for(int i=0;i<n;i++){
        int l=i,r=i;
        while(l>=0 && r<n && s[l]==s[r]){
            if((r-l+1)>resl){
                resi=l;
                resl=r-l+1;
            }
            l--;
            r++;
        }
        l=i,r=i+1;
        while(l>=0 && r<n && s[l]==s[r]){
            if((r-l+1)>resl){
                resi=l;
                resl=r-l+1;
            }
            l--;
            r++;
        }
    }
    res+=s.substr(resi,resl);
    return res;
    }
};