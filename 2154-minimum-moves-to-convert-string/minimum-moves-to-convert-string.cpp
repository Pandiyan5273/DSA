class Solution {
public:
    int minimumMoves(string s) {
        int n=s.size();
        int mov=0;
        for(int i=0;i<n;i++){
            if(s[i]=='X'){
                mov++;
                i+=2;
            }
        }
        return mov;
    }
};