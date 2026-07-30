class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int maxcount=1;
        int count=1;

        for (int i=0;i<nums.length-1;i++){

            if (nums[i+1]-nums[i]==1){
                count+=1;
                if (maxcount<count) {
                    maxcount=count;
                }
            }
            else if (nums[i]==nums[i+1]){
                continue;
            }
            else{
                count=0;
            }

        }
        return maxcount;
        
    }
}
