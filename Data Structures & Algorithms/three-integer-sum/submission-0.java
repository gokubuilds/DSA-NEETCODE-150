class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i=0 ; i<nums.length;i++){
            if (nums[i] > 0){
                 break;}
            if (i > 0 && nums[i] == nums[i - 1]){
                continue;
            }
            int start=i+1;
            int end = nums.length-1;
            while(start<end){
                int total = nums[i]+nums[start]+nums[end];
                if (total>0){
                    end--;
                }
                else if (total<0){
                    start++;
                }
                else if (total==0){
                    res.add(new ArrayList<>(List.of(nums[i],nums[start],nums[end])));
                    start++;
                    end--;
                    while (start < end && nums[start] == nums[start- 1]) {
                        start++;
                    }
                    
                }
            }
        }
        return res;
        
        
    }
}
