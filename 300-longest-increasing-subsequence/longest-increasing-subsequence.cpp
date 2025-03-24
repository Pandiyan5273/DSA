class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int>res(nums.size(),1);
        for(int i=nums.size()-1;i>=0;i--){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]<nums[j]){
                    res[i]=max(res[i],1+res[j]);
                }
            }
        }
        return *max_element(res.begin(),res.end());
    }
};