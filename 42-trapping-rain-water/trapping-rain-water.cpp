class Solution {
public:
    int trap(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        int lm=height[l];
        int rm=height[r];
        int res=0;
        while(l<r){
            if(lm<rm){
                l+=1;
                lm=max(lm,height[l]);
                res+=lm-height[l];
            }
            else{
                r-=1;
                rm=max(rm,height[r]);
                res+=rm-height[r];
            }
        }
        return res;
    }
};