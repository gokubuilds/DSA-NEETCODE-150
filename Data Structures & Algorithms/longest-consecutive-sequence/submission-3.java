class Solution {
    public int longestConsecutive(int[] nums) {
        int max_streak = 0;
        Set < Integer > set = new HashSet<>();
        for ( int i : nums ) {
            set.add(i);
        }
        for ( int num : nums ) {
            int streak = 0;
            int curr = num;
            while( set.contains( curr ) ) {
                streak++;
                curr++;
            }
            max_streak = Math.max(max_streak,streak);
        }
        return max_streak;
        
    }
}
