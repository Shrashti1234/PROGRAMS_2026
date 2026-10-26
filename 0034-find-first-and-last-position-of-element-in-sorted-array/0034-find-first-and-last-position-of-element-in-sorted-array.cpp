class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int low=0,high=(int)nums.size()-1;
        int first=-1,last=-1;
        while(low<=high){
            int m=low+(high-low)/2;
            if(nums[m]==target){
                first=m;
                last=m;
                int left=low,right=m-1;
                while(left<=right){
                    int mid=left+(right-left)/2;
                    if(nums[mid]==target){
                        first=mid;
                        right=mid-1;
                    }
                    else{
                        left=mid+1;
                    }
                }
                left=m+1;
                right=high;
                while(left<=right){
                    int m=left+(right-left)/2;
                    if(nums[m]==target){
                        last=m;
                        left=m+1;
                    }
                    else{
                        right=m-1;
                    }
                }
                return {first,last};
            }
            if(nums[m]<target){
                low=m+1;
            }
            else{
                high=m-1;
            }
        }
        return {-1,-1};
    }

              
    

};