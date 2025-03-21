class Solution {
public:
     int sum(vector<int>& nums){
        int tot=0;
        for(int num:nums){
            tot+=num;
        }
        return tot;
     }    
public:
    bool canPartition(vector<int>& nums) {
        if(sum(nums)%2!=0){
            return  false;
        }
        int target=sum(nums)/2;
        vector<bool>dp(target+1,false);
        dp[0]=true;
        for(int i=0;i<nums.size();i++){
            for(int j=target;j>=nums[i];j--){
                dp[j]=dp[j] || dp[j-nums[i]];
            }
        }
        return dp[target];
    }
};